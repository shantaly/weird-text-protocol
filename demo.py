from weird_text_protocol import WeirdTextProtocol

class Demo:
    __protocol = WeirdTextProtocol()
    
    def run(self):
        choice = None
        while choice != '3':
            print('\nPick one of the following:')
            print('1. Encode a phrase')
            print('2. Decode a list of integer values')
            print('3. Quit')

            choice = input()
            if choice == '1':
                self.encode_demo()
            elif choice == '2':
                self.decode_demo()
            elif choice == '3':
                print('Goodbye :)')
    
    def encode_demo(self):
        print('Please enter the phrase')
        text_to_encode = input()
        encoded_number_list = self.__protocol.encode(text_to_encode)
        print(f'Encoded phrase: {encoded_number_list}')

    def decode_demo(self):
        print('Enter numbers list seperate it by commas. (ex. 199408003, 133178887, 192024619, 267402758)')
        numbers_to_decode_str = input()
        numbers_to_decode = []
        try:
            for number in numbers_to_decode_str.split(','):
                numbers_to_decode.append(int(number.strip())) 
        except Exception as e: 
            print(e)

        if len(numbers_to_decode) > 0:
            try:
                decoded_phrase = self.__protocol.decode(numbers_to_decode)
                print(f'Decoded phrase: {decoded_phrase}')
            except Exception as e:
                print(e)

if __name__ == "__main__":
    app = Demo()
    app.run()