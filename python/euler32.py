# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def find_pandigital_products():
    solutions_set = set()
    for i in range(1, 9999):
        for j in range(1, 9999):
            product = i * j
            expr_string = f"{i}{j}{product}"
            is_pandigital = True
            # Short Circuit if product has a zero in it
            if "0" in expr_string:
                continue
            
            # Short circtuit if expr_string does not have 9 digits
            if len(expr_string) != 9:
                continue

            # check for each digit in the expr string
            for z in range(1, 10):
                count = sum(map(lambda x : 1 if f"{z}" in x else 0, expr_string))
                if count != 1:
                    is_pandigital = False
                    continue
            
            if is_pandigital:
                print(f"Solution: {i} * {j} = {product}")
                solutions_set.add(product)

    return solutions_set


solutions = find_pandigital_products()

sum_of_solutions = sum(list(solutions))
print(f"sum of products is {sum_of_solutions}")

