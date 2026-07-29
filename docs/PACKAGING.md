# Deployment packs

`scripts/pack.py` turns the current repository working tree into one
self-installing `.tar.gz` for an Ubuntu host. The packer is generic: project-specific
names, secrets, services, health checks, and capability URLs live in
`deploy/pack.toml`; the archive carries the standard-library-only
`deploy/install.py` installer and `deploy/docs.py` documentation launcher.

## Build and transfer

From the development checkout:

```bash
uv run --frozen python scripts/pack.py
```

The command writes an archive and a `sha256` sidecar under `dist/`, then prints
the exact commands for the generated filenames. The flow on Lobster is:

```bash
scp dist/alexandria-<bundle>.tar.gz dist/alexandria-<bundle>.tar.gz.sha256 lobster:
ssh lobster
sha256sum -c alexandria-<bundle>.tar.gz.sha256
tar -xzf alexandria-<bundle>.tar.gz
./alexandria-<bundle>/install.py
```

Run the installer from the transfer directory rather than changing into the
unpacked bundle. A successful default installation removes that bundle, while
the calling shell remains in a valid working directory.

The unpacked bundle also has a people-facing documentation launcher:

```bash
./launch-docs.py
```

It serves a generated index of the shipped README, Markdown documents, and HTML
specifications on a random loopback port and opens the local browser when one is
available. On headless Lobster, use `./launch-docs.py --no-browser --port 8000`
and an SSH port forward such as `ssh -L 8000:127.0.0.1:8000 lobster`.

The documentation index includes a collapsible **Installation front panel**.
Opening it runs local, no-spend component checks and turns each successful
component green. It checks the managed release link, installed command, canonical
host configuration, research credentials, systemd user service, HTTP health
response, MCP capability token, Tailscale path route, host service registry, and
documentation payload. It never calls OpenRouter and never returns secret or token values.

Use `./install.py --dry-run` to see resolved paths without changing anything.
Use `./install.py --check` to rerun the same component checks later without
changing the installation. Its exit status is non-zero when a required component
fails. `--check --skip-service` verifies the tool-only installation and reports
service components as skipped.

After a successful interactive installation, the installer offers to delete the
transferred `.tar.gz`, its `.sha256` sidecar, and the unpacked transfer directory.
`--yes` performs that cleanup automatically; `--keep-bundle` retains them. Cleanup
never runs after a failed installation and never removes installed releases,
rollback copies, service-unit backups, secrets, application data, or run artifacts.
Before cleanup, the documentation launcher, index, component checks, and a symlink
to the installed release are preserved under `~/src/alexandria/support/<bundle-id>`.
`--yes` accepts defaults and refuses to prompt; required secrets must already be
in the environment or canonical secrets file. `--skip-service` installs only the
uv tool and release payload.

The default interactive path is deliberately non-destructive. Before changing
anything, it detects an existing install root, `current` release, uv command, and
systemd unit. It asks before adopting an unmanaged directory, switching a managed
release, reinstalling an existing command, or replacing a differing unit. A unit
replacement first creates a timestamped `.bak-*` copy. Existing secret values are
never replaced, existing releases are never rewritten, and a real directory at
the intended `current` path is refused rather than removed. `--yes` accepts
replacement of already managed pack state, but still refuses to adopt an unknown
non-empty directory; that decision must be made interactively or avoided with a
different `--install-root`.

The shared registry helper receives the same treatment: an earlier managed helper
is backed up before replacement, while an unknown executable is refused
non-interactively. Registry entries are never removed by install, rollback, or
transfer cleanup.

## What the installer creates

The interactive Alexandria installer:

1. asks for an install root (default `~/src/alexandria`, matching Lobster's
   source-tree convention);
2. installs the payload as `releases/<bundle-id>` without deleting older releases;
3. installs or reinstalls the project with `uv tool install --reinstall`;
4. creates or updates `~/.config/alexandria/alexandria.env`, preserving unrelated
   settings and backing up a changed file before replacing its managed path entries;
5. asks, with hidden input, for any missing `OPENROUTER_API_KEY` and writes
   `~/.config/alexandria/secrets.env` with mode `0600`;
6. atomically points `current` at the new release;
7. installs the root-owned host registry helper and atomically imports or verifies
   Wingman (`8787`), Trent (`8788`), and Alexandria (`8797`) plus their Tailscale
   paths, failing a collision before unit or route mutation;
8. writes and enables `~/.config/systemd/user/alexandria-mcp.service`;
9. checks that `http://127.0.0.1:8797/health` identifies itself as Alexandria,
   rolling back when the new service fails health or another process owns the port;
