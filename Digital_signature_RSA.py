"""digital signature and menu"""
import random
import math
import random
import math

#Pulled from Blackboard
def fermat(n1 = 1000000, n2 = 100000000, k = 1000):
    p = random.randint(n1, n2)
    pseudo_prime = False
    while not pseudo_prime:
        for i in range(k):
            j = random.randint(2, p)
            if pow(j, p-1, p) > 1:
                p = random.randint(n1, n2)
                break
        pseudo_prime = True

    return p

##def Fermat(p):
##    '''Test if p is prime with Fermat\'s little theorem\n'''
##    t = True
##    for i in range(1, p):
##        if pow(i, p-1, p) != 1:
##            t = False
##            break
##    if not t:
##        return False
##    else:
##        return True

def testPrime_brute_force(p = 10):
    if (p == 2):
        return True
    else:
        for b in range(2, math.floor(math.sqrt(p))):
            if math.gcd(p, b) > 1:
                return False
            else:
                continue
        return True
    
def generate_prime():
    while(True):
        pseudo_prime = fermat()
        if(testPrime_brute_force(pseudo_prime)):
            break

    return pseudo_prime

    
##def generate_prime(bits):
##    """Generate a random prime number with a given number of bits."""
##    while True:
##        candidate = random.getrandbits(bits)
##        if candidate % 2 == 0:
##            candidate += 1  # Ensure the number is odd
##        if Fermat(candidate):
##            return candidate

# Usage example:
#bit_length = 24# Choose the desired number of bits for your prime

def generate_phi(p,q):
    phi = (p-1)*(q-1)
    return phi

def generate_n(p,q):
    n = p*q
    return n

#Pulled from blackboard
def gcd(a, b):
    ''' The gcd function implements Euclid's
    GCD algorithm to find the greatest common
    divisor of two positive integers a and b'''
    
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
def generate_e(phi):
    #pulled from lecture notes
   e = random.randint(2, phi)
   while gcd (e, phi) != 1:
       e = random.randint(2, phi)
   return e

#computes the extended gcd of two numbers. Pulled from Dr. Chenyi Hu's lecture notes
def extendedGCD(a=1, b=1):
    if (b==0):
        return (1,0,a)
    (x,y,d) = extendedGCD(b,a%b)
    
    return y, x-a//b*y, d

#generate private key d which is the relative inverse of e. Pulled from Dr. Chenyi Hu's lecture notes
def generate_private_key(e,phi):
    x = extendedGCD(e,phi)
    d = x[0] % phi

    return d

#encrypts a given message using the public key (e,n)
def encrypt_message(message, e, n):
    message = message.upper()
    cyphered_message = []
    for x in message:
        #encrypt the specific character using the public key and fast modular exponentiation (pow method).
        #pulled from Dr. Chenyi Hu's lecture notes
        x = pow(ord(x),e,n) 
            
        cyphered_message.append(x)

    return cyphered_message


#decyphers an encrypted data using the private key d, and one component of the public key n
def decrypt_message(cyphered_data, d, n):
    decyphered_message = ''
    var = 0

    for x in (cyphered_data):
        #decrypt the specific character using the private key and fast modular exponentiation (pow method).
        #pulled from Dr. Chenyi Hu's lecture notes
        var = pow(x,d,n)
        
        if(var == 32):
            decyphered_message += chr(var)
        else:
            var = (var-65)%26
            decyphered_message += chr(var+65)

    return decyphered_messagep
#= generate_prime(bit_length)
#q = generate_prime(bit_length)
#phi = generate_phi(p, q)
#e = generate_e(phi)
#n = generate_n(p,q)
print("p: " , p)
print("q: " , q)
print("phi: " , phi)
print("e: " , e)
print("n:", n)

###########################################################
#dictionary to store encrypted messages
encrypted_messages = {}
message_counter = 1

signatures_received = {}
"""just so you know, S is the received signature"""
def sign_message(message, d, n):
    #implementing fast modular exponentiation to compute S
    """ascii convertion """
    message_int = int.from_bytes(message.encode(), byteorder='big')
    hashed_message = pow(message_int, d, n)
    #S = pow(message_int, d, n)
    #print("this is s: ",S)
    return hashed_message
