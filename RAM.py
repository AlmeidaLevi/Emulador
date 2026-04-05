from array import array


class RAM:
    def __init__(self):
        self.memory = array('L', [0]) * (1024 * 1024 // 4)

    def read_word(self, address):
        word_address = address & 0b111111111111111111
        return self.memory[word_address]

    def write_word(self, address, value):
        word_address = address & 0b111111111111111111
        value = value & 0xFFFFFFFF
        self.memory[word_address] = value

    def read_byte(self, address):
        word_address = (address & 0b111111111111111111) >> 2
        word = self.memory[word_address]

        byte_address = address & 0b11

        byte = word >> (byte_address << 3)

        return byte

    def write_byte(self, address, value):
        word_address = (address & 0b1111111111111111111) >> 2
        byte_address = address & 0b11

        mask = ~(0xFF << (byte_address << 3))

        word = self.memory[word_address] & mask

        value = (value & 0xFF) << (byte_address << 3)
        word = word | value
        self.memory[word_address] = word
