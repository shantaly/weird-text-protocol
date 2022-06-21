def decimal_to_binary(n):
    return bin(n).replace("0b", "")


def binary_to_decimal(binaryArray):
    i = 0
    integer = 0
    size = len(binaryArray)
    while i < len(binaryArray):
        integer += binaryArray[size - 1 - i]*pow(2, i)
        i += 1
    return integer
