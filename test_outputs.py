"""
Verifier tests for the log-report task.

These tests check the *content* of /app/report.json, not merely its existence.
A no-op agent (empty file, missing file, or `{}`) must score reward 0.
The oracle solution must score reward 1.
"""
import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load():
    """Load and parse the report; fail clearly if missing or invalid JSON."""
    assert REPORT.exists(), f"{REPORT} not found — agent produced no report"
    raw = REPORT.read_text().strip()
    assert raw, f"{REPORT} is empty"
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise AssertionError(f"{REPORT} is not valid JSON: {exc}") from exc


def test_required_keys_present():
    """Report must contain all three required keys."""
    data = _load()
    for key in ("total_requests", "unique_ips", "top_path"):
        assert key in data, f"missing key '{key}' in report"


def test_total_requests():
    """total_requests must equal the number of lines in the access log (6)."""
    data = _load()
    assert isinstance(data["total_requests"], int), \
        f"total_requests must be an int, got {type(data['total_requests']).__name__}"
    assert data["total_requests"] == 6, \
        f"expected total_requests=6, got {data['total_requests']}"


def test_unique_ips():
    """unique_ips must equal the number of distinct client IPs (3)."""
    data = _load()
    assert isinstance(data["unique_ips"], int), \
        f"unique_ips must be an int, got {type(data['unique_ips']).__name__}"
    assert data["unique_ips"] == 3, \
        f"expected unique_ips=3, got {data['unique_ips']}"


def test_top_path():
    """top_path must be the most-requested URL path (/index.html)."""
    data = _load()
    assert isinstance(data["top_path"], str), \
        f"top_path must be a str, got {type(data['top_path']).__name__}"
    assert data["top_path"] == "/index.html", \
        f"expected top_path='/index.html', got {data['top_path']!r}"
