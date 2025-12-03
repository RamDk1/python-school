def get_primes_factors(n):
    factors = []
    divisor = 2

    while n >=2:
        if n % divisor == 0:
            factors.append(divisor)
            n = n//divisor
        else:
            divisor+=1
    return factors

print(get_primes_factors(315))  # [3, 3, 5, 7]