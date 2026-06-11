# Architecture: ansible-powerstore

## Metadata

<!-- yaml-metadata-start -->
scope_paths: ["./"]
capture_git_sha: "166f8d0208afe2139ae3fd1d0575919126f1d7d3"
status: "current"
auto_update: false
preview_before_apply: true
scaffold_version: "1.0"
<!-- yaml-metadata-end -->

---

## Purpose and Structure

Ansible Galaxy collection `dellemc.powerstore` (v3.8.1) for Dell PowerStore block and file storage arrays. Provides 45 modules for declarative, idempotent resource management via the PowerStore REST API.

Published to Ansible Galaxy under the `dellemc` namespace. Uses the `PyPowerStore` Python SDK (==3.4.2).

---

## Components

| Component | Path | Responsibility |
|-----------|------|---------------|
| Collection metadata | `galaxy.yml` | Namespace, name, version, dependencies |
| Modules | `plugins/modules/*.py` | One file per resource (45 modules) |
| Module utilities | `plugins/module_utils/storage/dell/` | SDK init, connection factory, logger, error helpers |
| Domain helpers | `plugins/module_utils/storage/dell/libraries/` | `powerstore_base.py` (base class), `configuration.py` (`ConfigurationSDK`), `provisioning.py` |
| Doc fragments | `plugins/doc_fragments/powerstore.py` | Shared DOCUMENTATION fragment for connection params |
| Runtime metadata | `meta/runtime.yml` | `meta/runtime.yml` contains 21 tombstone entries for deprecated `dellemc_powerstore_*` prefixed modules redirected to their current names. |
| Execution env | `meta/execution-environment.yml` | EE definition |
| Example playbooks | `playbooks/modules/` | One example playbook per module |
| Unit tests | `tests/unit/plugins/modules/` | One test file per module |
| Mock helpers | `tests/unit/plugins/module_utils/` | API mock utilities |
| Docs | `docs/` | Generated module documentation |
| Python deps | `requirements.txt` | `PyPowerStore==3.4.2` |

---

## Key Behaviors

### Module Execution Pattern

**GIVEN** a playbook declares a desired resource state using `state: present`
**WHEN** the Ansible engine runs the module
**THEN** the module (1) validates parameters, (2) initialises SDK client via `self.conn`, (3) fetches current resource state via GET, (4) compares current vs desired, (5) applies no change if identical (`changed=false`), (6) applies delta via SDK PUT/POST if different, (7) returns `changed=true` + updated resource details

### Idempotency

**GIVEN** a module has been run and the resource already matches the declared state
**WHEN** the same playbook is run again
**THEN** the module returns `changed=false` without making any SDK write call

### Check Mode

**GIVEN** `--check` is passed to `ansible-playbook`
**WHEN** the module would normally apply a change
**THEN** the module reports `changed=true` and the intended change but skips all SDK write calls

### Action Group

**GIVEN** a playbook uses `module_defaults` with `group/dellemc.powerstore.all`
**WHEN** any module in the collection is invoked
**THEN** shared connection parameters are injected without repeating them per task

---

## Interfaces

### Connection Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `array_ip` | str | Yes | Management IP or FQDN |
| `username` | str | Yes | API username |
| `password` | str | Yes | API password (`no_log: True`) |
| `verifycert` | bool | Yes | TLS verification (`true` for production) |

### Module Return Contract

| Return key | Type | Description |
|------------|------|-------------|
| `changed` | bool | `true` if the module made any change |
| `<resource>_details` | dict/list | Current resource state after execution |

---

## Dependencies

| Depends On | For |
|------------|-----|
| `PyPowerStore` ==3.4.2 | Platform Python SDK |
| Ansible >= 2.15.0 | Ansible engine |

---

## Known Constraints

1. **SDK version coupling is strict** — each collection release is tested against exactly one SDK version (or tight range). Mismatch is a blocking defect.
2. **`meta/runtime.yml` is source of truth** — tombstone/redirect entries for deprecated module names must not be removed.
3. **Tombstone entries are permanent** — deprecated `dellemc_powerstore_*` prefixed module names must not be removed.
4. **`verifycert: false` is lab-only** — production requires `true`.
5. **Example playbooks are mandatory** — every module must ship a working example in `playbooks/modules/`.

---

## Change History

| Date | Feature | What Changed | Author |
|------|---------|-------------|--------|
| 2026-06-10 | Initial architecture | Provider-specific architecture extracted from generic multi-provider doc | architecture-agent |
