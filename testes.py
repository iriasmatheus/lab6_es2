import unittest
from classes import Horario

class Testes(unittest.TestCase):

    def testExcecaoHorarioInvalido(self):
        self.horario = Horario(horas = 23, minutos = 75)
        with self.assertRaises(Exception):
            self.horario.validacao_horario()
