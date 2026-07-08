#!/bin/bash
# Harbor verifier entry point.
# Runs pytest, then writes reward and CTRF results to /logs/verifier/ as Harbor requires.

set -euo pipefail

VERIFIER_DIR="/logs/verifier"
mkdir -p "$VERIFIER_DIR"

# Run pytest with CTRF reporter; capture exit code without aborting on test failure
pytest /tests/test_outputs.py \
    -rA \
    --json-ctrf "$VERIFIER_DIR/ctrf.json" \
    ; EXIT=$?

# Write reward: 1 if all tests passed, 0 otherwise
if [ "$EXIT" -eq 0 ]; then
    echo 1 > "$VERIFIER_DIR/reward.txt"
else
    echo 0 > "$VERIFIER_DIR/reward.txt"
fi

exit "$EXIT"
