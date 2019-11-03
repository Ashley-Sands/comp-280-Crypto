class Caesar:

    def __init__(self):
        self.offset = 1;
        self.max_offset = 128

    def set_key(self, key):
        if isinstance(key, int):
            self.offset = key
        else:
            self.offset = ord(key)

        if self.offset > self.max_offset - 1:
            self.offset -= int(self.offset/self.max_offset) * self.max_offset

    def set_max_offset(self, max_offset):
        if max_offset < 1:
            max_offset = 128
            print("Error: unable to set maxOffset below 1. has been set to 128")
        self.max_offset = max_offset
        self.set_key(self.offset)       # we must reset the key to make sure it is set up correctly

    def encrypt(self, string):

        final_string = ""

        for s in string:
            ascii_code = ord( s )
            ascii_code = ascii_code + self.offset
            if ascii_code > self.max_offset - 1:    # prevent going out side of ascii values (not full proof tho).
                ascii_code -= self.max_offset # - 1
            final_string = final_string + str( chr( ascii_code ) )

        return final_string

    def decrypt(self, string):

        final_string = ""

        for s in string:
            ascii_code = ord(s)
            ascii_code = ascii_code - self.offset
            if ascii_code < 0:      # prevent going out side of ascii values (not full proof tho).
                ascii_code += self.max_offset # - 1
            final_string = final_string + str(chr(ascii_code))

        return final_string

