# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

coin_values = [1, 2, 5, 10, 20, 50, 100, 200]

def find_all_solutions(coin_vec = [0] * 8, already_tried = set(), value = 200) -> list[int]:
    # Recurse through solutions, but keep a record of what we have tried to prevent
    # doing extra work. i.e. if we add a 1 coin and a 2 coin, that is the same as 
    # adding a 2 coin then a 1 coin
    solutions = []
    for i in range(0, len(coin_values)):
        new_coin_vec = coin_vec.copy()
        new_coin_vec[i] += 1
        
        # If we have already tried new_coin_vec we can short circuit here
        # to prevent duplicating work, otherwise, we check the solution and
        # continue adding coins if needed
        hashable_vec = "_".join([str(int) for int in new_coin_vec])
        if hashable_vec in already_tried:
            continue
        else:
            already_tried.add(hashable_vec)
        
        new_value = value - coin_values[i]
        if new_value < 0:
            continue
        elif new_value == 0:
            print(f"Found Solutions: {new_coin_vec}")
            solutions.append(new_coin_vec)
            continue
        else:
            # new value > 0
            # print(f"recursing: {new_coin_vec} new_value {new_value}")
            solutions += find_all_solutions(new_coin_vec, already_tried, new_value)

    return solutions


solutions = find_all_solutions(value=200)
print(f"Found {len(solutions)} solutions")