import ent
from random import randint

from diff_helman import Diffie_Helman


def encrypt_RSA(M, e, n):
    return ent.binary_power(M, e, n)


def decrypt_RSA(C, d, n):
    return encrypt_RSA(C, d, n)


def encrypt_Rabin(M, n):
    return ent.binary_power(M, 2, n)

def decrypt_Rabin(C, p, q):
    return ent.sqrt_modpq_factors(C, p, q)


def encrypt_El_Gamal(p,g,m,h):
    r = randint(1,p - 1)
    c_1 = ent.binary_power(g, r, p)
    c_2 =m *  ent.binary_power(h, r, p)
    return [c_1, c_2]
def decrypt_El_Gamal(C, a, p):
    return (C[1] * ent.inverse(ent.binary_power(C[0], a, p),p)) % p





