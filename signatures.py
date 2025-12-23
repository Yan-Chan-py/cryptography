import hashlib
from random import randint
import cryprosystems
import ent
import key_generators

def hash(message):
    return int(hashlib.sha256(message.encode()).hexdigest(), 16)

def sign_RSA(message, d, n):
    hashed = hash(message)
    if hashed > n :
        return "cannot sign"
    return  cryprosystems.encrypt_RSA(hashed, d, n)


def verify_RSA(message, signature,e, n):
    hashed = hash(message)
    sign_recieved = cryprosystems.encrypt_RSA(signature, e, n)
    print(hashed,sign_recieved)
    if sign_recieved!= hashed:
        return "cannot verify"
    return "match"

keys = key_generators.generate_RSA_keys(2**1024)
print(keys)
message = "хей"
n = keys["open_keys"][0]
e = keys["open_keys"][1]
d = keys["secret_key"]
signature = sign_RSA(message, d, n)
check = verify_RSA("хей", signature, e, n)
print(check)


def sign_disc_Log(message,p,g,a):
    hashed = hash(message)
    k = randint(1, p - 1)
    while True:
        k = randint(1, p - 1)
        if ent.gcd(k,p - 1) == 1:
            break
    r = ent.binary_power(g,k, p)
    inv = ent.inverse(k,p-1)
    s = (inv * (hashed - a* r)) % (p - 1)
    return [r,s]


def verify_disc_Log(message, signature,p,g,h):
    hashed = hash(message)
    r,s = signature[0],signature[1]
    if not( 0 < r < p):
        return "cannot verify"
    left = ent.binary_power(g,hashed,p)
    part_1 = ent.binary_power(h,r,p)
    part_2 = ent.binary_power(r,s,p)
    right = (part_1 * part_2) % p
    return left == right


# p, q =ent.gen_Sophie_German_primes(2**256)
# g = ent.gen_primitive_root_safe_prime(p,q)
# a = randint(1,p-1)
# h = ent.binary_power(g,a,p)
# m = "хй"
# signature = sign_disc_Log(m,p,g,a)
# check = verify_disc_Log(m,signature,p,g,h)
# print(check)
# print(p)
# print(g)


