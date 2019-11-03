import unittest
import bruteForceMethods
import time



class BaseTestClass( unittest.TestCase ):

    def setUp(self):
        self.started_time = time.time()

    def tearDown(self):
        self.elapsed_time = time.time() - self.started_time
        print( '.'.join('{} ( {}s )'.format( self.id(), round( self.elapsed_time, 3 ) ).split('.')[1:]) )


class CaesarTest( BaseTestClass ):

    import ceasar

    def test_string_is_not_equal_to_caesar_encrypted_string(self):

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

    def test_string_is_not_equal_to_encrypted_string(self):

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

class AesCryptographyTest( unittest.TestCase ):

    import aes

    def test_string_is_not_equal_to_aes_encrypted_string(self):
        pass


class Aes__Test( unittest.TestCase ):
    pass

if __name__ == '__main__':
    unittest.main()



