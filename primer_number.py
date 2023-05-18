def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime_number(n):
    count = 0
    number = 2
    while count < n:
        if is_prime(number):
            count += 1
        number += 1
    return number - 1