def authenticate_signature(S, e, n, received_message_hash):
    calculated_hash = pow(S, e, n)
    received_message_hash_int = int.from_bytes(received_message_hash.encode(), byteorder='big')

    if calculated_hash == received_message_hash_int:
        return True
    else:
        return False


#    message_int = int.from_bytes(message.encode(), byteorder='big')
 #   hashed_message = pow(message_int, e, n)
  #  print("Received S:", S)
#    print("Calculated Hash:", hashed_message)
#    if S == hashed_message:
#        return True
#    else:
#        return False
    """message_int = int.from_bytes(message.encode(), byteorder='big')
    hashed_message = pow(message_int, e, n)"""
#    print("hash:",hashed_message)
#    print("s:",S)
    """if S == hashed_message:
        return True
    else:
        return False"""


#main menu
print("RSA keys have been generated.")
while True:
    
    print("Please select your user type:")
    print("1. A public user")
    print("2. The owner of the keys")
    print("3. Exit program")

    user_type_choice = input("Enter your choice: ")

    if user_type_choice == "1":
        #public user menu
        while True:
            print("As a public user, what would you like to do?")
            print("1. Send an encrypted message")
            print("2. Authenticate a digital signature")
            print("3. Exit")

            public_user_choice = input("Enter your choice: ")

            if public_user_choice == "1":
                #call the function to send an encrypted message 
                message = input("Enter a message: ")
                #call the function to send the message
                encrypted_message = encrypt_message(message, e, n)
                encrypted_messages[message_counter] = encrypted_message
                message_counter += 1
                
                print("Message encrypted and sent.")

            elif public_user_choice == "2":
                
                if signatures_received:
                    #display available signatures
                    print("The following messages are available:")
                    for index, message in enumerate(signatures_received.keys(), start=1):
                        print(f"{index}. {message}")
                    
                    #ask the user to select a signature to authenticate
                    selected_index = int(input("Enter your choice: ")) - 1
                    selected_message = list(signatures_received.keys())[selected_index]
                    
                    #get signature S 
                    S = signatures_received[selected_message]  
                    is_signature_valid = authenticate_signature(S, e, n, selected_message)

                    if is_signature_valid:
                        print("Signature is valid.")
                    else:
                        print("Signature is not valid.")  
                        signature_choice = input("Enter your choice: ")

                else:
                    print("There are no signatures to authenticate.")    
                
                

            elif public_user_choice == "3":
                break  

    elif user_type_choice == "2":
        #owner of the keys menu
        while True:
            print("As the owner of the keys, what would you like to do?")
            print("1. Decrypt a received message")
            print("2. Digitally sign a message")
            print("3. Show the keys")
            print("4. Generating a new set of keys")
            print("5. Exit")

            owner_choice = input("Enter your choice: ")

            if owner_choice == "1":
                
                if not encrypted_messages:
                    print("No messages to decrypt yet")
                else:
                    """this will display available messages with their unique identifiers"""
                    print("The following messages are available:")
                    for message_id, _ in encrypted_messages.items():
                        print(f"{message_id}. (length = {len(encrypted_messages[message_id])})")

                    #ask the owner to select a message for decryption
                    selected_message_id = int(input("Enter your choice: "))

                    #check if the selected message_id exists in the dictionary
                    if selected_message_id in encrypted_messages:
                        selected_encrypted_message = encrypted_messages[selected_message_id]
                        decrypted_message = decrypt_message(selected_encrypted_message, d, n)
                        print("Decrypted message:", decrypted_message)
                    else:
                        print("Invalid message selection.")


            elif owner_choice == "2":
                #call the function to digitally sign a message 
                message = input('Enter a message: ')
                #S = sign_message(message, d, n)  
                S = (message ^ d) % n

                """this will store the signatur as an integer"""
                signatures_received[message] = S
                message_counter += 1
                
                print("Message signed and sent.")
    
                
                                

            elif owner_choice == "3":
                #call the function to show the keys 
                #display key information
                print("Key information:")
                #call the function to display key information 

            elif owner_choice == "4":
                #call the function to generate a new set of keys 
                print("now in option 4")
            elif owner_choice == "5":
                break  

    elif user_type_choice == "3":
        print("Bye for now!")
        break  # this will exit you from the whole program and menu

    else:
        print("Invalid choice. Please enter a valid option!!")

 
