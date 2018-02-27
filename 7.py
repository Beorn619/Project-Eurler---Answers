count = 0
number = 2
total = 0



def isPrime(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i = i + 1
    return True



while number < 1000000:
    if number % 10000 == 0:
            print(number)
    if isPrime(number):
        total = total + number
    number = number + 1
print(total)
    


        
