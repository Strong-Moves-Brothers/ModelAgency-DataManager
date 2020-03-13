from App.DateTreatment import DateTreatment
from datetime import date
from Tests.Exceptions import InvalidModelType, InvalidCourseType, InvalidShift, InvalidPaymentStatus


class TeamFactory:
    """
    This class contains the methods responsible for the manufacture of a Team object.
    """
    @classmethod
    def factory(cls, team_course_type : str, team_shift: str, team_start_course_date : str):
        """
        This method receive the basic team/course information and returns a Team object built based on the
        specified parameters.
        :param team_course_type: It is the type of course this team will do: Normal or VIP.
        :param team_shift: The shift that the classes should happen.
        :param team_start_course_date: The starting date of this team course.
        :return: A Team object.
        """
        team_start_course_date = DateTreatment.convert_string_to_date(team_start_course_date)
        team_course_type = team_course_type.strip().upper()
        team_shift = team_shift.strip().upper()
        cls._input_verify(team_course_type, team_shift)
        team_finish_course_date = DateTreatment.add_7_months(team_start_course_date)
        team_name = cls._generate_team_name(team_start_course_date, team_course_type, team_shift).strip().upper()
        team_id = cls._generate_team_id(team_start_course_date, team_shift)
        return Team(team_name, team_course_type, team_shift, team_start_course_date, team_finish_course_date, team_id)

    @staticmethod
    def _input_verify(team_course_type : str, team_shift: str):
        """
        This method is responsible for verifying if some inputs were gave correctly, and case not, stop the manufacture.
        """
        if team_shift not in ['MATUTINO', 'VESPERTINO', 'NOTURNO']:
            raise InvalidShift('Turno inválido! Escolha entre: MATUTINO, VESPERTINO e NOTURNO.')
        if team_course_type not in ['NORMAL', 'VIP']:
            raise InvalidCourseType('Tipo de curso inválido! Escolha entre: NORMAL e VIP.')

    @staticmethod
    def _generate_team_id(team_start_course_date : date, team_shift : str):
        """
        Generates an unique ID that for this specific team, based on the given parameters.
        :return: int -> ID
        """
        if team_shift == 'MATUTINO':
            t_f = 0
        elif team_shift == 'VESPERTINO':
            t_f = 1
        else: #team_shift == 'NOTURNO'
            t_f = 2
        return int(f"{team_start_course_date.month}{team_start_course_date.year}{t_f}")

    @staticmethod
    def _generate_team_name(team_start_course_date : date, team_course_type : str, team_shift : str):
        """
        Generates an unique name for this specific team, based on the given parameters.
        :return: str -> Team name
        """
        month = DateTreatment.months[team_start_course_date.month-1].upper()
        return f"{month}_{team_start_course_date.year}_{team_course_type}_{team_shift}"


class StudentFactory:
    """"
    This class contains the methods responsible for the manufacture of a Student object.
    """
    @classmethod
    def factory(cls, student_name : str, student_birth_date : str, student_model_type : str,
                 student_is_graduated : bool, student_sit_pay_course : str):
        """
        This method receive the basic team/course information and returns a Team object built based on the
        specified parameters.
        :param student_name: The student name.
        :param student_birth_date: The student birth-date.
        :param student_model_type: The type of model the student is.
        :param student_is_graduated: If the student is or not graduated yet.
        :param student_sit_pay_course: The payment situation.
        :return: A Student object.
        """
        student_name = student_name.strip().upper()
        student_birth_date = DateTreatment.convert_string_to_date(student_birth_date)
        student_is_graduated = int(student_is_graduated)
        student_model_type = student_model_type.strip().upper()
        student_sit_pay_course = student_sit_pay_course.strip().upper()
        cls._input_verify(student_model_type, student_sit_pay_course)
        return Student(student_name, student_birth_date, student_model_type,
                       student_is_graduated, student_sit_pay_course)

    @staticmethod
    def _input_verify(student_model_type, student_sit_pay_course):
        """
        This method is responsible for verifying if some inputs were gave correctly, and case not, stop the manufacture.
        """
        if student_model_type not in ['PASSARELA', 'LIMOUSINE', 'CIRCO']:
            raise InvalidModelType('Tipo de modelo inválido. Por favor escolha entre: PASSARELA, LIMOUSINE E CIRCO.')
        if student_sit_pay_course not in ['PAGO', 'PENDENTE', 'ATRASADO']:
            raise InvalidPaymentStatus(
                'Situação do pagamento inválida. Por favor escolha entre: PAGO, PENDENTE E ATRASADO')


class Team:
    """
    This class contains the basic attributes of a Team object and is capable of instantiate one.
    """
    def __init__(self, name : str, course_type : str, shift: str, start_course_date : str,
                 finish_course_date : date, team_id : date):
        """
        Instantiates a Team object.
        :param name: The Team's name.
        :param course_type: It is the type of course this team will do: Normal or VIP.
        :param shift: The shift that the classes should happen.
        :param start_course_date: The starting date of this team course.
        :param finish_course_date: The finishing date of this team course.
        :param team_id: This team ID.
        """
        self.start_course_date = start_course_date
        self.course_type = course_type
        self.shift = shift
        self.finish_course_date = finish_course_date
        self.name = name
        self.team_id = team_id


class Student:
    """
    This class contains the basic attributes of a Student object and is capable of intantiate one.
    """
    def __init__(self, name, birth_date, model_type, is_graduated, sit_pay_course):
        """
        Instantiates a Student object.
        :param name: The student name.
        :param birth_date: The student birth-date.
        :param model_type: The type of model the student is.
        :param is_graduated: If the student is or not graduated yet.
        :param sit_pay_course: The payment situation.
        """
        self.name = name
        self.birth_date = birth_date
        self.model_type = model_type
        self.is_graduated = is_graduated
        self.sit_pay_curse = sit_pay_course