10. offers to add the non-destructive Tailscale Funnel path `/alexandria`, forwarding
   to `http://127.0.0.1:8797`; an existing different mapping is shown and requires a
   separate, default-no replacement confirmation;
11. invokes the installed command with `--help` and runs the complete component
   panel, rolling back when a required component fails;
12. offers to enable systemd linger, then prints both the private loopback URL and
    the resolved `https://<tailscale-dns>/alexandria/mcp/<token>` URL;
13. preserves the documentation/front panel under the managed install root and,
    unless declined, removes only the three transfer artifacts.

If uv is absent, the interactive installer asks before downloading the official
installer from `astral.sh`. It never puts a secret in a command line or bundle.

The application data directory remains separate at
`~/.local/share/alexandria`: run records, drafts, and the capability token do not
move when a release changes. The `current` symlink is written as `ALEXANDRIA_REPO`
in the canonical host file, which the CLI and systemd service both read.

## Source and secret boundary

The packer includes tracked files, tracked working-tree edits, and non-ignored
untracked files. This makes it useful before a branch is published, but the
manifest marks such a bundle as dirty and the installer warns about it.

It excludes ignored files plus `.git`, `.scratch`, virtual environments, caches,
`dist`, local data directories, common key formats, capability-token files, and
files named `secrets.env` or `keys.env`. It does not attempt to recognize secrets
embedded in ordinary source files: review `git status` before packing. Files over
20 MB require the explicit `--allow-large-files` option.

## Upgrade and rollback model

A pack is a push deployment and contains no `.git` directory. Upgrade by building
and installing another pack. Do not run `alexandria-ctl cycle` against a packed
release: that command is the separate Git-checkout deployment lane and requires a
real clone that can run `git pull --ff-only`.

Every pack install keeps previous releases. A failed post-restart health check
restores the prior `current` target, reinstalls that uv tool version, and restarts
the service. Releases are not pruned automatically.

## Reuse for another tool

Copy `scripts/pack.py`, `deploy/install.py`, `deploy/docs.py`, and
`deploy/pack.toml`. Customize only the TOML:

- `[pack]`: tool identity, default paths, repository environment variable,
  canonical secrets file, required secret names, and exclusions;
- `[[services]]`: systemd unit, installed entry point, arguments, and loopback
  health URL (repeat for multiple services);
- `[capability]`: token file and URL templates to print after a healthy start;
  `{tailscale_dns}` is resolved on the destination host;
- `[tailscale]`: optional `serve` or `funnel` path mount, local target, HTTPS port,
  and whether that route is a required component.
- `[registry]` and `[[registry.entries]]`: the root-owned helper and data paths,
  non-overlapping static/dynamic bands, plus endpoint, health, unit, provenance,
  and independently reserved external-route declarations.

The installer consumes the JSON manifest generated from that TOML, so the target
host needs only a stock `python3`; it does not need TOML support or project
dependencies before installation.

## Current boundary

The Alexandria pack currently enables only the token-gated MCP service. The
standalone report web server is intentionally not installed as a remotely exposed
service while it is unauthenticated. Once the report routes are mounted under the
same capability token as MCP, they can travel through this same service and pack
without adding a second public port.

## Lobster front door

Alexandria stays bound to `127.0.0.1:8797`. Lobster's existing HTTPS Funnel on
port 443 continues to serve Wingman at `/`; the installer adds only the
`/alexandria` handler and does not reset or replace the other handlers. Tailscale
strips that mount path before forwarding, so Alexandria continues to serve MCP at
its local `/mcp/<token>` route while remote clients use:

```text
https://lobster.tail08dfce.ts.net/alexandria/mcp/<token>
```

The server auto-detects the machine's Tailscale DNS name for its Host allow-list.
Run `alexandria-ctl --tunnel-path /alexandria url` on Lobster to print the current
ready-to-paste connector URL without restarting the service.

## Host service registry

The registry lives outside every release at
`/var/lib/common-services/registry.json`; the helper is
`/usr/local/bin/service-registry`. Normal users may inspect it:

```bash
service-registry list
service-registry check
```

Run full host reconciliation with root privileges so systemd managers belonging
to other Unix users can be inspected:

```bash
sudo service-registry reconcile
```

Reconciliation reports missing or unknown managed-range listeners, stale units,
failed health identity checks, and Tailscale route drift. It never repairs or
deletes state. Recovery, ownership, allocation bands, and the normative record
contract are defined in
[RFC-0006](RFC-0006-host-service-registry.md).
