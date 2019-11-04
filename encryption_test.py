import unittest
import bruteForceMethods
import time


# Set up a timer for all test classes
class BaseTestClass( unittest.TestCase ):

    print_elapsed_time_threshold = 0.0001   # < 0 always print else print if > value (sec)

    def setUp(self):
        self.started_time = time.time()

    def tearDown(self):
        self.elapsed_time = time.time() - self.started_time
        if self.elapsed_time > self.print_elapsed_time_threshold:
            print( '.'.join('{} ( {}s )'.format( self.id(), round( self.elapsed_time, 3 ) ).split('.')[1:]) )


class CaesarTest( BaseTestClass ):

    import ceasar

    def test_string_to_encrypt_is_not_equal_to_encrypted_string(self):

        # set up the cipher for testing
        cipher = self.ceasar.Caesar()
        cipher_key = 10
        cipher_max_offset = 200;

        cipher.set_max_offset( cipher_max_offset )
        cipher.set_key( cipher_key )

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = cipher.encrypt(string_to_encrypt)

        # test they are not equals
        self.assertNotEqual(string_to_encrypt, encrypted_string)

    def test_decrypted_is_equal_to_string_to_encrypt(self):

        # setup cipher for testing
        cipher = self.ceasar.Caesar()
        cipher_key = 10
        cipher_max_offset = 200

        cipher.set_max_offset( cipher_max_offset )
        cipher.set_key( cipher_key )

        # encrypt string and decrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = cipher.encrypt(string_to_encrypt)
        decrypted_string = cipher.decrypt(encrypted_string)

        # test that the string to encrypt is equals to the decrypted string
        self.assertEqual( string_to_encrypt, decrypted_string )

    def test_decrypted_with_different_key_does_not_match_string_to_encrypt(self):

        # set up cipher for encryption
        encrypt_cipher = self.ceasar.Caesar()
        encrypt_cipher_key = 10
        encrypt_cipher_offset = 200

        encrypt_cipher.set_max_offset( encrypt_cipher_offset )
        encrypt_cipher.set_key( encrypt_cipher_key )

        # set up cipher for decryption
        decrypt_cipher = self.ceasar.Caesar()
        decrypt_cipher_key = 20
        decrypt_cipher_offset = 200

        decrypt_cipher.set_max_offset(decrypt_cipher_offset)
        decrypt_cipher.set_key(decrypt_cipher_key)

        string_to_encrypt = "Helloo World"

        # encrypt string
        encrypted_string = encrypt_cipher.encrypt( string_to_encrypt )

        # decrypt with other cipher
        decrypted_string = decrypt_cipher.decrypt( encrypted_string )

        self.assertNotEqual(encrypted_string, decrypted_string)

    def test_brute_force_decryption_method_finds_string_to_encryption(self):

        # set up cipher
        cipher = self.ceasar.Caesar()
        cipher_key = 10
        cipher_offset = 200

        cipher.set_max_offset( cipher_offset )
        cipher.set_key( cipher_key )

        # set up brute force
        brute_force = bruteForceMethods.BruteForce()
        brute_force_max_attempts = 200

        # encrypt string
        string_to_encrypt = "Helloo World"
        encrypted_string = cipher.encrypt( string_to_encrypt )

        # brute force are way through the encryption
        possible_strings = brute_force.caesar(encrypted_string, brute_force_max_attempts)

        self.assertTrue( (cipher_key, string_to_encrypt) in possible_strings )


class XorTest( BaseTestClass ):

    import xor

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

    def test_brute_force_decryption_method_finds_string_to_encryption_using_64_bit_key(self):
        pass

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

        # encrypt cipher
        string_to_encrypt = "Helloo World"
        encrypted_string = encrypt_cipher.enhanced_encrypt(string_to_encrypt)
        decrypted_string = decrypt_cipher.enhanced_encrypt(encrypted_string)

        self.assertNotEqual( decrypted_string, string_to_encrypt )


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


class AesCryptographyTest( BaseTestClass ):

    import aes

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


class Aes__Test( unittest.TestCase ):
    pass

if __name__ == '__main__':
    unittest.main()



