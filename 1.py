i = 1
total = 0

while i < 1000:
    if i % 5 == 0 or i % 3 == 0:
        total = total + i
    i = i + 1
print(total)
