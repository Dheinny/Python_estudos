import unittest
from src.cpf_validator import CPFValidator

class CPFValidatorTests(unittest.TestCase):

    def test_retira_formatacao_test01(self):
        self.assertEqual(CPFValidator().retira_formatacao("324.325.432-66"), "32432543266")

    def test_retira_formatacao_test02(self):
        self.assertNotRegex(CPFValidator().retira_formatacao("32a.32s.4e2-66"), "\\d{11}")

    def test_calcula_mod11_test01(self):
        self.assertEqual(7, CPFValidator().calcula_mod11("43963273070", 9))

    def test_calcula_mod11_test02(self):
        self.assertEqual(0, CPFValidator().calcula_mod11("43963273070", 10))

    def test_valida_cpf_test01(self):
        cpf_clean = CPFValidator().retira_formatacao("439.632.730-70")
        self.assertTrue(CPFValidator().valida_cpf(cpf_clean))

    def test_valida_cpf_test02(self):
        cpf_clean = CPFValidator().retira_formatacao("439.633.730-70")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean))

    def test_valida_cpf_test03(self):
        cpf_clean = CPFValidator().retira_formatacao("999.99.9-99")
        self.assertRaises(ValueError, CPFValidator().valida_cpf, cpf_clean)

    def test_valida_cpf_test04(self):
        cpf_clean = CPFValidator().retira_formatacao("439.632.730-89")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "É falso, pois DV1 deveria ser 7")

    def test_valida_cpf_test05(self):
        cpf_clean = CPFValidator().retira_formatacao("439.633.730-71")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "É falso, pois DV2 deveria ser 0")

    def test_valida_cpf_test06(self):
        cpf_clean = CPFValidator().retira_formatacao("111.111.111-11")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "{} não deve ser válido".format(cpf_clean))

    def test_valida_cpf_test07(self):
        cpf_clean = CPFValidator().retira_formatacao("222.222.222-22")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "{} não deve ser válido".format(cpf_clean))

    def test_valida_cpf_test08(self):
        cpf_clean = CPFValidator().retira_formatacao("333.333.333-33")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "{} não deve ser válido".format(cpf_clean))

    def test_valida_cpf_test09(self):
        cpf_clean = CPFValidator().retira_formatacao("444.444.444-44")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "{} não deve ser válido".format(cpf_clean))

    def test_valida_cpf_test10(self):
        cpf_clean = CPFValidator().retira_formatacao("555.555.555-55")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "{} não deve ser válido".format(cpf_clean))

    def test_valida_cpf_test11(self):
        cpf_clean = CPFValidator().retira_formatacao("666.666.666-66")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "{} não deve ser válido".format(cpf_clean))

    def test_valida_cpf_test12(self):
        cpf_clean = CPFValidator().retira_formatacao("777.777.777-77")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "{} não deve ser válido".format(cpf_clean))

    def test_valida_cpf_test13(self):
        cpf_clean = CPFValidator().retira_formatacao("888.888.888-88")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "{} não deve ser válido".format(cpf_clean))

    def test_valida_cpf_test14(self):
        cpf_clean = CPFValidator().retira_formatacao("999.999.999-99")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "{} não deve ser válido".format(cpf_clean))

    def test_valida_cpf_test15(self):
        cpf_clean = CPFValidator().retira_formatacao("000.000.000-00")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "{} não deve ser válido".format(cpf_clean))

if __name__ == "__main__":
    unittest.main()