import unittest
from classes import Horario, Data, DataEHora, Tarefa

class TestesDataEHora(unittest.TestCase):

    def testExcecaoHoraInvalida(self):
        self.horario = Horario(horas = 25, minutos = 55)
        with self.assertRaises(Exception):
            self.horario.validaHoras()

    def testExcecaoMinutosInvalidos(self):
        self.horario = Horario(horas = 23, minutos = 75)
        with self.assertRaises(Exception):
            self.horario.validaMinutos()

    def testExcecaoDataInvalida31Dias(self):
        self.data = Data(dia = 35, mes = 3, ano = 2022)
        with self.assertRaises(Exception):
            self.data.validacao_data()

    def testExcecaoDataInvalida30Dias(self):
        self.data = Data(dia = 31, mes = 4, ano = 2022)
        with self.assertRaises(Exception):
            self.data.validacao_data()
    
    def testExcecaoDataInvalidaFevereiro(self):
        self.data = Data(dia = 29, mes = 2, ano = 2022)
        with self.assertRaises(Exception):
            self.data.validacao_data()

class TestesTarefa(unittest.TestCase):

    def setUp(self):
        self.data1 = Data(dia = 8, mes = 2, ano = 2022)
        self.hora = Horario(horas = 20, minutos = 15)
        self.inicio = DataEHora(data = self.data1, horario = self.hora)

    def testExcecaoDatasTarefa(self):
        self.data2 = Data(dia = 31, mes = 12, ano = 2021)
        self.fim = DataEHora(data = self.data2, horario = self.hora)
        self.tarefa = Tarefa(nome = 'Tarefa 1', inicio = self.inicio, fim = self.fim)
        with self.assertRaises(Exception):
            self.tarefa.validaDatasInicioEFim()

    def testExcecaoDatasTarefa2(self):
        self.data2 = Data(dia = 31, mes = 1, ano = 2022)
        self.fim = DataEHora(data = self.data2, horario = self.hora)
        self.tarefa = Tarefa(nome = 'Tarefa 2', inicio = self.inicio, fim = self.fim)
        with self.assertRaises(Exception):
            self.tarefa.validaDatasInicioEFim()