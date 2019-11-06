import unittest
from Test.base_test import *
import bruteForceMethods


class XorTest( BaseTestClass ):

    import Encryptions.xor as xor

# =========== Simple Xor witch only supports a single character key.

    def test_string_to_encrypt_is_not_equal_to_encrypted_string(self):

        # setup cipher
        cipher_key = "A"
        cipher = self.xor.XorChipher( cipher_key )

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = cipher.chipher( string_to_encrypt )

        self.assertNotEqual( string_to_encrypt, encrypted_string )

    def test_decrypted_string_is_equals_to_string_to_encrypt(self):

        # setup cipher
        cipher_key = "A"
        cipher = self.xor.XorChipher(cipher_key)

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = cipher.chipher(string_to_encrypt)
        decrypted_string = cipher.chipher(encrypted_string)

        self.assertEqual(string_to_encrypt, decrypted_string)

    def test_decrypted_with_different_key_does_not_match_string_to_encrypt(self):

        # setup encryption cipher
        encrypt_cipher_key = "A"
        encrypt_cipher = self.xor.XorChipher(encrypt_cipher_key)

        # setup decryption cipher
        decrypt_cipher_key = "B"
        decrypt_cipher = self.xor.XorChipher(decrypt_cipher_key)

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = encrypt_cipher.chipher(string_to_encrypt)
        decrypted_string = decrypt_cipher.chipher(encrypted_string)

        self.assertNotEqual(string_to_encrypt, decrypted_string)

    def test_brute_force_decryption_method_finds_string_to_encryption(self):

        # setup cipher
        cipher_key = "A"
        cipher = self.xor.XorChipher(cipher_key)

        # setup brute force method
        brute_force = bruteForceMethods.BruteForce();
        brute_force_max_key = 1024

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = cipher.chipher(string_to_encrypt)

        possible_strings = brute_force.xor( encrypted_string, brute_force_max_key )
        self.assertTrue( (cipher_key, string_to_encrypt) in possible_strings )

# =========== Xor support for keys with length grater than 1

    def test_string_to_encrypt_is_not_equal_to_encrypted_string_using_64_bit_key(self):

        # setup cipher
        cipher_key = 'D8\r3#\t\n:'
        cipher = self.xor.XorChipher( cipher_key )

        # encrypt key
        string_to_encrypt = "Helloo World"
        encrypted_string = cipher.encrypt( string_to_encrypt )

        self.assertNotEqual( string_to_encrypt, encrypted_string )

    def test_decrypted_string_is_equals_to_string_to_encrypt_using_64_bit_key(self):

        # setup cipher
        cipher_key = 'D8\r3#\t\n:'
        cipher = self.xor.XorChipher(cipher_key)

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = cipher.encrypt(string_to_encrypt)
        decrypted_string = cipher.decrypt(encrypted_string)

        self.assertEqual(string_to_encrypt, decrypted_string)

    def test_decrypted_with_different_key_does_not_match_string_to_encrypt_using_64_bit_key(self):

        # setup encryption cipher
        encrypt_cipher_key = 'D8\r3#\t\n:'
        encrypt_cipher = self.xor.XorChipher(encrypt_cipher_key)

        # setup decryption cipher
        decrypt_cipher_key = 'B\rG@3]dP'
        decrypt_cipher = self.xor.XorChipher(decrypt_cipher_key)

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = encrypt_cipher.encrypt(string_to_encrypt)
        decrypted_string = decrypt_cipher.decrypt(encrypted_string)

        self.assertNotEqual(string_to_encrypt, decrypted_string)

