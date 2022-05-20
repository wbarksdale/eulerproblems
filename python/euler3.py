# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def is_prime(n):
    for i in range(2, int((n + 2)/2)):
        # print(f"checking {n} / {i}")
        if n % i == 0:
            return False
    return True

def compute_prime_factors(n: int) -> list[int]:
    factors = [n]
    prime_factors = []

    while len(factors) > 0:
        print(f"Factors: {factors}")
        print(f"Prime Factors: {prime_factors}")
        factor = factors.pop()
        if is_prime(factor):
            prime_factors += [factor]
        else:
            for i in range(2, int(factor/2)):
                if factor % i == 0:
                    factors += [i, int(factor/i)]
                    break

    return prime_factors


print(f"is 2 prime? {is_prime(2)}")
print(f"is 3 prime? {is_prime(3)}")
print(f"is 4 prime? {is_prime(4)}")
print(f"is 20 prime? {is_prime(20)}")
print(f"is 23 prime? {is_prime(23)}")

number = 600851475143
primes = compute_prime_factors(number)
largest_prime = max(primes)
print(f"The prime factors of {number} are {primes}")
print(f"The largest prime factor of {number} is {largest_prime}")