import random

class XorChipher:

    def __init__(self, chr_key):
        self.key = chr_key

    def random_key(self):
        self.key = chr(random.randint(1, 255))

    def chipher(self, string):

        str_len = len (string)

        for i in range( str_len ):
            string = ( string[:i] + chr(ord(string[i]) ^ ord(self.key) ) + string[i+1:])

        return string
