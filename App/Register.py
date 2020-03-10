from App.Initializer import DatabaseInitializer
from App.Team import Team, Student
from App.DateTreatment import DateTreatment
from datetime import date
from Tests.Exceptions import InvalidShift, InvalidCourseType, InvalidModelType, InvalidPaymentStatus


class StudentRegister(DatabaseInitializer):

    def __init__(self, table_name: str, student_name : str, student_age : str, student_type_m : str,
                 student_is_graduated : bool, student_sit_pay_course : str):
        super().__init__()
        student_name = student_name.strip().upper()
        student_age = DateTreatment.convert_string_to_date(student_age)
        student_is_graduated = int(student_is_graduated)
        student_type_m = student_type_m.strip().upper()
        student_sit_pay_course = student_sit_pay_course.strip().upper()
        self.input_verify(student_type_m, student_sit_pay_course)

        self.table = table_name
        self.student = Student(student_name, student_age, student_type_m, student_is_graduated, student_sit_pay_course)

    @staticmethod
    def input_verify(student_type_m, student_st_pay_course):
        if student_type_m not in ['PASSARELA', 'LIMOUSINE', 'CIRCO']:
            raise InvalidModelType('Tipo de modelo inválido. Por favor escolha entre: PASSARELA, LIMOUSINE E CIRCO.')
        if student_st_pay_course not in ['PAGO', 'PENDENTE', 'ATRASADO']:
            raise InvalidPaymentStatus('Situação do pagamento inválida. Por favor escolha entre: PAGO, PENDENTE E ATRASADO')



    def registrate_into_team(self):
        insert_dt = f"INSERT INTO {self.table} (name, age, type_m, is_graduated, sit_pay_curse" \
                    f") VALUES ('{self.student.name}', '{self.student.age}', '{self.student.type_m}'," \
                    f" '{self.student.is_graduated}', '{self.student.sit_pay_curse}')"
        print(insert_dt)
        self.cursor.execute(insert_dt)
        self.conexao.commit()
        self.conexao.close()


class TeamRegister(DatabaseInitializer):

    def __init__(self, team_course_type : str, team_shift: str, team_start_course_date : str):
        super().__init__()
        team_start_course_date = DateTreatment.convert_string_to_date(team_start_course_date)
        team_course_type = team_course_type.strip().upper()
        team_shift = team_shift.strip().upper()
        self.input_verify(team_course_type, team_shift)
        team_finish_course_date = DateTreatment.add_7_years(team_start_course_date)
        team_name = self.generate_team_name(team_start_course_date, team_course_type, team_shift).strip().upper()
        team_id = self.generate_team_id(team_start_course_date, team_shift)
        self.team = Team(team_name, team_course_type, team_shift, team_start_course_date, team_finish_course_date, team_id)


    @staticmethod
    def input_verify(team_course_type : str, team_shift: str):
        if team_shift not in ['MATUTINO', 'VESPERTINO', 'NOTURNO']:
            raise InvalidShift('Turno inválido! Escolha entre: MATUTINO, VESPERTINO e NOTURNO.')
        if team_course_type not in ['NORMAL', 'VIP']:
            raise InvalidCourseType('Tipo de curso inválido! Escolha entre: NORMAL e VIP.')

    def registrate(self):
        insert_dt = f"CREATE TABLE {self.team.name} (user_id SMALLINT PRIMARY KEY AUTO_INCREMENT, " \
                    f"name VARCHAR(255), age DATE, type_m VARCHAR(255), " \
                    f"is_graduated BOOL, sit_pay_curse VARCHAR(255), start_course DATE " \
                    f"DEFAULT '{self.team.start_course_date}', finish_course DATE DEFAULT " \
                    f"'{self.team.finish_course_date}', team_id INT DEFAULT '{self.team.team_id}');"
        print(insert_dt)
        self.cursor.execute(insert_dt)
        self.conexao.commit()
        self.conexao.close()
        return self.team.name

    @staticmethod
    def generate_team_id(team_start_course_date : date, team_shift : str):
        if team_shift == 'MATUTINO':
            t_f = 0
        elif team_shift == 'VESPERTINO':
            t_f = 1
        else: #team_shift == 'NOTURNO'
            t_f = 2
        return int(f"{team_start_course_date.month}{team_start_course_date.year}{t_f}")

    @staticmethod
    def generate_team_name(team_start_course_date : date, team_course_type : str, team_shift : str):
        month = DateTreatment.months[team_start_course_date.month-1].upper()
        return f"{month}_{team_start_course_date.year}_{team_course_type}_{team_shift}"
