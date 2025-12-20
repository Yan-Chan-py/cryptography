import math
import sys
sys.set_int_max_str_digits(2**30)
def fast_power(n,m):
    if m == 0:
        return 1 
    if m % 2 == 1:
        return n * fast_power(n,m - 1)
    return   fast_power(n**2,m//2)


print(fast_power(2,100000001))
