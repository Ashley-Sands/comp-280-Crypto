import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class AES:

    def __init__(self):
        self.encryption_key = get_random_bytes(16)
        self.cipher = AES.new(self.encryption_key, AES.MODE_CTR)

    def new_cipher(self, key):
        self.cipher = AES.new(key, AES.MODE_CTR)

    def encrypt(self, str_to_encrypt):
        """ Encrypt using AES CTR

        :param str_to_encrypt:  plain text string to be encrypted
        :return:                encrypted str
        """

        encrypted_bytes = self.cipher.encrypt( str_to_encrypt )

        return base64.b64encode( encrypted_bytes )

    def decrypt(self, str_to_decrypt):
        """ Encrypt using AES CTR

        :param str_to_decrypt:  plain text string to be encrypted
        :return:                encrypted str
        """

        decoded_str = base64.b64decode( str_to_decrypt )

        return self.cipher.decrypt( decoded_str )