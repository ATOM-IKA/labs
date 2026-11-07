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


def measure(name, function, limit, reference):
    start = time.time()
    result = function(limit)
    spent = (time.time() - start) * 1000
    same = result == reference
    print(f"  {name:6} найдено {len(result)}, верно: {same}, время {spent:.2f} мс")


for limit in (1000, 5000, 10000):
    print("Предел", limit)
    reference = primes_slow(limit)
    measure("slow", primes_slow, limit, reference)
    measure("sqrt", primes_sqrt, limit, reference)
    measure("odd", primes_odd, limit, reference)
    measure("sieve", primes_sieve, limit, reference)
