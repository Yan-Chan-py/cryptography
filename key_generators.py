import ent
from random import randint
import cryprosystems



def generate_RSA_keys(n):

    p = ent.strong_peseudoPrime_generator(n, 20)
    q = ent.strong_peseudoPrime_generator(n, 20)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = randint(2, phi + 1)
    while not ent.coprime(e, phi):
        e = randint(2, phi - 1)
        if ent.coprime(e, phi):
            break
    d = ent.inverse(e, phi)
    return {"open_keys": [n, e], "secret_key": d}


def generate_rabin_keys(n):
    p = ent.strong_peseudoPrime_generator(n, 20)
    q = ent.strong_peseudoPrime_generator(2 * n, 20)
    return {"public_key": p * q, "secret_key": [p, q]}


def generate_EL_gamal_keys(n):
    p = ent.strong_peseudoPrime_generator(n, 20)
    g = ent.gen_primitive_root(p)
    a = randint(1, p - 1)
    h = ent.binary_power(g, a, p)
    return {"public key": [p, g, h], "private key": a}
keys = generate_RSA_keys(2**1024)
n =  keys["open_keys"][0]
e = keys["open_keys"][1]
d = keys["secret_key"]

M = cryprosystems.encrypt_RSA(12312123131315465475634542525235235221231245546546463525251512515142141421,e,n)
print(M)
print(cryprosystems.decrypt_RSA(M,d,n))



