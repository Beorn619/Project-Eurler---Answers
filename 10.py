import math

x = 2000000
y = 1415

sieve = []
clean = []

def generateNums():
    for i in range(3, (x + 1), 2):
        sieve.append(i)
    sieve.insert(0, 2)


def findPrimes():
    for num in range(3, (y), 2):
        for place in range(4, len(sieve), 1):
            if sieve[place] % num == 0:
                sieve[place] = 0
    
def cleanUp():
    total = 0
    for i in range(0, len(sieve), 1):
        if sieve[i] != 0:
            clean.append(sieve[i])
            total = total + sieve[i]
    print(total)


generateNums()
findPrimes()
cleanUp()
