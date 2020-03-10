from datetime import date
from Tests.Exceptions import InvalidDate


class DateTreatment:

    months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
              'Outubro', 'Novembro', 'Dezembro']

    @classmethod
    def convert_string_to_date(cls, string):
        string.strip()
        if '-' in string:
            string = string.split('-')
        elif '/' in string:
            string = string.split('/')
        else:
            raise InvalidDate('Data inválida! Por favor escreva uma data no formato dd-mm-aaaa ou dd/mm/aaaa')
        try:
            return date(int(string[2]), int(string[1]), int(string[0]))
        except:
            raise InvalidDate('Data inválida! Por favor escreva uma data no formato dd-mm-aaaa ou dd/mm/aaaa')

    @classmethod
    def add_7_years(cls, start_date : date):
        finish_date = date(start_date.year+7, start_date.month, start_date.day)
        return finish_date