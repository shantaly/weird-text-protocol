

from encode import encode
from decode import decode
from helpers.numbers_base_conversions import decimal_to_binary, binary_to_decimal

def main():

    text_to_encode = 'tacocat'# input("Enter text to encode: ")  # Ask for user input
    encoded_val = encode(text_to_encode)
    print(encoded_val)
    decoded_val = decode(encoded_val)
    print(decoded_val)

    print(text_to_encode == decoded_val)



if __name__ == "__main__":
    main()
