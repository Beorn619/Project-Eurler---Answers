a = 3
b = 4
c = 5

while c < 1000:
    while b < 1000:
        while a < 1000:
            if a < b < c and (a*a) + (b*b) == (c*c):
                if a + b + c == 1000:
                    print(a * b * c)

            a = a + 1
        b = b + 1
        a = 3
    c = c + 1
    if c % 10 == 0:  
        print("c " + str(c))
    b = 4
    a = 3
