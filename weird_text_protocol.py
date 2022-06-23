import numpy as np
import copy
from typing import List
from helpers.numbers_base_conversions import NumberBaseConversions
from helpers.string_manipulation import StringManipulation


class WeirdTextProtocol:

    chunk_size = 4
    bit_size = 8

    def encode(self, string):
        """ 
        Loops through the string in chunks of 4 characters. 
        Converts each chunk into a binary 2D array each element representing a character.
        Reverse characters and bits for simpler logic
        Makes copy to start encoding it
        Reverses the characters and bits back when done
        Converts encoded binary to decimal and returns
        """
        integer_list = []
        for chunk in StringManipulation.split_chunks(string, self.chunk_size):
            raw_binary = self.__convert_str_to_binary(chunk)

            raw_binary.reverse()
            for char in raw_binary:
                char.reverse()

            encoded_binary = [copy.copy(char) for char in raw_binary]

            # encoding
            for x in range(self.chunk_size):
                for i in range(self.bit_size):
                    pos = (x*2)+1 if i > 3 else (x*2)
                    encoded_binary[x][i] = int(
                        raw_binary[i % self.chunk_size][pos])

            encoded_binary.reverse()
            for char in encoded_binary:
                char.reverse()

            integer_list.append(NumberBaseConversions.binary_to_decimal(
                np.array(encoded_binary).flatten()))
        return integer_list

    def decode(self, decimal_integer_list: List[int]):
        """
        Loops through each number and converts it into a binary 
        The binary number is then converted into a array of binary bits
        Reverse characters and bits for simpler logic
        Makes copy to start dencoding it
        Reverses the characters and back when done
        Append decoded string chunk to list. When done join and return as string
        """
        string_chucks = []
        for decimal_number in decimal_integer_list:
            binary_number = NumberBaseConversions.decimal_to_binary(
                decimal_number)

            binary_number_str = str(binary_number)
            if len(binary_number_str) > self.chunk_size * self.bit_size:
                raise Exception(f'Error: {decimal_number} is longer than {self.chunk_size * self.bit_size} bits')

            encoded_binary = []
            for a in range(self.chunk_size):
                encoded_binary.append([0, 0, 0, 0, 0, 0, 0, 0])

            char_count = -1
            for i in range(len(binary_number_str)):
                bit = binary_number_str[::-1][i]
                if i % self.bit_size == 0:
                    char_count += 1
                encoded_binary[char_count][i % self.bit_size] = int(bit)

            encoded_binary.reverse()
            for char in encoded_binary:
                char.reverse()

            decoded_binary = [copy.copy(char) for char in encoded_binary]

            # decoding
            for x in range(self.chunk_size):
                for i in range(self.bit_size):
                    pos = (x*2)+1 if i > 3 else (x*2)
                    decoded_binary[i %
                                   self.chunk_size][pos] = encoded_binary[x][i]

            decoded_binary.reverse()

            chunk = self.__convert_binary_to_str(decoded_binary).rstrip('\x00')
            string_chucks.append(chunk)
        decoded_str = "".join(string_chucks)
        return decoded_str

    def __convert_str_to_binary(self, string):
        """ 
        loop through each character from back to front
        convert char to ASCII/Decimal
        convert ASCII to binary, pad with 0s if needed
        append to raw_bianry array then return that array
        """

        raw_binary = []

        for char in string[::-1]:
            char_decimal = ord(char)
            char_binary_str = NumberBaseConversions.decimal_to_binary(
                char_decimal)
            char_binary = [int(bit) for bit in char_binary_str]
            while(len(char_binary) % self.bit_size != 0):
                char_binary.insert(0, 0)
            raw_binary.append(char_binary)

        while(len(raw_binary) < self.chunk_size):
            raw_binary.insert(0, [0, 0, 0, 0, 0, 0, 0, 0])

        return raw_binary

    def __convert_binary_to_str(self, binary_map):
        """
        For each binary char representation, convert to decimal.
        Convert decimal to character
        Append char to chunk. Once done return string chunk
        """
        chunk = ""
        for char_binary in binary_map:
            char_decimal = NumberBaseConversions.binary_to_decimal(
                np.array(char_binary).flatten())
            chunk += chr(char_decimal)
        return chunk
