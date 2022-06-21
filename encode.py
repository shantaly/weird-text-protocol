import copy
import numpy as np

from helpers.numbers_base_conversions import decimal_to_binary, binary_to_decimal
from helpers.string_manipulation import split_chunks

CHUNK_SIZE = 4

def convert_str_to_binary(string):
    raw_binary = []

    # loop through each character from back to front
    # convert char to ASCII/Decimal
    # convert ASCII to binary, pad with 0s if needed
    # append to raw_bianry array
    for char in string[::-1]:
        char_decimal = ord(char)
        char_binary_str = decimal_to_binary(char_decimal)
        char_binary = [int(bit) for bit in char_binary_str]
        while(len(char_binary) % 8 != 0):
            char_binary.insert(0, 0)
        raw_binary.append(char_binary)

    # Pad with 0s if needed (triggered if input string was less than 4 characters)
    while(len(raw_binary) < CHUNK_SIZE):
        raw_binary.insert(0, [0, 0, 0, 0, 0, 0, 0, 0])

    return raw_binary


def encode(string):
    integer_list = []
    for chunk in split_chunks(string, CHUNK_SIZE):
        raw_binary = convert_str_to_binary(chunk)
        # print(raw_binary)

        # Being encoding
        # reverse characters and bits for simpler logic
        raw_binary.reverse()
        for char in raw_binary:
            char.reverse()

        # make deepcopy of raw data to start encoding
        encoded_binary = copy.deepcopy(raw_binary)

        # encoding happens here
        for x in range(4):
            for i in range(8):
                pos = (x*2)+1 if i > 3 else (x*2)
                encoded_binary[x][i] = int(raw_binary[i % 4][pos])

        # reverse characters and bits back when done
        encoded_binary.reverse()
        for char in encoded_binary:
            char.reverse()
        # print(encoded_binary)

        integer_list.append(binary_to_decimal(
            np.array(encoded_binary).flatten()))
    return integer_list
