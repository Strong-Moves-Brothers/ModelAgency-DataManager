from App.Initializer import DatabaseInitializer
from App.Team import Team, Student
from App.DateTreatment import DateTreatment
from datetime import date
from Tests.Exceptions import InvalidShift, InvalidCourseType, InvalidModelType, InvalidPaymentStatus


class StudentRegister(DatabaseInitializer):

    def __init__(self, table : str):
        super().__init__()
        self._table = table

    def registrate(self, student):
        insert_dt = f"INSERT INTO {self._table} (name, age, type_m, is_graduated, sit_pay_curse" \
                    f") VALUES ('{student.name}', '{student.age}', '{student.type_m}'," \
                    f" '{student.is_graduated}', '{student.sit_pay_curse}')"
        print(insert_dt)
        self.cursor.execute(insert_dt)
        self.conexao.commit()
        self.conexao.close()


class TeamRegister(DatabaseInitializer):

    def __init__(self):
        super().__init__()

    def registrate(self, team):
        insert_dt = f"CREATE TABLE {team.name} (user_id SMALLINT PRIMARY KEY AUTO_INCREMENT, " \
                    f"name VARCHAR(255), age DATE, type_m VARCHAR(255), " \
                    f"is_graduated BOOL, sit_pay_curse VARCHAR(255), start_course DATE " \
                    f"DEFAULT '{team.start_course_date}', finish_course DATE DEFAULT " \
                    f"'{team.finish_course_date}', team_id INT DEFAULT '{team.team_id}');"
        print(insert_dt)
        self.cursor.execute(insert_dt)
        self.conexao.commit()
        self.conexao.close()
        return team.name
