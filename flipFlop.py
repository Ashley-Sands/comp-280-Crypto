
class FlipFlop:

    def __init__(self, min_chr, max_chr, str_len, bytes_=False):

        self.min_chr = min_chr
        self.max_chr = max_chr
        self.str_length = str_len
        self.current_col = str_len - 1
        self.bytes = bytes_

        self.out = [chr(self.min_chr)] * self.str_length
        self.skip = True

    def __iter__(self):
        return self

    def __next__(self):

        self.current_col = self.str_length - 1;
        if not self.skip:
            self.out[self.current_col] = chr( ord(self.out[self.current_col]) + 1 )
        else:
            self.skip = False


        while ord( self.out[ self.current_col ] ) > self.max_chr:

            self.out[ self.current_col ] = chr(self.min_chr)
            self.current_col -= 1;

            if self.current_col == -1:
                raise StopIteration()

            self.out[self.current_col] = chr(ord(self.out[self.current_col]) + 1)

        if self.bytes:
            return ''.join(self.out).encode("utf-8")
        else:
            return ''.join(self.out)

    def set_key_len(self, len):
        self.str_length = len

    def set_chr_range(self, min_c, max_c):
        self.min_chr = min_c
        self.max_chr = max_c
