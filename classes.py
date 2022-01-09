class Horario:
    def __init__(self, horas, minutos):
        self._horas = horas
        self._minutos = minutos

    def validaHoras(self):
        if not (self._horas >= 0 and self._horas <= 23):
            raise Exception("Horário inválido")
    
    def validaMinutos(self):
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
                self.validaFevereiroEmAnoBissexto()
            else:
                self.validaFevereiroEmAnosComuns()

    def validaMesesCom31Dias(self):
        if not (self._dia >= 1 and self._dia <= 31):
            raise Exception("Data inválida")

    def validaMesesCom30Dias(self):
        if not (self._dia >= 1 and self._dia <= 30):
            raise Exception("Data inválida")

    def validaFevereiroEmAnoBissexto(self):
        if not (self._dia >= 1 and self._dia <= 29):
            raise Exception("Data inválida")

    def validaFevereiroEmAnosComuns(self):
        if not (self._dia >= 1 and self._dia <= 28):
            raise Exception("Data inválida")

class DataEHora:
    def __init__(self,  data, horario):
        self._data = data
        self._horario = horario

class Evento:
    def __init__(self, nome, inicio, fim):
        self._nome = nome
        self._inicio = inicio
        self._fim = fim

    def validaAnosInicioEFim(self):
        if self._fim._data._ano < self._inicio._data._ano:
            raise Exception("Início acontece depois do fim")

    def validaMesesInicioEFim(self):
        if self._fim._data._ano == self._inicio._data._ano and self._fim._data._mes < self._inicio._data._mes:
                raise Exception("Início acontece depois do fim")

    def validaDiasInicioEFim(self):
        if self._fim._data._mes == self._inicio._data._mes and self._fim._data._dia < self._inicio._data._dia:
                raise Exception("Início acontece depois do fim")

    def validaHorasInicioEFim(self):
        if self._fim._data._dia == self._inicio._data._dia and self._fim._horario._horas < self._inicio._horario._horas:
                raise Exception("Início acontece depois do fim")

    def validaMinutosInicioEFim(self):
        if self._fim._horario._horas == self._inicio._horario._horas and self._fim._horario._minutos < self._inicio._horario._minutos:
                raise Exception("Início acontece depois do fim")