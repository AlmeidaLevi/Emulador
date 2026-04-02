from array import array

memory = array("L", [0]) * (1024*1024//4)  # 1 MB de memoria


def read_memory(address):
    address = address & 0b111111111111111111
    return memory[address]


def write_memory(address, new_value):
    address = address & 0b111111111111111111
    new_value = new_value & 0xFF

    memory[address] = new_value


def read_byte(byte_address):
    byte_address = byte_address & 0b11111111111111111111
    byte_memory_position = byte_address >> 2

    byte_slot = byte_address & 0b11

    word_value = memory[byte_memory_position]
    byte_value = word_value >> (byte_slot << 3)
    byte_value = byte_value & 0xFF

    return byte_value


def write_byte(byte_address, new_value):
    byte_address = byte_address & 0b11111111111111111111
    new_value = new_value & 0xFF

    byte_memory_position = byte_address >> 2
    byte_slot = byte_address & 0b11

    word_value = memory[byte_memory_position]

    mask = ~(0xFF << (byte_slot << 3))
    new_word_value = word_value & mask

    new_value = new_value << (byte_slot << 3)

    new_word_value = word_value | new_value

    memory[byte_memory_position] = new_word_value
