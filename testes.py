import unittest
from classes import Horario, Data

class Testes(unittest.TestCase):

    def testExcecaoHorarioInvalido(self):
        self.horario = Horario(horas = 23, minutos = 75)
        with self.assertRaises(Exception):
            self.horario.validacao_horario()

    def testExcecaoDataInvalida31Dias(self):
        self.data = Data(dia = 35, mes = 3, ano = 2022)
        with self.assertRaises(Exception):
            self.data.validacao_data()

    def testExcecaoDataInvalida30Dias(self):
        self.data = Data(dia = 31, mes = 4, ano = 2022)
        with self.assertRaises(Exception):
            self.data.validacao_data()