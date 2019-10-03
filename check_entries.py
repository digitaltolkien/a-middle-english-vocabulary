#!/usr/bin/env python3

from entry_patterns import check_entry
from utils import get_entries

success = 0
failure = 0
errors = []

for entry in sorted(get_entries(), key=lambda x: (len(x), x)):
    if entry:
        c = check_entry(entry)
        if c:
            success += 1
        else:
            failure += 1
            errors.append(entry)

print(f"{success} successes; {failure} failures")
if errors:
    print()
    for error in errors[:10]:
        print(error)
    print()
