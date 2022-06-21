import copy
import numpy as np
from helpers.numbers_base_conversions import decimal_to_binary, binary_to_decimal

def convert_binary_to_str(decoded_binary_map):
    chunk = ""
    for char_binary in decoded_binary_map:
        char_decimal = binary_to_decimal(np.array(char_binary).flatten())
        chunk += chr(char_decimal)
    return chunk

def decode(decimal_integer_list):
    string_chucks = []
    for decimal_number in decimal_integer_list:
        binary_number = decimal_to_binary(decimal_number)
        # print(binary_number)
        binary_number_str = str(binary_number)
        encoded_binary = []
        for a in range(4):
            encoded_binary.append([0, 0, 0, 0, 0, 0, 0, 0])
        char_count = -1
        for i in range(len(binary_number_str)):
            bit = binary_number_str[::-1][i]
            if i % 8 == 0:
                char_count += 1
            # print(f'[{char_count}][{i%8}]')
            encoded_binary[char_count][i % 8] = int(bit)
        # print(encoded_binary)

        # reverse characters and bits back when done
        encoded_binary.reverse()
        for char in encoded_binary:
            char.reverse()
        # print(encoded_binary)

        decoded_binary = copy.deepcopy(encoded_binary)

        # decoding happens here
        for x in range(4):
            for i in range(8):
                pos = (x*2)+1 if i > 3 else (x*2)
                decoded_binary[i % 4][pos] = encoded_binary[x][i]

        # print(decoded_binary)

        decoded_binary.reverse()

        chunk = convert_binary_to_str(decoded_binary).rstrip('\x00')
        string_chucks.append(chunk)
    decoded_str = "".join(string_chucks)
    return decoded_str