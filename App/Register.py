from App.Initializer import DatabaseInitializer


class StudentRegister(DatabaseInitializer):
    """
    This class contains the methods responsible for register an student in a specific Team Table
    """
    def __init__(self, table : str):
        """
        This method instantiates an StudentRegister object and initializes the database connection
        :param table: It's the team/table name
        """
        super().__init__()
        self._table = table

    def registrate(self, student):
        """
        This method is responsible for registrating the given student into the table specified by the
        table parameter of the object
        :param student: A Student object
        """
        insert_dt = f"INSERT INTO {self._table} (name, birth_date, model_type, is_graduated, sit_pay_curse" \
                    f") VALUES ('{student.name}', '{student.birth_date}', '{student.model_type}'," \
                    f" '{student.is_graduated}', '{student.sit_pay_curse}')"
        print(insert_dt)
        self.cursor.execute(insert_dt)
        self.conexao.commit()
        self.conexao.close()


class TeamRegister(DatabaseInitializer):
    """
    This class contains the methods responsible for registrating a team by creating a table based on it's parameters.
    """
    def __init__(self):
        """
        This method instantiates an TeamRegister object and initializes the database connection
        """
        super().__init__()

    def registrate(self, team):
        """
        This method is responsible for creating a table in the database, based on the team parameters.
        :param team: A Team object
        """
        insert_dt = f"CREATE TABLE {team.name} (user_id SMALLINT PRIMARY KEY AUTO_INCREMENT, " \
                    f"name VARCHAR(255), birth_date DATE, model_type VARCHAR(255), " \
                    f"is_graduated BOOL, sit_pay_curse VARCHAR(255), start_course_date DATE " \
                    f"DEFAULT '{team.start_course_date}', finish_course_date DATE DEFAULT " \
                    f"'{team.finish_course_date}');"
        print(insert_dt)
        self.cursor.execute(insert_dt)
        self.conexao.commit()
        self.conexao.close()
