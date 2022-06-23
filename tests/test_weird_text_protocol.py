from weird_text_protocol import WeirdTextProtocol
import unittest

class TestWeirdTextProtocol(unittest.TestCase):
    __protocol = WeirdTextProtocol()

    def test_no_space(self):
        string = 'tacocat'
        self.assertEqual((self.__protocol.decode(
            self.__protocol.encode(string))), string)

    def test_with_spaces(self):
        string = 'never odd or even'
        self.assertEqual((self.__protocol.decode(
            self.__protocol.encode(string))), string)

    def test_with_comas(self):
        string = 'lager, sir, is regaln'
        self.assertEqual((self.__protocol.decode(
            self.__protocol.encode(string))), string)

    def test_with_escape_char(self):
        string = 'go hang a salami, I\'m a lasagna hog'
        self.assertEqual((self.__protocol.decode(
            self.__protocol.encode(string))), string)

    def test_with_a_coma(self):
        string = 'egad, a base tone denotes a bad age'
        self.assertEqual((self.__protocol.decode(
            self.__protocol.encode(string))), string)