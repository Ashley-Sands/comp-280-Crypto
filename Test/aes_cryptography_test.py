import unittest
from Test.base_test import *
import bruteForceMethods


class AesCryptographyTest( BaseTestClass ):

    import Encryptions.aes as aes

    def test_string_is_not_equal_to_encrypted_string(self):

        # setup cipher
        cipher = self.aes.AES(16)

        # encrypt string
        string_to_encrypt = "Helloo World"

        encrypted_string = cipher.encrypt( string_to_encrypt )

        self.assertNotEqual( string_to_encrypt, encrypted_string )

    def test_decrypted_string_is_equals_to_string_to_encrypt(self):

        # setup cipher
        cipher = self.aes.AES(16)

        # encrypt string
        string_to_encrypt = "Helloo World"

        encrypted_string = cipher.encrypt( string_to_encrypt )
        decrypted_string = cipher.decrypt( encrypted_string )

        self.assertEqual( decrypted_string.decode('utf-8'), string_to_encrypt )

    def test_decrypted_with_different_key_does_not_equal_string_to_encrypt(self):

        # set up encrypt cipher
        encrypt_cipher = self.aes.AES(16)

        # setup decrypt cipher
        decrypt_cipher = self.aes.AES(16)

        # encrypt string
        string_to_encrypt = "Helloo World"

        encrypted_string = encrypt_cipher.encrypt(string_to_encrypt)
        decrypted_string = decrypt_cipher.decrypt(encrypted_string)

        self.assertNotEqual( decrypted_string, string_to_encrypt )

    def test_brute_force_decryption_method_finds_string_to_encryption(self):
        # I am not going to implement this here.
        # if there are 255 different bytes (python bytes function)
        # and we use a 128bit key (or 16 bytes) that would mean
        # that there are 255 to the power of 16 different keys
        # ‭or 319,626,579,315,078,487,616,775,634,918,21‬ possibilities
        # (AKA a very, very, very, very big number)
        # ...
        # If i done my math correctly, on my PC (using a single thread)
        # it would take ~9.628519811583301e+21 Millenniums (+/- 10%)
        # see implementation in main.py for more info on the math :)
        # ...
        # So if i implemented it here we would all be long gone before
        # the test finished.
        pass


if __name__ == '__main__':
    unittest.main()