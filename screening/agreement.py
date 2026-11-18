#!/usr/bin/env python3
"""Inter-rater agreement for title/abstract screening.

Reads screening_decisions.csv (one row per screened record) and compares the two
reviewers' FIRST independent decisions (columns reviewer_A_first, reviewer_B_first).
"include" and "maybe" are both counted as "advance to full text"; "exclude" stays
"exclude". Reports percent agreement, Cohen's kappa (Cohen, 1960) and the number of
conflicts (records where the two binary decisions differ).

Usage:
    python3 agreement.py [path/to/screening_decisions.csv]

Standard library only.
"""
import csv
import os
import sys
from collections import Counter

ADVANCE = {"include", "maybe"}


def to_binary(decision):
    d = decision.strip().lower()
    if d in ADVANCE:
        return "advance"
    if d == "exclude":
        return "exclude"
    raise ValueError(f"unexpected decision value: {decision!r}")


def cohen_kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    ca = Counter(a for a, _ in pairs)
    cb = Counter(b for _, b in pairs)
    pe = sum(ca[c] * cb[c] for c in set(ca) | set(cb)) / (n * n)
    return po, pe, (po - pe) / (1 - pe) if pe < 1 else 1.0


def main():
    default = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screening_decisions.csv")
    path = sys.argv[1] if len(sys.argv) > 1 else default
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    pairs = [(to_binary(r["reviewer_A_first"]), to_binary(r["reviewer_B_first"])) for r in rows]
    n = len(pairs)
    po, pe, k = cohen_kappa(pairs)
    table = Counter(pairs)
    conflicts = sum(a != b for a, b in pairs)

    print(f"Records screened:          {n}")
    print("2x2 table (A, B):")
    for a in ("advance", "exclude"):
        print(f"  A={a:<8} B=advance: {table[(a, 'advance')]:>4}   B=exclude: {table[(a, 'exclude')]:>4}")
    print(f"Agreements:                {n - conflicts}")
    print(f"Conflicts:                 {conflicts}")
    print(f"Percent agreement:         {100 * po:.1f}%")
    print(f"Expected agreement (pe):   {100 * pe:.1f}%")
    print(f"Cohen's kappa:             {k:.2f}")
    final = Counter(r["final_decision"].strip().lower() for r in rows)
    print(f"Final decisions:           {dict(final)}")


if __name__ == "__main__":
    main()
