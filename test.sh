#!/bin/bash
set -euo pipefail

for py in python/day*.py; do
    (set -x && python3 $py)
done
