import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class AES:

    '''
    @Param Key_len: must be 16, 24 or 32
    '''
    def __init__(self, key_len = 16):
        self.encryption_key = os.urandom(key_len)
        self.mode_key = os.urandom(16)
        self.cipher = Cipher( algorithms.AES( self.encryption_key ), modes.CBC( self.mode_key ), default_backend() )

    def new_cipher(self, e_key):

        self.cipher = Cipher( algorithms.AES( e_key ), modes.CBC( self.mode_key ), default_backend() )

    def encrypt(self, string):

        print( "(s) len", len(string) )
        string = self.pad_data( string , 16 )
        print( "(e) len", len(string) )

        encryptor = self.cipher.encryptor()
        encrypted = encryptor.update( bytes( string, 'utf-8' ) ) + encryptor.finalize()

        return encrypted

    def decrypt(self, bstr):

        decryptor = self.cipher.decryptor()
        decrypted = decryptor.update(bstr) + decryptor.finalize()

        return decrypted

    def print_keys(self):
        m = 0
        i = 1
        for k in self.encryption_key :
            print( i, "e_key: ", k )
            if k > m:
                m = k;
            i += 1
        print( "max", m )
        print( "e_key ", self.encryption_key )
        print( "int from bytes ", int.from_bytes(self.encryption_key, byteorder = "big" ) )
        print("Len: ", len( str( int.from_bytes(self.encryption_key, byteorder = "big" ) ) ) )
        print( "e_key_len", len(self.encryption_key))
        print( "e_key", self.encryption_key )
        print( "m_key: ", self.mode_key )


    def pad_data(self, string, mult_length):

        pad_len = 0

        if len(string) % mult_length > 0:
            pad_len = mult_length - ( len(string) % mult_length )

        padding = " " * pad_len
        string += padding

        return string

