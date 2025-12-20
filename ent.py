from typing import Tuple
from random import randint


def gcd(a, b) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def gcd_extended(a, b) -> Tuple:
    r_0, r_1 = a, b
    u_1, v_1 = 1, 0
    u_2, v_2 = 0, 1
    while r_1 != 0:
        q = r_0 // r_1
        u_1, u_2 = u_2, u_1 - u_2 * q
        v_1, v_2 = v_2, v_1 - v_2 * q
        r_0, r_1 = r_1, r_0 % r_1
    return (u_1, v_1)


def coprime(a, b) -> bool:
    return gcd(a, b) == 1


def inverse(a, mod) :
    if not coprime(a, mod):
        return "no inverse"
    return gcd_extended(a, mod)[0] % mod


def chinease_remainder(n_1, n_2, x_1, x_2) -> int:
    mod = n_1 * n_2
    u, v = gcd_extended(n_1, n_2)
    return (u * n_1 * x_2 + v * n_2 * x_1) % mod


def binary_power(a, b, m):
    res = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        a = (a * a) % m
        b = b // 2

    return res


def extract_powers(n, m) -> Tuple:
    powers = 0
    while n % m == 0:
        n //= m
        powers += 1
    return powers, n





def Jacobi(n, m):
    n = n % m
    if n <= 1:
        return n
    if n % 2 == 0:
        powers, remainder = extract_powers(n, 2)
        if powers % 2 == 0:
            return Jacobi(remainder, m)
        return Jacobi(remainder, m) * ((-1) ** ((m**2 - 1) // 8))
    return Jacobi(m % n, n) * ((-1) ** ((n - 1) * (m - 1) // 4))


def Euler_prime_test(n, m):
    a = randint(1, n)
    J = Jacobi(a, n) % n
    if binary_power(a, (n - 1) // 2, n) != J:
        return False
    return True


def strong_peseudoPrime_test(n, m):
    if n > 2 and n % 2 == 0:
        return False
    s, remainder = extract_powers(n - 1, 2)
    for _ in range(m):
        x = randint(1, n - 1)
        if gcd(x, n) != 1:
            return False
        y_0 = binary_power(x, remainder, n)
        if y_0 == 1 or y_0 == n - 1:
            continue
        for _ in range(s - 1):
            y_0 = binary_power(y_0, 2, n)
            if y_0 == n - 1:
                break
        else:
            return False
    return True


def gen_Euler_prime(l):
    for _ in range(2 * l - 2 - l):
        a = randint(l, 2 * l - 2)
        if a % 2 == 0:
            a += 1
        if Euler_prime_test(a, 10):
            return a
        continue
    return -1


def strong_peseudoPrime_generator(n: int, m: int) -> int:
    for _ in range(2 * n - 2 - n):
        a = randint(n, 2 * n - 2)
        if a % 2 == 0:
            a += 1
        if strong_peseudoPrime_test(a, m):
            return a
        continue
    return -1


def phi(n):
    y = n
    i = 2
    temp_n = n
    while i * i <= temp_n:
        if temp_n % i == 0:
            while temp_n % i == 0:
                temp_n //= i
            y = (y // i) * (i - 1)
        i += 1
    if temp_n > 1:
        y = (y // temp_n) * (temp_n - 1)
    return y


def factor(n: int):
    primes = []
    p = 2
    while pow(p, 2) <= n:
        if n % p == 0:
            primes.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        primes.append(n)
    return primes


def gen_primitive_root(p):
    root = 0
    if strong_peseudoPrime_test(p, 20):
        f = p - 1
    else:
        f = phi(p)
    factors = factor(f)
    for g in range(2, p):
        is_primitive_root = True
        for q in factors:
            if binary_power(g, f // q, p) == 1:
                is_primitive_root = False
                break
        if is_primitive_root:
            root = g
            break
    return root


def sqrt_modp(n, p):
    n = n % p
    if n % p == 0:
        return  [0]
    if binary_power(n, (p - 1) // 2, p) != 1:
        return "no roots"
    roots = []
    if p % 4 == 3:
        m = p // 4
        x_1 = binary_power(n, m + 1, p)
        x_2 = (-x_1) % p
        roots.append(x_1)
        roots.append(x_2)
        return roots
    elif p % 8 == 5:
        d = binary_power(n, (p - 1) // 4, p)

        if d == 1:
            x_1 = binary_power(n, (p + 3) // 8, p)
        else:
            x_1 = (binary_power(n, (p + 3) // 8, p) * binary_power(2, (p - 1) // 4, p)) % p

        x_2 = p - x_1
        roots.append(x_1)
        roots.append(x_2)
        return roots
    elif p % 8 == 1:
        s, r = extract_powers(p - 1, 2)
        z = 2
        while binary_power(z, (p - 1) // 2, p) != p - 1:
            z += 1
        m = s
        c = binary_power(z, r, p)
        t = binary_power(n, r, p)
        r = binary_power(n, (r + 1) // 2, p)
        while t != 1:
            tt = t
            i = 0
            for k in range(1, m):
                tt = (tt * tt) % p
                if tt == 1:
                    i = k
                    break
            b_pow = m - i - 1
            b = c
            for _ in range(b_pow):
                b = (b * b) % p

            m = i
            c = (b * b) % p
            t = (t * c) % p
            r = (r * b) % p

    return [r, p - r]


def sqroot_modpq(x, n):
    prime_factors = factor(n)
    p = prime_factors[0]
    q = prime_factors[1]
    roots_p1 = sqrt_modp(x, p)
    roots_p2 = sqrt_modp(x, q)
    if roots_p1 == "no roots" or roots_p2 == "no roots":
        return "no roots"
    root_p = roots_p1[0]
    root_q = roots_p2[0]
    x = chinease_remainder(p, q, root_p, root_q)
    y = chinease_remainder(p, q, root_p, -root_q)
    return [x, n - x, y, n - y]


def sqrt_modpq_factors(x, p, q):
    roots_p1 = sqrt_modp(x, p)
    roots_p2 = sqrt_modp(x, q)
    print(p * q)
    if roots_p1 == "no roots" or roots_p2 == "no roots":
        return "no roots"
    root_p = roots_p1[0]
    root_q = roots_p2[0]
    x = chinease_remainder(p, q, root_p, root_q)
    y = chinease_remainder(p, q, root_p, -root_q)
    return [x, p * q - x, y, p * q - y]


def gen_Sophie_German_primes(n):
    while True:
        q = strong_peseudoPrime_generator(n,100)
        p = 2 *q + 1
        if strong_peseudoPrime_test(p,100):
            return [p,q]

def gen_primitive_root_safe_prime(p, q):
    while True:
        g = randint(2, p - 2)

        if binary_power(g, 2, p) == 1:
            continue
        if binary_power(g, q, p) == 1:
            continue

        return g
