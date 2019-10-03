#!/usr/bin/env python3

from etym_patterns import check_etymology
from utils import extract_etymology, get_entries

success = 0
failure = 0
errors = []

for etymology in sorted(
    (extract_etymology(entry) for entry in get_entries()), key=lambda x: (len(x), x)
):
    if etymology:
        c = check_etymology(etymology)
        if c:
            success += 1
        else:
            failure += 1
            errors.append(etymology)

print(f"{success} successes; {failure} failures")
if errors:
    for error in errors[:10]:
        print(error)
