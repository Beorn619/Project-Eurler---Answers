import math

goal = 100
primes = [2]
clean = []
for n in range(3,goal,2):
  sq = math.sqrt(n)
  for prime in primes:
    if sq < prime:
      primes.append(n)
      break
    elif n%prime == 0:
      break
    else:
      if primes[-1] != prime:
        continue
      else:
        primes.append(n)
        continue
    primes.append(n)


def cleanUp():
    total = 0
    for i in range(0, len(primes), 1):
        if primes[i] != 0:
            clean.append(primes[i])
            total = total + primes[i]
    print(total)
    
cleanUp()
