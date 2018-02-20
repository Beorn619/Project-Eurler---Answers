num1 = 999
num2 = 999
final = 0

while num2 > 100:
    while num1 > 100:
        if str(num1 * num2) == str(num1 * num2)[::-1]:
            break
        else:
            num1 = num1 - 1

    if str(num1 * num2) == str(num1 * num2)[::-1] and (num1 * num2) > final:
        final = (num1 * num2)
    num2 = num2 - 1
    num1 = 999
print(final)



