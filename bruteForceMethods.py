import time
from time_and_units import *


class BruteForce:

    def caesar(self, encrypted_string, max_offset):
        """ Brute force method to crack the super simple caesar encryption
        This method is supper quick to crack to since the char offset only
        goes up 255.
        (Anything after that get raped back around to 0)

        :param encrypted_string:        String to attempt to decrypt.
        :param max_offset:              The max char offset
        :return:                        All keys and strings
        """

        temp_str = ""
        cracked_strings = []  # list of tuples (key, str)

        # go through all keys up to max offset.
        # in caesar the key is just the a character offset
        for k in range(max_offset):
            # go through each char in encrypted string and shift it by 'k'
            for s in encrypted_string:
                ascii_code = ord(s) + k
                if ascii_code > max_offset - 1:  # warp around to ~0 if we have gone over the max offset
                    ascii_code -= max_offset
                temp_str += str(chr(ascii_code))
            cracked_strings.append((max_offset - k, temp_str))
            temp_str = ""

        return cracked_strings  # return all possible original strings

    def xor(self, encrypted_string, max_key):
        """ Brute force method to crack simple Xor (key with len 1)
        This method is supper quick to crack, since there can only be 255 keys.

        :param encrypted_string:    String to attempt to decrypt.
        :param max_key:             Max key (or char numb) (255, utf-8)
        :return:                    All keys and strings
        """
        string_length = len( encrypted_string )
        temp_string = "";
        key = ""
        
        cracked_strings = [] # list of tuples( key, decrypted string )
        
        for k in range(1, max_key, 1):
            key = chr(k)
            temp_string = encrypted_string;
            for c in range(string_length):
                temp_string = (temp_string[:c] + chr( ord( temp_string[c] ) ^ ord( key ) ) + temp_string[c+1:] )
                cracked_strings.append( (key, temp_string) )

        return cracked_strings

    def AES( self, key_len, chiper ):
        """

        :param key_len:
        :param chiper:
        :return:
        """

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

        c = 0       # counter
        cc = 1      # col counter

        flip_flop_offset = 2

        w_time = time.time()    # warning
        s_time = time.time()    # start

        while current_col > -1:
            c += 1
            e_str[current_col] = chr(last_chr)
            last_chr -= 1

            a = ''.join(e_str)
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

            # incase you get board and want to exit.
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