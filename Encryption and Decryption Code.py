# Import necessary libraries
import random
import math

# Setup

# Implement extended gcd function
def extendedGCD(a=1, b=1):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extendedGCD(b, a % b)
    return y, x - a // b * y, d

# Generate reasonably large and random prime p and q
def generate_prime():
    p_is_not_prime = True
    square_rt = 0
    p = random.randint(100000, 1000000)

    while p_is_not_prime:
        square_rt = math.ceil(math.sqrt(p))
        for i in range(2, square_rt):
            if p % i == 0:
                p_is_not_prime = True
                break
            else:
                p_is_not_prime = False

        if p_is_not_prime:
            p = random.randint(100000, 1000000)

    return p

# Generate p and q
p = generate_prime()
q = generate_prime()

n = p * q
Fi = (p - 1) * (q - 1)


print('p = ', p)
print('q = ', q)


#generate public key e
e = random.randint(2, Fi)
while math.gcd(e, Fi) != 1:
    e = random.randint(2, Fi)

print('Your public key is: ', e)

#generate private key d
x = extendedGCD(e, Fi)
d = x[0] % Fi

print('private key is: ',d )

"""another approach"""
#encoding the message as ASCII values
message = input('Type your message: ')
message_encoded = [ord(char) for char in message]

#encryption
ciphertext = [pow(char, e, n) for char in message_encoded]

print('This is your ciphertext:', ciphertext)

#decryption
decrypted_message_encoded = [pow(char, d, n) for char in ciphertext]
decrypted_message = ''.join(chr(char) for char in decrypted_message_encoded)

print('Decrypted message:', decrypted_message)


print('The original message is: ', message)
print('The cyphered message is: ', ciphertext)
print('The decyphered message is: ', decrypted_message)



"""signature verification"""
"""to be signed by owner of the keys only """
signature_request = False

if signature_request == True
    """list of messages"""
    signatures_received = []
    messages = input('Enter a message: ')
    
    if messages not in signatures_received:
            signatures_received.append(messages)
        else:
            #find the next available index to store the message
            index = 0
            while f"{messages}_{index}" in signatures_received:
                index += 1
            signatures_received.append(f"{messages}_{index}")
print("Stored unique messages:")
for messages, message_index in signatures_received.items():
    print(f"Message {message_index}: {message}")
            
def sign_data(signature_received, private_key):
    n, d = private_key
    S = pow(name, d, n)
    return S

"""the public user is the only one who can authenticate a signature"""
#Verifying the Signature
def verify_signature(signature, name, public_key):
    n, e = public_key
    M = pow(signature, e, n)
    return M == name

#User inputs a message (Name)
name = int(input('Enter the message (an integer): '))

#Sign the Data
signature = sign_data(name, (n, d))

# Output the signature
print('Signature:', signature)

#Verify the Signature
is_verified = verify_signature(signature, name, (n, e))

if is_verified:
    print('Signature is valid. Message is authenticated.')
else:
    print('Signature is not valid. Message could not be authenticated.')
