import csv
import sys
from collections import Counter


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


if len(sys.argv) != 2:
    print("Usage: python main.py <file.csv>")
    sys.exit(1)

path = sys.argv[1]

try:
    with open(path) as f:
        rows = list(csv.DictReader(f))
except FileNotFoundError:
    print(f"Error: no such file '{path}'")
    sys.exit(1)

if not rows:
    print("File has no data rows.")
    sys.exit(0)

print(f"rows: {len(rows)}")

for header in rows[0].keys():
    values = [row[header] for row in rows]
    filled = [v for v in values if v.strip() != ""]
    missing = len(values) - len(filled)

    print(f"\n{header}: {missing} missing")

    if all(is_number(v) for v in filled):
        nums = [float(v) for v in filled]
        print(f"  numeric | min {min(nums)}, max {max(nums)}, avg {sum(nums)/len(nums):.1f}")
    else:
        counts = Counter(filled)
        print(f"  text    | {len(counts)} unique, most common: {counts.most_common(2)}")