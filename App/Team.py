class Team:

    def __init__(self, team_id: int, shift: str, start_course: str):
        self.start_course = start_course
        self.shift = shift
        self.finish_course = (start_course + 7)
        self.name = self.create_name()
        self.team_id = team_id

    def create_name(self):
        return 0 #VAMOS FAZER UNS TESTES PARA QUE A PROPRIA CLASSE TEAM CONSIGA CONVERTER "START_COURSE" DE STR
#PARA DATE E CONSIGA CALCULAR (TAMBEM COMO DATE) O FINISH_COURSE


class Student:

    def __init__(self, name, age, type_m, is_graduated, sit_pay_course, team_id):
        self.name = name
        self.age = age
        self.type_m = type_m
        self.is_graduated = is_graduated
        self.sit_pay_curse = sit_pay_course
        self.team_id = team_id
