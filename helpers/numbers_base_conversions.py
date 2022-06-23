from typing import List


class NumberBaseConversions:
    
    @staticmethod
    def decimal_to_binary(n):
        return bin(n).replace("0b", "")

    @staticmethod
    def binary_to_decimal(binaryArray: List[int]):
        i = 0
        integer = 0
        size = len(binaryArray)
        while i < len(binaryArray):
            integer += binaryArray[size - 1 - i]*pow(2, i)
            i += 1
        return integer
