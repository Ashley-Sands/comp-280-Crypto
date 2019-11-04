
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
