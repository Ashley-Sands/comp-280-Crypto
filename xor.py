import random

class XorChipher:

    def __init__(self, chr_key):
        self.key = chr_key
        self.key_len = len(chr_key)

    def random_key(self, key_len = 1):
        self.key = [ chr(random.randint(0, 255)) for i in range(key_len) ]
        self.key_len = key_len

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

        return str_to_encrypt

    def decrypt(self, str_to_decrypt):
        """More Complex Xor cipher decryption
        This method will work with key of any length.
        It turns out this is unnecessary, i assumed that if the encryption key
        was 'ABC' to decrypt it you would have to do the key in reverse ('CBA'),
        but that is not the case. The string can be decrypted as long key
        consists of all the characters of the original key (no extra or less)
        (eg. if the original key was 'ABC' it can be decrypted using keys
        'BAC', 'ACB', 'BCA', 'CBA' and so on)

        So this function is redundant.

        :param str_to_decrypt: string to be decrypted
        :return: decrypted string
        """

        str_len = len(str_to_decrypt)

        for k in range(self.key_len-1, -1, -1):
            for i in range(str_len):
                str_to_decrypt = (str_to_decrypt[:i] +
                                  chr(ord(str_to_decrypt[i]) ^ ord(self.key[k])) +
                                  str_to_decrypt[i + 1:])

        return str_to_decrypt

    def enhanced_encrypt(self, str_to_encrypt):
        """ enhanced Xor Cipher that works with a key of any length
        It also enforces the order of the key

        By enforcing the order of the key we dramatically increase the amount
        of possible keys.

        Possible key comparison
        Based on the key using utf-8 characters that gives us 255 characters
        ---------------------------------------------------------------------
        Using a key with len 1 (8 bit):
        Xor.Cipher function (simple Xor) only has             255 possible keys
        since its only a single character key

        Using a key with len 8 (64 bit):
        Xor.encrypt function has                              2040 possible keys (255 * 8)
        since the key order is not enforced.

        Xor.enhanced_encrypt has                              255^8 possible keys
        since the key order is enforce

        :param str_to_encrypt: string to encrypt
        :return: encrypted / decryped string
        """

        str_len = len(str_to_encrypt)

        for i in range(str_len):
            k = i % len(self.key)
            str_to_encrypt = (str_to_encrypt[:i] +
                              chr(ord(str_to_encrypt[i]) ^ ord(self.key[k])) +
                              str_to_encrypt[i + 1:])

        return str_to_encrypt

