from datetime import date
from Tests.Exceptions import InvalidDate


class DateTreatment:
    """
    This class contains the methods responsible to the needed procedures related to dates.
    """

    months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
              'Outubro', 'Novembro', 'Dezembro']

    @classmethod
    def convert_string_to_date(cls, string):
        """
        Converts a string object into a date object.
        :param string: str -> The input string.
        :return: A date object.
        """
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
    def add_7_months(cls, start_date : date):
        """
        This method is responsible for, given a date object, add 7 months to it.
        :param start_date: A date object.
        :return: A date object.
        """
        finish_date = date(start_date.year, start_date.month+7, start_date.day)
        return finish_date