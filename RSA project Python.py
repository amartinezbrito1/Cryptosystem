"""RSA project """
import random



def generate_prime(bits):
    """Generate a random prime number with a given number of bits."""
    while True:
        candidate = random.getrandbits(bits)
        if candidate % 2 == 0:
            candidate += 1  # Ensure the number is odd
        if Fermat(candidate):
            return candidate

# Usage example:
bit_length = 24# Choose the desired number of bits for your prime


def generate_phi(p,q):
    phi = (p-1)*(q-1)
    return phi
def generate_n(p,q):
    n = p*q
    return n
def generate_e(phi):
    #pulled from lecture notes
   e = random.randint(2, phi)
   while gcd (e, phi) != 1:
       e = random.randint(2, phi)
   return e
#Pulled from blackboard
def gcd(a, b):
    ''' The gcd function implements Euclid's
    GCD algorithm to find the greatest common
    divisor of two positive integers a and b'''
    
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
#Pulled from Blackboard
def Fermat(p):
    '''Test if p is prime with Fermat\'s little theorem\n'''
    t = True
    for i in range(1, p):
        if pow(i, p-1, p) != 1:
            t = False
            break
    if not t:
        return False
    else:
        return True
p = generate_prime(bit_length)
q = generate_prime(bit_length)
phi = generate_phi(p, q)
e = generate_e(phi)
print("p: " , p)
print("q: " , q)
print("phi: " , phi)
print("e: " , e)
