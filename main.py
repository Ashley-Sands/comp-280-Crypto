import time
import random

import Encryptions.ceasar as ceasar
import Encryptions.aes as aes
import Encryptions.xor as xor
from bruteForceMethods import BruteForce

import flipFlop


# set up ciphers for encryption and decryption
# decrypts are only use when using a different key
# Caesar
encrypt_caesar = ceasar.Caesar()
encrypt_caesar.set_max_offset(255)
decrypt_caesar = ceasar.Caesar()
decrypt_caesar.set_max_offset(255)
# Xor
encrypt_xor = xor.XorChipher("A")
decrypt_xor = xor.XorChipher("B")
# Aes
encrypt_aes = aes.AES(16)
decrypt_aes = aes.AES(16)

brute_force = BruteForce();

method_options = ['a', 'b', 'c']

print("Hi, Welcome to AMS Encrypt...")
print("Type quit, to exit the application")

while True:

    inp_method = ""
    inp_message = ""
    inp_decrypt = ""

    encrypted_string = ""
    decrypted_string = ""

    while inp_method not in method_options:
        print( "Enter an encryption method you would like to test")
        print( "a) Aes", "b) Xor", "c) Caesar", sep="\n")
        inp_method = str( input() )

    while len(inp_message) == 0:
        print( "Thank you!", "Please enter the message you would like to encrypt", sep="\n")
        inp_message = str( input() )

    if inp_message.lower() == "quit" or inp_method.lower() == "quit":
        break

    if inp_method.lower() == 'a':
        encrypted_string = encrypt_aes.encrypt(inp_message)

        while inp_decrypt not in method_options:
            print("Your secrets message: ", encrypted_string)
            print("How would you like to decrypt the message")
            print("a) Decrypt using same cipher", "b) Decrypt using random key", sep="\n")
            print("c) Brute force")

            inp_decrypt = str( input() )

        if inp_decrypt == 'a':
            decrypted_string = encrypt_aes.decrypt(encrypted_string)
        elif inp_decrypt == 'b':
            decrypt_caesar.set_key(random.randint(0, 500))
            decrypted_string = decrypt_aes.decrypt(encrypted_string)
        elif inp_decrypt == 'c':
            try:
                decrypted_string = brute_force.AES(16, decrypt_aes)
            except:
                print("Error: Unknown")

        print ("Your decrypted message: ", decrypted_string)

    elif inp_method.lower() == 'b':
        pass
    elif inp_method.lower() == 'c':
        print("Please enter a key offset (must be int)")
        key_offset = 1

        while key_offset < 2:
            try:
                key_offset = int( input() )
            except ValueError:
                key_offset = 1
                print("Try Again")

        encrypt_caesar.set_key(key_offset)
        encrypted_string = encrypt_caesar.encrypt(inp_message)

        while inp_decrypt not in method_options:
            print("Your secrets message: ", encrypted_string)
            print("How would you like to decrypt the message")
            print("a) Decrypt using same cipher", "b) Decrypt using random key", sep="\n")
            print("c) Brute force")

            inp_decrypt = str( input() )

        if inp_decrypt == 'a':
            decrypted_string = encrypt_caesar.decrypt(encrypted_string)
        elif inp_decrypt == 'b':
            decrypt_caesar.set_key(random.randint(0, 500))
            decrypted_string = decrypt_caesar.decrypt(encrypted_string)
        elif inp_decrypt == 'c':
            decrypted_string = brute_force.caesar(encrypted_string, 255)

        print ("Your decrypted message: ", decrypted_string)



###################################################################
# caesar
###################################################################
caesar_encription = ceasar.Caesar()

caesar_encription.set_max_offset( 200 )
caesar_encription.set_key(random.randrange(0, 400)) #1234)

encrypted_str = caesar_encription.encrypt( str_to_encrypt )
decrypted_str = caesar_encription.decrypt( encrypted_str )

print(encrypted_str)
print(decrypted_str)

# crack the encrypted using brute force

start_time = time.time()

brute_force = BruteForce()

for bf in brute_force.caesar( encrypted_str, caesar_encription.max_offset ):
    print( bf )
    if bf[1] == decrypted_str:  ## point out that we have found it.
        print("---------------------------------------------------------------------------------------------------")
        print("Cracked!")
        break

end_time = time.time()

print( "\n\n Total time:", (end_time-start_time), "seconds to try all posabilities" )

input("Hit enter to continue onto Xor...")


###################################################################
# Xor
###################################################################

xor_encryption = xor.XorChipher('A')
string_to_encrypt = "Helloo World"

encrypted_str = xor_encryption.chipher(string_to_encrypt)
decrypted_str = xor_encryption.chipher(encrypted_str)

xor_key = 'Adj\r\n8@4gD'
xor_better_key_encryption = xor.XorChipher(xor_key)
xor_better_key_decryption = xor.XorChipher('Fd83ks\n\t4')

encrypted_better_key_str = xor_better_key_encryption.encrypt(string_to_encrypt)
decrypted_better_key_str = xor_better_key_encryption.decrypt(encrypted_better_key_str)

bad_decrypted_better_key_str = xor_better_key_decryption.decrypt(encrypted_better_key_str)

print("------------------ XOR ------------------")
print("-- Key Len 1")
print("encrypted_str: ", encrypted_str)
print("decrypted_str: ", decrypted_str)

print("-- Key Len", len(xor_key))
print("encrypted_str: ", encrypted_better_key_str)
print("decrypted_str: ", decrypted_better_key_str)
print("dead decrypted_str: ", bad_decrypted_better_key_str)

print("New Key...")
xor_encryption.random_key()
decrypted_str = xor_encryption.chipher(encrypted_str)
print("Dead str", decrypted_str)

input("Hit enter to continue onto AES...")

###################################################################
# aes
###################################################################

print( "\n\n\nAES Keys: " );

aes_encription = aes.AES(16)
aes_encription.print_keys()
e_data = aes_encription.encrypt("Helloo World")
d_data = aes_encription.decrypt( e_data )

print("======================================", d_data, d_data.decode("utf-8"))

print( e_data, "\n", d_data.decode("utf-8") )

print("-----------------")
brute_force.AES(16, aes_encription)

byte = bytearray()

