import ent
from random import randint

def Alice_generator(n):
    p = ent.strong_peseudoPrime_generator(n,20)
    g = ent.gen_primitive_root(p)
    return p,g

def random_generator(p):
    a = randint(1,p)
    b = randint(1,p)
    return a,b


def Diffie_Helman(n):
    p,g = Alice_generator(n)
    # for i in range(0, p - 1):
    #     print(ent.binary_power(g,i,p))
    # print(p)
    a, b = random_generator(p)
    allice_pub = allice_key(g,a,p)
    bob_pub = bob_key(g,b,p)
    a_check = alice_check(a,bob_pub,p)
    b_check = alice_check(b,allice_pub,p)
    if a_check == b_check:
        return a_check
    else:
        return -1


def allice_key(g,a,p):
    return ent.binary_power(g,a,p)

def bob_key(g,b,p):
    return ent.binary_power(g,b,p)

def bob_check(b,alice_pub,p):
    return ent.binary_power(alice_pub,b,p)

def alice_check(alice_key,b_pub,p):
    return ent.binary_power(b_pub,alice_key,p)



