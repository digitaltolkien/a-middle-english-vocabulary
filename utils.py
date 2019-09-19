#!/usr/bin/env python3


def get_entries(filename="corrected.txt"):
    """
    yields entries from the corrected vocabulary, one per line
    """
    with open(filename) as f:
        s = []
        for line in f.readlines()[280:14406]:
            if line == "\n":
                if s:
                    yield " ".join(s)
                s = []
            else:
                s.append(line.strip())
        if s:
            yield " ".join(s)


def extract_etymology(entry):
    """
    extracts the etymology part of a given entry string
    """
    state = 0
    etymology = ""
    for ch in entry:
        if state == 0:
            if ch == "[":
                state = 1
            elif ch == "]":
                raise Exception(f"unexpected ] in: {entry}")
            else:
                pass
        elif state == 1:
            if ch == "[":
                raise Exception(f"unexpected [ in: {entry}")
            elif ch == "]":
                state = 2
            else:
                etymology += ch
        elif state == 2:
            if ch == "[":
                state = 1
                etymology = ""  # reset etymology so only last [...] is counted
            elif ch == "]":
                raise Exception(f"unexpected ] in: {entry}")
            else:
                pass
        else:
            raise Exception(f"unexpected state {state} in: {entry}")
    if state not in [0, 2]:
        raise Exception(f"unexpected end state {state} in: {entry}")

    return etymology
