# KNOWLEDGE.md — ansible-powerstore

<!-- yaml-metadata-start -->
scope_paths: ["./"]
capture_git_sha: "114262ceec0c7467b97de2583d4ec360c351a21a"
status: "current"
auto_update: false
preview_before_apply: true
scaffold_version: "1.0"
# session_state: { is_complete: true }
<!-- yaml-metadata-end -->

<!-- quick-reference-start -->
## Agent Quick Reference

| Section | Heading | Summary | never_again_count |
|---------|---------|---------|-------------------|
| Component Overview | `## Component Overview` | dellemc.powerstore collection for PowerStore | — |
| Architectural Rationale | `## Architectural Rationale` | PyPowerStore SDK; Ansible collection pattern | — |
| Failure Modes & Gotchas | `## Failure Modes & Gotchas` | SDK coupling, idempotency, verify_ssl | 0 |
| Implicit Contracts | `## Implicit Contracts` | Connection params, ordering, action groups | — |
<!-- quick-reference-end -->

## Five Questions Quick Reference

### What does it do?
Ansible Galaxy collection `dellemc.powerstore` (v3.8.1). Provides 45 modules for declarative, idempotent management of Dell PowerStore block and file storage arrays. Uses `PyPowerStore` (==3.4.2) Python SDK.

### How do you modify it?
Create module file in `plugins/modules/`, add example playbook in `playbooks/modules/`, add unit test in `tests/unit/plugins/modules/`, append module FQCN to `meta/runtime.yml` action group.

### What breaks?
SDK version mismatch is a blocking defect. Missing action group entry causes `module_defaults` to silently skip the module. `verifycert: false` in production violates security constitution.

### What depends on it?
`PyPowerStore` ==3.4.2, Ansible >= 2.15.0. Ordering: dependent resources must exist before referencing them.

### What's undocumented?
`powerstore_base.py` (base class), `configuration.py` (`ConfigurationSDK`), `provisioning.py`. Defaults to `NullHandler` — **no file is written by default**. File logging enabled via environment variable toggle (truthy values `1`/`true`/`yes`). Outlier compared to other storage collections.

---

## Component Overview

Ansible Galaxy collection `dellemc.powerstore` (v3.8.1) for Dell PowerStore block and file storage arrays. 45 modules covering volumes, hosts, host groups, protection policies, snapshot rules, file systems, file system snapshots, NAS servers, NFS exports, SMB shares, replication sessions, replication groups, storage containers, certificates, DNS, email, NTP, networks, LDAP, remote support, security config, and more.

---

## Architectural Rationale

Standard Ansible Galaxy collection layout. Each module is a self-contained Python file under `plugins/modules/` that communicates with the PowerStore REST API through the `PyPowerStore` SDK.

**SDK strategy:** Static import, checked at module load via `HAS_PY4PS` flag. Version pinned at `==3.4.2` in `requirements.txt`.

---

## Failure Modes & Gotchas

### 1. SDK version coupling

Each collection release is tested against exactly one SDK version (or tight range for PyU4V). A mismatch between collection and SDK version is a blocking defect. Never update `requirements.txt` SDK versions without verifying against the corresponding collection release notes.

### 2. Idempotency assumptions

Modules are designed to be idempotent but some parameters may be accepted by the module yet ignored by the underlying API. Always verify with a second run.

### 3. Verify SSL setting

`verifycert: false` is used in example playbooks but is a lab-only setting. Production requires `true`. Modules must not default to skipping verification.

### 4. Acceptance test cleanup

If tests fail mid-run, resources may be left on the array. Clean up manually before re-running.

### Never Again

No incident-derived constraints recorded.

---

## Performance Characteristics

TBD — requires SME input.

---

## Implicit Contracts

**Connection parameters required:** All modules require `array_ip`, `username`, `password`, `verifycert` — these are not optional.

**Resource ordering:** Dependent resources must exist before being referenced (e.g., filesystem before snapshot, volume group before volumes, policies before assignment).

**Action group registration:** Every new module must be appended to the `dellemc.powerstore.all` action group in `meta/runtime.yml`.

---

## Threading & Synchronization

Ansible handles concurrency via forks at the play level. Individual module executions are single-threaded.

---

## Build System & Configuration

| Command | Description |
|---------|-------------|
| `ansible-galaxy collection build` | Build collection tarball |
| `ansible-galaxy collection install <tarball>` | Install locally |
| `pytest tests/unit/` | Run unit tests |
| `ansible-playbook --syntax-check` | Validate playbook syntax |

---

## Operational Knowledge

Defaults to `NullHandler` — **no file is written by default**. File logging enabled via environment variable toggle (truthy values `1`/`true`/`yes`). Outlier compared to other storage collections.

---

## General Context

No additional context beyond what has been captured.

---

## References

- [Ansible Galaxy — dellemc.powerstore](https://galaxy.ansible.com/dellemc/powerstore)
- [Ansible Collection Developer Guide](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html)

---

## Governance Spec Discrepancies

No discrepancies detected.
