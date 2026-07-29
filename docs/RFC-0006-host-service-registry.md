# RFC-0006 — Host service endpoint registry

**Status:** Accepted for Alexandria pack tooling

**Schema:** [`schemas/service-registry.schema.json`](../schemas/service-registry.schema.json)

**Issue:** [#25](https://github.com/dhk/alexandria/issues/25)

## 01. Purpose

Small shared Ubuntu hosts need one authority for service endpoint ownership. A
port probe alone is not a reservation, and per-repository manifests cannot
prevent two installers owned by different Unix users from selecting the same
local endpoint or Tailscale route.

Version 1 is a deliberately small, host-local broker implemented as a privileged
command over a root-owned, locked JSON file. It coordinates cooperating pack
installers without adding Consul, Kubernetes, or a long-running daemon.

## 02. Authority and ownership

The authoritative state is `/var/lib/common-services/registry.json`. It is
root-owned, mode `0644`, and contains no credentials or capability-path tokens.
Mutations are performed through `/usr/local/bin/service-registry`, normally via
`sudo`. The adjacent lock file is mode `0600`.

Every mutation takes an exclusive `flock`, validates the complete document, and
commits with `fsync` plus atomic replacement. The previous document is preserved
as `registry.json.bak`. Consequently, concurrent cooperating installers cannot
receive the same reservation. The registry remains advisory at the operating
system boundary: an unrelated process can still bind a port without consulting
it. Reconciliation makes that drift visible; systemd socket activation is the
stronger future end state.

Registry state is independent of Git checkouts, uv installations, pack releases,
and application data. Upgrade and rollback never release or reassign entries.

## 03. Namespaces and ranges

Version 1 reserves TCP loopback endpoints only. Two independent collision
namespaces exist:

1. Local endpoint: `(protocol, bind address, port)`. Wildcard addresses conflict
   with matching loopback reservations.
2. External route: `(host, HTTPS port, normalized path)`. A route reservation does
   not imply or replace a local endpoint reservation.

The default, non-overlapping managed ranges are:

| Band | Range | Policy |
|---|---:|---|
| Static | `8700–8799` | Explicit stable assignments for named services |
| Dynamic | `8800–8999` | Allocator-selected, durable assignments |

Range boundaries are stored in the registry. A caller that presents different
ranges fails instead of silently changing allocation policy. Ports outside these
bands may not be allocator-selected; version 1 pack declarations use the static
band.

## 04. Record contract

Each entry records a stable service ID, display name, Unix owner, optional
systemd user unit, provenance, one local endpoint, optional health identity, and
optional Tailscale Serve or Funnel route. `created_at` survives idempotent
upgrades; `updated_at` records the last declaration. The normative machine shape
is the linked JSON Schema.

Lifecycle is reported from declared and observed state rather than trusted as a
manually written label:

- **reserved** — a durable declaration exists;
- **installed** — its declared unit or listener is observed;
- **healthy** — every configured listener, unit, health identity, and route check
  passes;
- **stale** — a required observation is missing or has drifted;
- **released** — the entry was explicitly removed. The current document no longer
  contains it, while the backup provides immediate recovery history.

`list`, `check`, and `reconcile` never print secrets. Health URLs must be ordinary
local health endpoints, never token-bearing capability paths.

## 05. Operator contract

```text
service-registry list
sudo service-registry reserve <service> --port N ...
sudo service-registry reserve <service> --allocate ...
sudo service-registry reserve-route <service> --https-port 443 --path /path ...
service-registry check [service]
sudo service-registry reconcile [service]
sudo service-registry release <service> --yes
```

Static collision errors identify the owning service. Dynamic allocation happens
while holding the registry lock and persists like a static assignment. Importing
an already-running known service requires the explicit `--adopt-listener` flag.
A differing reservation is never silently migrated. Release is explicit and is
not part of install rollback.

`list` combines the declaration with current listener and health observations.
`check` evaluates declared services. `reconcile` additionally scans both managed
ranges for unknown listeners and compares declared systemd user units, health
identities, and Tailscale Serve/Funnel routes. It reports missing listeners, stale
units, route drift, and unknown listeners without changing any state.

## 06. Pack integration and initial migration

`deploy/pack.toml` declares the registry location, bands, and entries required by
a pack. The generated installer:

1. installs or safely upgrades the marked helper, backing up an earlier managed
   copy and refusing an unknown executable non-interactively;
2. reserves every endpoint and route before writing systemd units, restarting
   services, or changing Tailscale configuration;
3. imports existing listeners only where the manifest explicitly says they are
   the known owner;
4. verifies the declarations in the installation front panel;
5. preserves all reservations if later installation work fails or rolls back.

The first Alexandria pack imports the existing Lobster assignments unchanged:

| Service | Owner | Local endpoint | External path |
|---|---|---|---|
| Wingman | `dhk` | `127.0.0.1:8787` | `/` |
| Wingman (Trent) | `trent` | `127.0.0.1:8788` | `/trent` |
| Alexandria | `dhk` | `127.0.0.1:8797` | `/alexandria` |

The helper is incubated in Alexandria's generic pack tooling. Issue
[#26](https://github.com/dhk/alexandria/issues/26) tracks extracting it to a
shared `common/services` home after operational experience.

## 07. Recovery

If the registry is unavailable or damaged, installers must stop before service
or Tailscale mutation. Do not delete the registry or pick replacement ports.

1. Stop concurrent pack installs.
2. Inspect `registry.json` and `registry.json.bak`; neither contains secrets.
3. Validate the selected copy against `schemas/service-registry.schema.json` and
   compare it with `systemctl --user`, listening sockets, health endpoints, and
   `tailscale serve status --json` / `tailscale funnel status --json`.
4. Restore the selected copy atomically as root with owner `root:root` and mode
   `0644`, then run `sudo service-registry reconcile`.
5. If no usable copy exists, rebuild declarations from reviewed pack manifests.
   Use `--adopt-listener` only after confirming the live process owner.

No recovery path automatically deletes entries, resets unrelated Tailscale
handlers, or moves a live service to another port.

## 08. Prior art and limits

The contract borrows stable naming and range governance from IANA, atomic
allocation from Kubernetes Services, catalog-plus-health semantics from Consul,
and the stronger socket-ownership model from systemd socket activation. Those
systems inform this small implementation; none is a runtime dependency.

Version 1 does not model UDP, non-loopback binds, distributed hosts, tombstone
history, or socket activation. It also cannot close the check-to-bind race against
non-cooperating processes. Those are explicit extension points, not implicit
behaviors.
