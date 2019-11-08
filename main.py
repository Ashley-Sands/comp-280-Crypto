import time
import random

import Encryptions.ceasar as ceasar
import Encryptions.aes_cryptography as aes_cryptography
import Encryptions.aes_cryptodome as aes_cryptodome;
import Encryptions.xor as xor
from bruteForceMethods import BruteForce
import time_and_units as time_units;

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
encrypt_aes_cryptography = aes_cryptography.AES(16)
decrypt_aes_cryptography = aes_cryptography.AES(16)

encrypt_aes_cryptodome = aes_cryptodome.AES()
decrypt_aes_cryptodome = aes_cryptodome.AES()

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
        encrypted_string = encrypt_aes_cryptography.encrypt(inp_message)

        while inp_decrypt not in method_options:
            print("Your secrets message: ", encrypted_string)
            print("How would you like to decrypt the message")
            print("a) Decrypt using same cipher", "b) Decrypt using random key", sep="\n")
            print("c) Brute force")

            inp_decrypt = str( input() )

        if inp_decrypt == 'a':
            decrypted_string = encrypt_aes_cryptography.decrypt(encrypted_string)
        elif inp_decrypt == 'b':
            decrypt_caesar.set_key(random.randint(0, 500))
            decrypted_string = decrypt_aes_cryptography.decrypt(encrypted_string)
        elif inp_decrypt == 'c':
            try:
                decrypted_string = brute_force.AES(16, decrypt_aes_cryptography)
            except:
                print("Error: Unknown")

        print ("Your decrypted message: ", decrypted_string)

    elif inp_method.lower() == 'b':

        key = " "

        while key.isspace():
            print("Please enter a key of any length :) (any chr)")
            key = input()

        encrypt_xor.set_key(key)
        encrypted_str = encrypt_xor.enhanced_encrypt( inp_message )
        print("Your secrets message: ", encrypted_string)

        while inp_decrypt not in method_options:
            print("How would you like to decrypt the message")
            print("a) Decrypt using same cipher", "b) Decrypt using random key", sep="\n")
            print("c) Brute force (Do not select this if the key was longer than 2, it takes for ever)")

            inp_decrypt = str( input() ).lower()

        if inp_decrypt == 'a':
            decrypted_str = encrypt_xor.enhanced_encrypt(encrypted_str)
        elif inp_decrypt == 'b':
            decrypt_xor.random_key(len(key))
            decrypted_str = decrypt_xor.enhanced_encrypt(encrypted_str)
        elif inp_decrypt == 'c':
            if ( len(key) > 2 ):
                print( "Your key is longer than 2, this could take " )
                print( time_units.time_and_units( (1/65000) * (pow(255, len(key)) ) ) )
                print( "Are you sure you want to continue ? (Y to continue)" )
                cont = input()

                if cont == "Y":
                    decrypted_str = brute_force.enhanced_xor(decrypt_xor, encrypted_str, len(key), False, True)
                else:
                    decrypted_str = "Canceled"

        print ("Your decrypted message: ", decrypted_str)

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



#############
## AES CTR from Cryptodome lib
##########

print("AES CTR from Cryptodome lib demo")

e_cipher = aes_cryptodome.AES()
d_cipher = aes_cryptodome.AES()

str_to_encrypt = "Helloo World"

encrypted_str = e_cipher.encrypt( str_to_encrypt )
e_cipher.new_cipher()
decrypted_str = e_cipher.decrypt( encrypted_str )

decrypted_str_dif_cipher = d_cipher.decrypt( encrypted_str )

print( "String to Encrypt: ", str_to_encrypt )

print( "Encrypted string: ", encrypted_str )
print( "Decrypted string: ", decrypted_str )

print( "Dead string: ", decrypted_str_dif_cipher )
