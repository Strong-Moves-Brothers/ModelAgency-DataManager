from App.DateTreatment import DateTreatment
from datetime import date
from Tests.Exceptions import InvalidModelType, InvalidCourseType, InvalidShift, InvalidPaymentStatus


class TeamFactory:

    @classmethod
    def factory(cls, team_course_type : str, team_shift: str, team_start_course_date : str):
        team_start_course_date = DateTreatment.convert_string_to_date(team_start_course_date)
        team_course_type = team_course_type.strip().upper()
        team_shift = team_shift.strip().upper()
        cls._input_verify(team_course_type, team_shift)
        team_finish_course_date = DateTreatment.add_7_years(team_start_course_date)
        team_name = cls._generate_team_name(team_start_course_date, team_course_type, team_shift).strip().upper()
        team_id = cls._generate_team_id(team_start_course_date, team_shift)
        return Team(team_name, team_course_type, team_shift, team_start_course_date, team_finish_course_date, team_id)

    @staticmethod
    def _input_verify(team_course_type : str, team_shift: str):
        if team_shift not in ['MATUTINO', 'VESPERTINO', 'NOTURNO']:
            raise InvalidShift('Turno inválido! Escolha entre: MATUTINO, VESPERTINO e NOTURNO.')
        if team_course_type not in ['NORMAL', 'VIP']:
            raise InvalidCourseType('Tipo de curso inválido! Escolha entre: NORMAL e VIP.')

    @staticmethod
    def _generate_team_id(team_start_course_date : date, team_shift : str):
        if team_shift == 'MATUTINO':
            t_f = 0
        elif team_shift == 'VESPERTINO':
            t_f = 1
        else: #team_shift == 'NOTURNO'
            t_f = 2
        return int(f"{team_start_course_date.month}{team_start_course_date.year}{t_f}")

    @staticmethod
    def _generate_team_name(team_start_course_date : date, team_course_type : str, team_shift : str):
        month = DateTreatment.months[team_start_course_date.month-1].upper()
        return f"{month}_{team_start_course_date.year}_{team_course_type}_{team_shift}"

class StudentFactory:

    @classmethod
    def factory(cls, student_name : str, student_age : str, student_type_m : str,
                 student_is_graduated : bool, student_sit_pay_course : str):
        student_name = student_name.strip().upper()
        student_age = DateTreatment.convert_string_to_date(student_age)
        student_is_graduated = int(student_is_graduated)
        student_type_m = student_type_m.strip().upper()
        student_sit_pay_course = student_sit_pay_course.strip().upper()
        cls._input_verify(student_type_m, student_sit_pay_course)
        return Student(student_name, student_age, student_type_m, student_is_graduated, student_sit_pay_course)

    @staticmethod
    def _input_verify(student_type_m, student_st_pay_course):
        if student_type_m not in ['PASSARELA', 'LIMOUSINE', 'CIRCO']:
            raise InvalidModelType('Tipo de modelo inválido. Por favor escolha entre: PASSARELA, LIMOUSINE E CIRCO.')
        if student_st_pay_course not in ['PAGO', 'PENDENTE', 'ATRASADO']:
            raise InvalidPaymentStatus(
                'Situação do pagamento inválida. Por favor escolha entre: PAGO, PENDENTE E ATRASADO')


class Team:

    def __init__(self, name : str, course_type : str, shift: str, start_course_date : str, finish_course_date : date, team_id : int):
        self.start_course_date = start_course_date
        self.course_type = course_type
        self.shift = shift
        self.finish_course_date = finish_course_date
        self.name = name
        self.team_id = team_id


class Student:

    def __init__(self, name, age, type_m, is_graduated, sit_pay_course):
        self.name = name
        self.age = age
        self.type_m = type_m
        self.is_graduated = is_graduated
        self.sit_pay_curse = sit_pay_course
