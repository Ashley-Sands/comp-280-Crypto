from Test.base_test import *


class AesCyptodomeTest(BaseTestClass):

    import Encryptions.aes_cryptodome as aes_cryptodome

    def test_string_to_encrypt_is_not_equal_to_encrypted_string(self):

        # set up cipher
        cipher = self.aes_cryptodome.AES()

        # encrypt string
        str_to_encrypt = "Helloo World"
        encrypted_string = cipher.encrypt(str_to_encrypt)

        # test
        self.assertNotEqual( str_to_encrypt, encrypted_string )

    def test_string_to_encrypt_is_equal_to_decrypted_string(self):

        # set up cipher
        cipher = self.aes_cryptodome.AES()

        # encrypt string
        str_to_encrypt = "Helloo World"
        encrypted_string = cipher.encrypt(str_to_encrypt)
        # using this lib we must create a new cipher to decode :|
        cipher.new_cipher()
        decrypted_string = cipher.decrypt( encrypted_string )

        # test
        self.assertEqual(str_to_encrypt, decrypted_string)

    def test_string_to_encrypt_does_not_equal_decrypted_string_with_different_cipher(self):
        # set up cipher
        encrypt_cipher = self.aes_cryptodome.AES()
        decrypt_cipher = self.aes_cryptodome.AES()

        # encrypt string
        str_to_encrypt = "Helloo World"
        encrypted_string = encrypt_cipher.encrypt(str_to_encrypt)
        decrypted_string = decrypt_cipher.decrypt(encrypted_string)

        # test
        self.assertNotEqual(str_to_encrypt, decrypted_string)


if __name__ == '__main__':
    unittest.main()