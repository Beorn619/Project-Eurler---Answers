sum_of_squares = 0
square_of_sum = 0
i = 1

while i <= 100:
    sum_of_squares = sum_of_squares + (i * i)
    square_of_sum = square_of_sum + i
    i = i + 1
print((square_of_sum * square_of_sum) - sum_of_squares)
