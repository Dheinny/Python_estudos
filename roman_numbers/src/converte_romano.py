import math

class ConverteRomano:
    def __init__(self):
        pass

    def __find_bases(self, num, decimais_list):
        dec = 0
        inter = 0
        for k, v, in decimais_list.items():
            if int(num / k) > 0:
                dec = k
                inter = dec * 5
                break
        return dec, inter

    def converte2romano(self, num):
        decimais_list = {1000: "M", 100: "C", 10: "X", 1: "I"}
        intermediarios_list = {500: "D", 50: "L", 5: "V"}

        res_str = ""
        while(num > 0):
            dec, inter = self.__find_bases(num, decimais_list)

            div = int(num/inter)
            if div > 0:
                n_dec = int((num-inter)/dec)
                res_str += "{}{}".format(decimais_list[dec], decimais_list[dec*10]) if  n_dec > 3 else intermediarios_list[inter]
                num -= (n_dec*dec) + inter if n_dec > 3 else inter
            else:
                n_dec = int(num / dec)
                if n_dec > 3:
                    res_str += "{}{}".format(decimais_list[dec], intermediarios_list[inter])
                else:
                    for n in range(n_dec):
                        res_str += decimais_list[dec]
                num -= n_dec*dec
        return res_str
