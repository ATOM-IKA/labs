import time


def primes_slow(limit):
    result = []
    for n in range(2, limit + 1):
        simple = True
        for d in range(2, n):
            if n % d == 0:
                simple = False
        if simple:
            result.append(n)
    return result


def primes_sqrt(limit):
    result = []
    for n in range(2, limit + 1):
        simple = True
        d = 2
        while d * d <= n:
            if n % d == 0:
                simple = False
                break
            d += 1
        if simple:
            result.append(n)
    return result


def primes_odd(limit):
    result = [2]
    for n in range(3, limit + 1, 2):
        simple = True
        d = 3
        while d * d <= n:
            if n % d == 0:
                simple = False
                break
            d += 2
        if simple:
            result.append(n)
    return result


def primes_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]


functions = [("slow", primes_slow), ("sqrt", primes_sqrt), ("odd", primes_odd), ("sieve", primes_sieve)]

for limit in (1000, 5000, 10000):
    print("Предел", limit)
    reference = primes_slow(limit)
    for name, function in functions:
        start = time.perf_counter()
        result = function(limit)
        spent = (time.perf_counter() - start) * 1000
        print(f"  {name:6} найдено {len(result)}, совпадает с исходным: {result == reference}, время {spent:.2f} мс")
