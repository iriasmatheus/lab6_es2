class Horario:
    def __init__(self, horas, minutos):
        self._horas = horas
        self._minutos = minutos

    def validacao_horario(self):
        if not (self._horas >= 0 and self._horas <= 23):
            raise Exception("Horário inválido")
        if not (self._minutos >= 0 and self._minutos <= 59):
            raise Exception("Horário inválido")


class Data:
    def __init__(self, dia, mes, ano):
        self._dia = dia
        self._mes = mes
        self._ano = ano

    def validacao_data(self):
        if not (self._mes >= 1 and self._mes <= 12):
            raise Exception("Data inválida")
        if self._mes in [1, 3, 5, 7, 8, 10, 12]:
            self.validaMesesCom31Dias()
        elif self._mes in [4, 6, 9, 11]:
            self.validaMesesCom30Dias()
        elif self._mes == 2:
            if self._ano % 4 == 0:
                if not (self._dia >= 1 and self._dia <= 29):
                    raise Exception("Data inválida")
            else:
                if not (self._dia >= 1 and self._dia <= 28):
                    raise Exception("Data inválida")

    def validaMesesCom31Dias(self):
        if not (self._dia >= 1 and self._dia <= 31):
            raise Exception("Data inválida")

    def validaMesesCom30Dias(self):
        if not (self._dia >= 1 and self._dia <= 30):
            raise Exception("Data inválida")

class DataEHora:
    def __init__(self,  data, horario):
        self._data = data
        self._horario = horario

class Tarefa:
    def __init__(self, nome, inicio, fim):
        self._nome = nome
        self._inicio = inicio
        self._fim = fim
