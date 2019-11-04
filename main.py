import time
import ceasar
import aes
import random
import xor


str_to_encrypt = "Helloo World"
encrypted_str = ""

def brute_force_caesar( string_to_crack, max_attamps ):

    temp_str = ""
    cracked_strs = []    # of tuples (key, str)

    for k in range(max_attamps):    # keys / offsets
        for s in string_to_crack:
            ascii_code = ord(s) + k
            if ascii_code > max_attamps - 1:
                ascii_code -= max_attamps
            temp_str += str(chr(ascii_code))
        cracked_strs.append((k, temp_str))
        temp_str = ""

    return cracked_strs


def brute_force_aes( key_len, chiper ):

    str_length = 16;#key_len
    max_chr = 255
    min_chr = 1

    e_str = [ chr(max_chr) ] * str_length
    end_str = [ chr(min_chr) ] * str_length

    last_chr = max_chr
    current_col = len(e_str) - 1

    possibilities = pow(max_chr - min_chr + 1, str_length)
    aprox_time = time_and_units( ( possibilities / 1000000 ) * 0.95 )   # if print 8.9

    print( "To be honest i cant be asked to brute force this, it will take to long for my pc" )
    print( "for my pc since it", (max_chr - min_chr + 1),"^", str_length,"or", possibilities, "possible keys" )
    print("..., Ok so i did anyway :)")
    print( "Aprox time:", aprox_time[0], aprox_time[1], "(On my pc its roughly 0.9 secs for 1,000,000)")
    print("Are you sure you want to continue, it might take a while. \nY to continue \nAnythink else to exit.")
    contin = input()
    warning = input("Would like a lil update ever 1,000,000 elements? (Y for yes)") == "Y"

    if contin != 'Y' :
        return

    c = 0
    cc = 1

    flip_flop_offset = 2

    w_time = time.time()    # warning
    s_time = time.time()    # start

    while current_col > -1:
        c += 1
        e_str[current_col] = chr(last_chr)
        last_chr -= 1

        a = ''.join(e_str);
        print( a.encode('utf-8') )
        chiper.new_cipher( a.encode('utf-8') )

        if e_str == end_str:
            break;

        if last_chr < min_chr:
            # flip flop are way thought the list
            while flip_flop_offset < str_length + 1:
                # go to the next chr
                e_str[len(e_str) - flip_flop_offset] = chr( ord( e_str[len(e_str) - flip_flop_offset] ) - 1 )

                # if it is less than are min chr put to max chr
                # and go to the next element in the list.
                if ord( e_str[len(e_str) - flip_flop_offset] ) < min_chr:
                    e_str[len(e_str) - flip_flop_offset] = chr(max_chr)
                    flip_flop_offset += 1
                else:   # done flip flopping when no chr are below min chr
                    break

            # reset last chr and flip flop offset
            last_chr = max_chr
            flip_flop_offset = 2

        if warning and c >= 1000000 * cc:
            print( "so thats, ", (1000000 * cc), "Done." )
            print( "the last 100,000 tock ", (time.time() - w_time), "seconds" )
            contin = input("Are You Board Yet? (Y to exit, any think else to continue)")
            if contin == "Y":
                return
            cc += 1
            w_time = time.time()

    t_time = time_and_units(time.time() - s_time)

    print("All Done, total time:", t_time[0], t_time[1])
    print("count", c)


def time_and_units( t_time):

    t_time_units = "Secs"

    if t_time > 60:
        t_time /= 60
        t_time_units = "Mins"
    
    if t_time > 60:
        t_time /= 60
        t_time_units = "Hours"

    if t_time > 24:
        t_time /= 24
        t_time_units = "Days"

    if t_time > 7:
        t_time /= 7
        t_time_units = "Weeks"

    if t_time > 52.1429:
        t_time /= 52.1429
        t_time_units = "Years"

    if t_time > 10:
        t_time /= 10
        t_time_units = "Decades"

    if t_time > 10:
        t_time /= 10
        t_time_units = "Centurys"

    if t_time > 10:
        t_time /= 10
        t_time_units = "Millenniums"

    return (t_time, t_time_units)


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

for bf in brute_force_caesar( encrypted_str, caesar_encription.max_offset ):
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
brute_force_aes(16, aes_encription)

byte = bytearray()

