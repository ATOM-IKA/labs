"""Замер характеристик исходного и оптимизированных вариантов."""
import json
import timeit

import primes

VARIANTS = [("v0", primes.primes_v0), ("v1", primes.primes_v1), ("v2", primes.primes_v2), ("v3", primes.primes_v3)]
LIMITS = [1000, 5000, 20000]


def measure():
    rows = []
    reference = {}
    for limit in LIMITS:
        reference[limit] = primes.primes_v0(limit)
    for limit in LIMITS:
        for name, function in VARIANTS:
            primes.divisions = 0
            result = function(limit)
            same = result == reference[limit]
            ops = primes.divisions
            repeat = 3 if (name == "v0" and limit >= 20000) else 5
            number = 1 if (name == "v0" and limit >= 5000) else 3
            seconds = min(timeit.repeat(lambda: function(limit), repeat=repeat, number=number)) / number
            rows.append({"limit": limit, "variant": name, "count": len(result), "same": same, "divisions": ops, "ms": seconds * 1000})
    return rows


if __name__ == "__main__":
    rows = measure()
    json.dump(rows, open("measure.json", "w"), indent=1)
    for r in rows:
        print(r)
