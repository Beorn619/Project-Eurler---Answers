i = 1
x = 20

while i <= 20:
    if x % i == 0:
        i = i + 1
    else:
        x = x + 20
        i = 1
print(x)
