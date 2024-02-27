"""abraham martinez prime number generator """
import random

def is_prime(n, k=5):
    """Check if a number is prime using the Miller-Rabin primality test"""
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Write n as 2^r * d + 1
    d = n - 1
    r = 0
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    """Generate a random prime number with a given number of bits."""
    while True:
        candidate = random.getrandbits(bits)
        if candidate % 2 == 0:
            candidate += 1  # Ensure the number is odd
        if is_prime(candidate):
            return candidate

# Usage example:
bit_length = 2048  # Choose the desired number of bits for your prime
random_prime = generate_prime(bit_length)
print("Random Prime:", random_prime)
