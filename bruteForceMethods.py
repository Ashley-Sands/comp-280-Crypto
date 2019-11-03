
class BruteForce:

    def caesar(self, encrypted_string, max_offset):

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
