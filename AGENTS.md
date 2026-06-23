# AGENTS.md - Dell Ansible Collection for PowerStore

## Project Overview

This is the Ansible Galaxy collection for Dell PowerStore block and file storage arrays. It provides Ansible modules for automating provisioning and management of PowerStore resources.

- **Language:** Python
- **Collection namespace:** `dellemc.powerstore`
- **Collection version:** 3.8.1
- **SDK:** `PyPowerStore` v3.5.0
- **License:** GNU General Public License v3.0

## Architecture

The collection follows the standard Ansible Galaxy collection layout. Each module is a self-contained Python file under `plugins/modules/` that communicates with the PowerStore REST API through the `PyPowerStore` SDK.

### Authentication

Modules authenticate to a PowerStore array using `gateway_host`, `username`, `password`, and optional `verifycert` and `timeout` parameters. These are passed as module arguments in playbooks.

### SDK Strategy

Uses `PyPowerStore` — a Dell-published Python SDK for the PowerStore REST API, installed via `pip`. The required version is pinned in `requirements.txt`.

### Module Count

The collection includes approximately 90 modules covering PowerStore entities such as volumes, hosts, host groups, protection policies, snapshot rules, file systems, NAS servers, NFS exports, SMB shares, replication sessions, and more.

## Directory Structure

```
galaxy.yml                        Collection metadata (namespace, name, version)
plugins/
  modules/                        Ansible modules (one .py file per resource)
  module_utils/
    storage/                      Shared utility classes and SDK wrappers
  doc_fragments/                  Shared documentation fragments for module args
meta/                             Collection metadata (runtime.yml)
tests/
  unit/
    plugins/                      Unit tests (pytest)
playbooks/                        Example playbooks
docs/                             Module documentation
changelogs/                       Release changelog fragments
requirements.txt                  Python dependencies (PyPowerStore)
requirements.yml                  Ansible collection dependencies
```

## Build Commands

| Command | Description |
|---------|-------------|
| `ansible-galaxy collection build` | Build the collection tarball |
| `ansible-galaxy collection install <tarball>` | Install the collection locally |
| `pytest tests/unit/` | Run unit tests |

## Testing

### Unit Tests

- Test files follow `test_*.py` convention in `tests/unit/plugins/`.
- Framework: `pytest` with `unittest.mock` for mocking SDK calls.
- No hardware required.

### Running Tests

```bash
# Install test dependencies
pip install -r requirements.txt
pip install -r dev-requirements.txt

# Run unit tests
pytest tests/unit/ -v

# Run with coverage
pytest tests/unit/ --cov=plugins --cov-report=html
```

## Code Style and Conventions

### Module Pattern

Each module follows the standard Ansible module pattern:
1. `DOCUMENTATION`, `EXAMPLES`, and `RETURN` docstrings at the top.
2. An `AnsibleModule` argument spec defining parameters.
3. A main class that wraps SDK calls and handles idempotency (check mode support).
4. `module.exit_json()` for success, `module.fail_json()` for errors.

### Shared Utilities

- `plugins/module_utils/storage/` contains shared base classes and SDK initialization code.
- `plugins/doc_fragments/` contains reusable documentation for common parameters (connection details).

### File Header

All source files must include the Dell copyright and GPL v3.0 license header.

## Common Development Tasks

### Adding a New Module

1. Create `plugins/modules/<resource>.py` following the Ansible module pattern.
2. Add shared documentation fragments if new common parameters are introduced.
3. Add unit tests in `tests/unit/plugins/`.
4. Add example playbooks in `playbooks/`.
5. Update `changelogs/` with a changelog fragment.
6. Bump the version in `galaxy.yml` if needed.

### Updating the SDK

Update `requirements.txt` with the new `PyPowerStore` version and test against the new SDK.

## CI/CD

GitHub Actions workflows in `.github/workflows/`. Code coverage tracked via `codecov.yml`.

## Code Ownership

All files are owned by the maintainers defined in `.github/CODEOWNERS`.
