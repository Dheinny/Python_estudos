import unittest
from roman_numbers.src.converte_romano import ConverteRomano

class ConverteRomanoTests(unittest.TestCase):

    def test_converte2romano_test01(self):
        print("3999 : {}".format(ConverteRomano().converte2romano(3999)))
        self.assertEqual("MMMCMXCIX", ConverteRomano().converte2romano(3999))


    def test_converte2romano_test02(self):
        print("1 : {}".format(ConverteRomano().converte2romano(1)))
        self.assertEqual("I", ConverteRomano().converte2romano(1))

    def test_converte2romano_test03(self):
        print("3 : {}".format(ConverteRomano().converte2romano(3)))
        self.assertEqual("III", ConverteRomano().converte2romano(3))

    def test_converte2romano_test04(self):
        print("4 : {}".format(ConverteRomano().converte2romano(4)))
        self.assertEqual("IV", ConverteRomano().converte2romano(4))

    def test_converte2romano_test05(self):
        print("5 : {}".format(ConverteRomano().converte2romano(5)))
        self.assertEqual("V", ConverteRomano().converte2romano(5))

    def test_converte2romano_test06(self):
        print("7 : {}".format(ConverteRomano().converte2romano(7)))
        self.assertEqual("VII", ConverteRomano().converte2romano(7))

    def test_converte2romano_test07(self):
        print("9 : {}".format(ConverteRomano().converte2romano(9)))
        self.assertEqual("IX", ConverteRomano().converte2romano(9))

    def test_converte2romano_test08(self):
        print("10 : {}".format(ConverteRomano().converte2romano(10)))
        self.assertEqual("X", ConverteRomano().converte2romano(10))

    def test_converte2romano_test09(self):
        print("14 : {}".format(ConverteRomano().converte2romano(14)))
        self.assertEqual("XIV", ConverteRomano().converte2romano(14))

    def test_converte2romano_test99(self):
        print("24 : {}".format(ConverteRomano().converte2romano(24)))
        self.assertEqual("XXIV", ConverteRomano().converte2romano(24))

    def test_converte2romano_test98(self):
        print("36 : {}".format(ConverteRomano().converte2romano(36)))
        self.assertEqual("XXXVI", ConverteRomano().converte2romano(36))

    def test_converte2romano_test97(self):
        print("12 : {}".format(ConverteRomano().converte2romano(12)))
        self.assertEqual("XII", ConverteRomano().converte2romano(12))


    def test_converte2romano_test10(self):
        print("40 : {}".format(ConverteRomano().converte2romano(40)))
        self.assertEqual("XL", ConverteRomano().converte2romano(40))

    def test_converte2romano_test11(self):
        print("50 : {}".format(ConverteRomano().converte2romano(50)))
        self.assertEqual("L", ConverteRomano().converte2romano(50))

    def test_converte2romano_test12(self):
        print("60 : {}".format(ConverteRomano().converte2romano(60)))
        self.assertEqual("LX", ConverteRomano().converte2romano(60))

    def test_converte2romano_test13(self):
        print("70 : {}".format(ConverteRomano().converte2romano(70)))
        self.assertEqual("LXX", ConverteRomano().converte2romano(70))

    def test_converte2romano_test14(self):
        print("80 : {}".format(ConverteRomano().converte2romano(80)))
        self.assertEqual("LXXX", ConverteRomano().converte2romano(80))

    def test_converte2romano_test15(self):
        print("90 : {}".format(ConverteRomano().converte2romano(90)))
        self.assertEqual("XC", ConverteRomano().converte2romano(90))

    def test_converte2romano_test16(self):
        print("100 : {}".format(ConverteRomano().converte2romano(100)))
        self.assertEqual("C", ConverteRomano().converte2romano(100))

    def test_converte2romano_test17(self):
        print("500 : {}".format(ConverteRomano().converte2romano(500)))
        self.assertEqual("D", ConverteRomano().converte2romano(500))

    def test_converte2romano_test18(self):
        print("439 : {}".format(ConverteRomano().converte2romano(439)))
        self.assertEqual("CDXXXIX", ConverteRomano().converte2romano(439))

    def test_converte2romano_test19(self):
        print("757 : {}".format(ConverteRomano().converte2romano(757)))
        self.assertEqual("DCCLVII", ConverteRomano().converte2romano(757))

    def test_converte2romano_test20(self):
        print("767 : {}".format(ConverteRomano().converte2romano(767)))
        self.assertEqual("DCCLXVII", ConverteRomano().converte2romano(767))

    def test_converte2romano_test21(self):
        print("1894 : {}".format(ConverteRomano().converte2romano(1894)))
        self.assertEqual("MDCCCXCIV", ConverteRomano().converte2romano(1894))

    def test_converte2romano_test22(self):
        print("2503 : {}".format(ConverteRomano().converte2romano(2503)))
        self.assertEqual("MMDIII", ConverteRomano().converte2romano(2503))

    def test_converte2romano_test23(self):
        print("876 : {}".format(ConverteRomano().converte2romano(876)))
        self.assertEqual("DCCCLXXVI", ConverteRomano().converte2romano(876))

    def test_converte2romano_test24(self):
        print("268 : {}".format(ConverteRomano().converte2romano(268)))
        self.assertEqual("CCLXVIII", ConverteRomano().converte2romano(268))

    def test_converte2romano_test25(self):
        print("321 : {}".format(ConverteRomano().converte2romano(321)))
        self.assertEqual("CCCXXI", ConverteRomano().converte2romano(321))
