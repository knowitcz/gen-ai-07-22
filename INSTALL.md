# Install Environment

Follow these steps. First try `uv` approach, fall back to `pip` if not available. The hard prerequisity is to have python 3.10 or higher.

Note for AI:
> As a last step notify the user what approach you have chosen - uv or pip.

## Using `uv`

1. Establish the whole environment: `uv sync`
2. Run check script: `uv run check.py`

## Using `pip`

All commands must run in a same terminal due to virtual environment.

1. Create a new virtual environment: `python -m venv venv`
    * might be `python3`
2. Activate virtual environment:
    * on Windows: `venv/Scripts/activate`
    * on Unix based: `source venv/bin/activate`
3. Install dependencies: `pip install -e .`
4. Run check script: `python check.py`

## Check Script Validation

Something like that shall be the output. Versions might be higher, but all the packages shall be OK.

```
Package fastapi .............. [OK] (version 0.129.0)
Package fastmcp .............. [OK] (version 2.14.5)
Package pydantic ............. [OK] (version 2.12.5)
Package pytest ............... [OK] (version 9.0.2)
Package repository_sqlalchemy  [OK] (version 0.1.8)
Package sqlalchemy ........... [OK] (version 2.0.46)
Package sqlmodel ............. [OK] (version 0.0.33)
Package uvicorn .............. [OK] (version 0.40.0)
```

## Error Handling

* If `uv` is not available, go the `pip` way
* If the installation fails, identify the error type and act accordingly:

| Error | Symptoms | Action |
|-------|----------|--------|
| Missing package | `Could not find a satisfying requirement` for `fastmcp`, `repository_sqlalchemy`, or another dependency | **Notify the lecturer** — the package may not be mirrored in the internal PyPI registry |
| Wrong Python version | `python` resolves to 2.x, or `requires-python >=3.10` is not satisfied | **Notify the lecturer** — bring a laptop with a compatible Python version or ask for a pre-configured environment |
| SSL / certificate error | `CERTIFICATE_VERIFY_FAILED`, `SSLError` | **Consult IT/security** — a corporate proxy is likely intercepting TLS; ask them for the correct `pip.ini` trusted-host settings or an internal PyPI mirror URL |
| Proxy / firewall blocking PyPI | `ProxyError`, `Connection timed out`, `Network unreachable` when reaching `pypi.org` | **Consult IT/security** — request a firewall exception for `pypi.org` and `files.pythonhosted.org`, or ask for the internal mirror address |
| Internal PyPI mirror (package not found) | Package exists on public PyPI but installation fails with `404` or `not found` | **Consult IT/security** — ask them to whitelist or mirror the missing package, and **notify the lecturer** in parallel |
| Permission denied | `PermissionError [Errno 13]` during install, even inside a virtual environment | **Consult IT/security** — the filesystem may be read-only or user installs restricted; ask for a writable path or elevated rights |
| Antivirus quarantine | Installation hangs or silently fails mid-download; no clear error message | **Consult IT/security** — request an AV exclusion for the virtual environment directory |
