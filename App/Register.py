from App.Initializer import DatabaseInitializer
from Tests.Exceptions import TableRegisterError


class StudentRegister:
    """
    This class contains the methods responsible for register an student in a specific Team Table
    """
    def __init__(self, database : DatabaseInitializer):
        """
        This method instantiates a StudentRegister object and initializes the database connection
        """
        self.database = database

    def registrate(self, student, table):
        """
        This method is responsible for registrating the given student into the table specified by the
        table parameter of the object
        :param student: A Student object
        :param table: It's the team/table name
        """
        insert_dt = f"INSERT INTO {table} (name, birth_date, model_type, is_graduated, sit_pay_curse" \
                    f") VALUES ('{student.name}', '{student.birth_date}', '{student.model_type}'," \
                    f" '{student.is_graduated}', '{student.sit_pay_curse}')"
        print(insert_dt)
        self.database.cursor.execute(insert_dt)
        self.database.conn.commit()


class TeamRegister:
    """
    This class contains the methods responsible for registrating a team by creating a table based on it's parameters.
    """
    def __init__(self, database : DatabaseInitializer):
        """
        This method instantiates an TeamRegister object and initializes the database connection
        """
        self.database = database

    def registrate(self, team):
        """
        This method is responsible for creating a table in the database, based on the team parameters.
        :param team: A Team object
        """
        insert_dt = f"CREATE TABLE {team.name} (user_id SMALLINT PRIMARY KEY AUTO_INCREMENT, " \
                    f"name VARCHAR(255), birth_date DATE, model_type VARCHAR(255), " \
                    f"is_graduated BOOL, sit_pay_curse VARCHAR(255), start_course_date DATE " \
                    f"DEFAULT '{team.course_start_date}', finish_course_date DATE DEFAULT " \
                    f"'{team.course_finish_date}');"
        print(insert_dt)
        try:
            self.database.cursor.execute(insert_dt)
            print(insert_dt)
        except:
            self.database.conn.commit()
            self.database.conn.close()
            raise TableRegisterError()
        self.database.conn.commit()
