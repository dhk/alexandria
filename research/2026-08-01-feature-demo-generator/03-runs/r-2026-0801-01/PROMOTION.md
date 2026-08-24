# Promotion note

This failed run produced no research output. Its `run.json`, exact brief, empty
claim and score artifacts, default failure report, and original manifest are
retained to preserve the operational history.

The three files under the local run's `raw/` directory were not promoted. They
contained OpenRouter `user_id` values and a key-specific account-settings URL.
Committing those private provider identifiers would violate Alexandria's
artifact-handling rules. The local source artifacts remain under the ignored
operational data directory and have these SHA-256 checksums:

```text
anthropic-claude-opus-4.7.json  1aba93ee9cbd93675f73dee003296b209e0f29e83d2dbcda32517e29bb933a28
google-gemini-3.1-pro-preview.json  e6180a4b50cbe2c4371e05ede708149e9bb05fa6c41645617cd90249b15de382
openai-gpt-5.4.json  7851c0be904d339b8ec6f267bc28b4766b779974c97874b87ec62a3e469aa6b6
```

Run `r-2026-0801-02` supersedes this attempt.
