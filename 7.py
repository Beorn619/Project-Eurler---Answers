count = 0
number = 0



def isPrime(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i = i + 1
    return True



while count < 10003:
    if isPrime(number):
        if count % 1000 == 0:
            print(count)
        count = count + 1
    number = number + 1
print(number - 1)


        
