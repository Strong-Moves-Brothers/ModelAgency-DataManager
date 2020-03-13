from App.DateTreatment import DateTreatment
from datetime import date
from Tests.Exceptions import InvalidModelType, InvalidCourseType, InvalidShift, InvalidPaymentStatus


class TeamFactory:
    """
    This class contains the methods responsible for the manufacture of a Team object.
    """
    available_values = {'course_type': ['NORMAL', 'VIP'], 'course_shift': ['MATUTINO', 'VESPERTINO', 'NOTURNO']}
    @classmethod
    def factory(cls, course_type : str, course_shift: str, course_start_date : str):
        """
        This method receive the basic team/course information and returns a Team object built based on the
        specified parameters.
        :param team_course_type: It is the type of course this team will do: Normal or VIP.
        :param team_shift: The shift that the classes should happen.
        :param team_start_course_date: The starting date of this team course.
        :return: A Team object.
        """
        team_start_course_date = DateTreatment.convert_string_to_date(course_start_date)
        team_course_type = course_type.strip().upper()
        team_shift = course_shift.strip().upper()
        cls._input_verify(team_course_type, team_shift)
        team_finish_course_date = DateTreatment.add_7_months(team_start_course_date)
        team_name = cls._generate_team_name(team_start_course_date, team_course_type, team_shift).strip().upper()
        return Team(team_name, team_course_type, team_shift, team_start_course_date, team_finish_course_date)

    @classmethod
    def _input_verify(cls, course_type : str, course_shift: str):
        """
        This method is responsible for verifying if some inputs were gave correctly, and case not, stop the manufacture.
        """
        if course_shift not in cls.available_values['course_shift']:
            raise InvalidShift('Turno inválido!')
        if course_type not in cls.available_values['course_type']:
            raise InvalidCourseType('Tipo de curso inválido!')

    @staticmethod
    def _generate_team_name(course_start_date : date, course_type : str, course_shift : str):
        """
        Generates an unique name for this specific team, based on the given parameters.
        :return: str -> Team name
        """
        month = DateTreatment.months[course_start_date.month-1].upper()
        return f"{month}_{course_start_date.year}_{course_type}_{course_shift}"


class StudentFactory:
    available_values = {'model_type': ['PASSARELA', 'LIMOUSINE', 'CIRCO'], 'is_graduated': ['SIM', 'NÃO'],
                        'sit_pay_course': ['PAGO', 'PENDENTE', 'ATRASADO']}
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
        student_model_type = student_model_type.strip().upper()
        student_sit_pay_course = student_sit_pay_course.strip().upper()
        cls._input_verify(student_model_type, student_sit_pay_course, student_is_graduated)
        student_is_graduated = int(cls._graduated_input_verify(student_is_graduated))
        return Student(student_name, student_birth_date, student_model_type,
                       student_is_graduated, student_sit_pay_course)

    @classmethod
    def _input_verify(cls, student_model_type, student_sit_pay_course, student_is_graduated):
        """
        This method is responsible for verifying if some inputs were gave correctly, and case not, stop the manufacture.
        """
        if student_model_type not in cls.available_values['model_type']:
            raise InvalidModelType('Tipo de modelo inválido.')
        if student_sit_pay_course not in cls.available_values['sit_pay_course']:
            raise InvalidPaymentStatus('Situação do pagamento inválida.')
        if student_is_graduated not in cls.available_values['is_graduated']:
            raise ValueError('Status de graduação inválido.')

    @staticmethod
    def _graduated_input_verify(student_is_graduated):
        if student_is_graduated == 'NÃO':
            student_is_graduated = 0
        elif student_is_graduated == 'SIM':
            student_is_graduated = 1
        return student_is_graduated


class Team:
    """
    This class contains the basic attributes of a Team object and is capable of instantiate one.
    """
    def __init__(self, name : str, course_type : str, course_shift: str, course_start_date : date, course_finish_date : date):
        """
        Instantiates a Team object.
        :param name: The Team's name.
        :param course_type: It is the type of course this team will do: Normal or VIP.
        :param shift: The shift that the classes should happen.
        :param start_course_date: The starting date of this team course.
        :param finish_course_date: The finishing date of this team course.
        :param team_id: This team ID.
        """
        self.course_start_date = course_start_date
        self.course_type = course_type
        self.course_shift = course_shift
        self.course_finish_date = course_finish_date
        self.name = name


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
