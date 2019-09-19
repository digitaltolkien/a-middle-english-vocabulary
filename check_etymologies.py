#!/usr/bin/env python3

from etym_patterns import check_etymology
from utils import extract_etymology, get_entries

success = 0
failure = 0
first_error = None

for etymology in sorted(
    (extract_etymology(entry) for entry in get_entries()),
    key=lambda x: (len(x), x)
):
    if etymology:
        c = check_etymology(etymology)
        if c:
            success += 1
        else:
            failure += 1
            if first_error is None:
                first_error = etymology

print(f"{success} successes; {failure} failures")
if first_error:
    print(f"first failure: {first_error}")
