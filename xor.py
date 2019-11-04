import random

class XorChipher:

    def __init__(self, chr_key):
        self.key = chr_key
        self.key_len = len(chr_key)

    def random_key(self, key_len = 1):
        self.key = [ chr(random.randint(0, 255)) for i in range(key_len) ]
        self.key_len = key_len

    def encrypt(self, str_to_encrypt):
        """ More Complex Xor cipher encryption
        This method will work with key of any length.

        :param str_to_encrypt: string to be encrypted
        :return: encrypted string
        """

        str_len = len(str_to_encrypt)

        for k in range(self.key_len):
            for i in range(str_len):
                str_to_encrypt = (str_to_encrypt[:i] +
                                  chr( ord( str_to_encrypt[i] ) ^ ord( self.key[k] ) ) +
                                  str_to_encrypt[i + 1:])

    def decrypt(self, str_to_decrypt):
        """More Complex Xor cipher decryption
        This method will work with key of any length.

        :param str_to_decrypt: string to be decrypted
        :return: decrypted string
        """

        str_len = len(str_to_decrypt)

        for k in range(self.key_len, 0, -1):
            for i in range(str_len):
                str_to_decrypt = (str_to_decrypt[:i] +
                                  chr(ord(str_to_decrypt[i]) ^ ord(self.key[k])) +
                                  str_to_decrypt[i + 1:])

    def chipher(self, string):
        """ Simple Xor Cipher.
        This method will only use the a key of len 1
        and works both ways (encrypt and decrypt)

        :param string: string to encrypt/decrypt
        :return: encrypted / decrypted string
        """
        str_len = len (string)

        for i in range( str_len ):
            string = ( string[:i] + chr(ord(string[i]) ^ ord(self.key[0]) ) + string[i+1:])

        return string
