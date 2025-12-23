import math
def is_prime(n:int) -> int:
    if abs(n) == 2:
        return  true
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return false
    return true


def prime_list(n:int) -> list:
    number_list = list(range(2,n+1))
    
    for i in range (2, int(math.sqrt(n)) + 1):
        j = 0
        if is_prime(i):
            number_list = list(filter(lambda x :x % i != 0  ,number_list))
        #     number_list.insert(j,i)
        # j +=1    
         
    return number_list
            


print(prime_list(1000))