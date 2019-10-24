import re


class CPFValidator():
    def retira_formatacao(self, num_cpf):
        signs_list = [".", ",", "-", "_", "(", ")", "/", " "]
        cpf_clean = num_cpf.translate(str.maketrans("", "", "".join(signs_list)))
        return cpf_clean

    def calcula_mod11(self, num_cpf, num_dig):
        soma =  0
        start = 10 - num_dig
        for i in range(start, 10):
            soma += i * int(num_cpf[i-1 if start == 1 else i])
        mod11 = soma % 11 if soma % 11 != 10 else 0
        return mod11


    def valida_cpf(self, num_cpf):
        if not re.search("^\\d{11}$", num_cpf):
            raise ValueError
        if all(d == num_cpf[0] for d in num_cpf):
            return False
        dv1 = int(num_cpf[9])
        dv2 = int(num_cpf[10])
        mod_11 = self.calcula_mod11(num_cpf, 9)

        return (True if dv2 == self.calcula_mod11(num_cpf, 10) else False) if dv1 == mod_11 else False