# =========== Enhanced Xor

    def test_string_to_encrypt_is_not_equal_to_enhanced_xor_encrypted_string_using_64_bit_key(self):

        # setup cipher
        cipher_key = "A9g@;dE9"
        cipher = self.xor.XorChipher( cipher_key )

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = cipher.enhanced_encrypt(string_to_encrypt)

        self.assertNotEqual( string_to_encrypt, encrypted_string )

    def test_enhanced_xor_decrypted_string_is_equals_to_string_to_encrypt_using_64_bit_key(self):

        # setup cipher
        cipher_key = "A9g@;dE9"
        cipher = self.xor.XorChipher(cipher_key)

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = cipher.enhanced_encrypt(string_to_encrypt)
        decrypted_string = cipher.enhanced_encrypt(encrypted_string)

        self.assertEqual(string_to_encrypt, decrypted_string)

    def test_enhanced_xor_decrypted_with_different_key_does_not_equals_to_string_to_encrypt_using_64_bit_key(self):

        # setup encryption cipher
        encryption_cipher_key = "A9g@;dE9"
        encryption_cipher = self.xor.XorChipher(encryption_cipher_key)

        # setup decryption cipher
        decryption_cipher_key = "H:Ai83@G"
        decryption_cipher = self.xor.XorChipher(decryption_cipher_key)

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = encryption_cipher.enhanced_encrypt(string_to_encrypt)
        decrypted_string = decryption_cipher.enhanced_encrypt(encrypted_string)

        self.assertNotEqual(string_to_encrypt, decrypted_string)

    def test_enhanced_xor_decrypted_with_key_in_different_order_does_not_match_string_to_encrypt_using_64_bit_key(self):

        # set up encryption cipher
        encrypt_cipher_key = "A9g@;dE9"
        encrypt_cipher = self.xor.XorChipher(encrypt_cipher_key)

        # set up decryption cipher
        decrypt_cipher_key = "9A@gd;E9"
        decrypt_cipher = self.xor.XorChipher(decrypt_cipher_key)

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = encrypt_cipher.enhanced_encrypt(string_to_encrypt)
        decrypted_string = decrypt_cipher.enhanced_encrypt(encrypted_string)

        self.assertNotEqual( decrypted_string, string_to_encrypt )

    def test_enhanced_brute_force_decryption_method_finds_string_to_encryption_and_32_bit_key(self):

        # set up encryption cipher
        encrypt_cipher_key = 'D7'
        encrypt_cipher = self.xor.XorChipher(encrypt_cipher_key)

        # set up decryption cipher
        # (we dont need a key it is done in the brute force method.)
        decrypt_cipher = self.xor.XorChipher("")

        # set up brute force
        brute_force = bruteForceMethods.BruteForce()

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = encrypt_cipher.enhanced_encrypt(string_to_encrypt);

        # get all pos keys and string
        possible_strings = brute_force.enhanced_xor(decrypt_cipher, encrypted_string, 2, True, True)
        print(possible_strings)
        # prove that the key and string only occors once
        self.assertTrue( (encrypt_cipher_key, string_to_encrypt) in possible_strings)

# =========== findings and curiosity
    def test_encrypt_twice_returns_decrypted_str_using_64_bit_key(self):

        # I found this by accident.
        # If we look at my implermentation of xor decrypt it goes through the
        # key backwards. But i accidentally encrypted it twice which seamed to
        # of decrypted it along with the decrypt method also working.

        # setup cipher
        cipher_key = 'D8\r3#\t\n:'
        cipher = self.xor.XorChipher(cipher_key)

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = cipher.encrypt(string_to_encrypt)
        decrypted_string = cipher.encrypt(encrypted_string)

        self.assertEqual(string_to_encrypt, decrypted_string)

    def test_decrypted_with_key_in_different_order_returns_correct_decrypted_str_using_64_bit_key(self):

        # It got me thinking does it mater what order the key is in ?

        # setup encryption cipher
        encrypt_cipher_key = 'D8\r3#\t\n:'
        encrypt_cipher = self.xor.XorChipher(encrypt_cipher_key)

        # setup decryption cipher
        decrypt_cipher_key = 'D\r83\t#\n:'
        decrypt_cipher = self.xor.XorChipher(decrypt_cipher_key)

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = encrypt_cipher.encrypt(string_to_encrypt)
        decrypted_string = decrypt_cipher.encrypt(encrypted_string)

        self.assertEqual(string_to_encrypt, decrypted_string)

        # It turns out no. as long as all the characters are there
        # no more, no less and in any order it will always decrypt
        # I guess i need to do some reading on xor...
        # :D


if __name__ == '__main__':
    unittest.main()