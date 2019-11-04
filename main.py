import time
import random

import ceasar
import aes
import xor
from bruteForceMethods import BruteForce

str_to_encrypt = "Helloo World"
encrypted_str = ""

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

