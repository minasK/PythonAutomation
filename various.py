# prints all the prime numbers
nums=range(1,100)
# print(list(nums))

def prime(num):
    for x in range(2,num):
        if(num%x) == 0:
            return False
    return True

    primes=list(filter(prime,nums))
    prime(100)

    print(primes)

num1 = 2_001_011
num2 = 1_200
ans = num1/num2
print(f'{ans:,}')
print(f'{ans:,}')
