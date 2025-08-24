def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Example tests
print(is_prime(2))    # True
print(is_prime(11))   # True
print(is_prime(15))   # False
print(is_prime(1))    # False
print(is_prime(0))    # False