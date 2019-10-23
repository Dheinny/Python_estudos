import unittest
from src.cpf_validator import CPFValidator

class CPFValidatorTests(unittest.TestCase):

    def test_retira_formatacao_test1(self):
        self.assertEqual(CPFValidator().retira_formatacao("324.325.432-66"), "32432543266")

    def test_retira_formatacao_test2(self):
        self.assertNotRegex(CPFValidator().retira_formatacao("32a.32s.4e2-66"), "\\d{11}")

    def test_calcula_mod11_test1(self):
        self.assertEqual(7, CPFValidator().calcula_mod11("43963273070", 9))

    def test_calcula_mod11_test2(self):
        self.assertEqual(0, CPFValidator().calcula_mod11("43963273070", 10))

    def test_valida_cpf_test1(self):
        cpf_clean = CPFValidator().retira_formatacao("439.632.730-70")
        self.assertTrue(CPFValidator().valida_cpf(cpf_clean))

    def test_valida_cpf_test2(self):
        cpf_clean = CPFValidator().retira_formatacao("439.633.730-70")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean))

    def test_valida_cpf_test3(self):
        cpf_clean = CPFValidator().retira_formatacao("111.111.111-11")
        self.assertTrue(CPFValidator().valida_cpf(cpf_clean))

    def test_valida_cpf_test4(self):
        cpf_clean = CPFValidator().retira_formatacao("444.444.444-44")
        self.assertTrue(CPFValidator().valida_cpf(cpf_clean))

    def test_valida_cpf_test5(self):
        cpf_clean = CPFValidator().retira_formatacao("999.999.999-99")
        self.assertTrue(CPFValidator().valida_cpf(cpf_clean))

    def test_valida_cpf_test6(self):
        cpf_clean = CPFValidator().retira_formatacao("999.99.9-99")
        self.assertRaises(ValueError, CPFValidator().valida_cpf, cpf_clean)

    def test_valida_cpf_test7(self):
        cpf_clean = CPFValidator().retira_formatacao("439.632.730-89")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "É falso, pois DV1 deveria ser 7")

    def test_valida_cpf_test8(self):
        cpf_clean = CPFValidator().retira_formatacao("439.633.730-71")
        self.assertFalse(CPFValidator().valida_cpf(cpf_clean), "É falso, pois DV2 deveria ser 0")

    def test_valida_cpf_test9(self):
        cpf_clean = CPFValidator().retira_formatacao("222.222.222-22")
        self.assertTrue(CPFValidator().valida_cpf(cpf_clean))

    def test_valida_cpf_test10(self):
        cpf_clean = CPFValidator().retira_formatacao("333.333.333-33")
        self.assertTrue(CPFValidator().valida_cpf(cpf_clean))

    def test_valida_cpf_test11(self):
        cpf_clean = CPFValidator().retira_formatacao("555.555.555-55")
        self.assertTrue(CPFValidator().valida_cpf(cpf_clean))

    def test_valida_cpf_test12(self):
        cpf_clean = CPFValidator().retira_formatacao("666.666.666-66")
        self.assertTrue(CPFValidator().valida_cpf(cpf_clean))

    def test_valida_cpf_test13(self):
        cpf_clean = CPFValidator().retira_formatacao("777.777.777-77")
        self.assertTrue(CPFValidator().valida_cpf(cpf_clean))

    def test_valida_cpf_test14(self):
        cpf_clean = CPFValidator().retira_formatacao("888.888.888-88")
        self.assertTrue(CPFValidator().valida_cpf(cpf_clean))

    def test_valida_cpf_test15(self):
        cpf_clean = CPFValidator().retira_formatacao("000.000.000-00")
        self.assertTrue(CPFValidator().valida_cpf(cpf_clean))

if __name__ == "__main__":
    unittest.main()