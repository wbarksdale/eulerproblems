# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_mult_below(n: int):
    sum = 0
    for i in range(n):
        if i % 3 == 0:
            sum += i
        if i % 5 == 0:
            sum += i
    return sum



print(f"The sum of all multiples of 3 and 5 below {10} is {sum_of_mult_below(10)}")
print(f"The sum of all multiples of 3 and 5 below {1000} is {sum_of_mult_below(1000)}")
