from App.Initializer import DatabaseInitializer

class Register(DatabaseInitializer):

    def __init__(self, database: str, table: str):
        super().__init__()
        self.database = database
        self.table = table


    def registrate_into_team(self, student):
        insert_dt = f"INSERT INTO Student_db (name, age, type_m, is_graduated, sit_pay_curse, start_curse, " \
                    f"finish_curse) VALUES ('{student.name}','{student.age}','{student.type_m}'," \
                    f"'{student.is_graduated}','{student.sit_pay_curse}','{student.start_curse}'," \
                    f"'{student.finish_curse}')"

        self.cursor.execute(insert_dt)
        self.conexao.commit()
        print(self.cursor.rowcount, f"add to data base {self.database} on table {self.table}")


class Creator(DatabaseInitializer):

    def __init__(self):
        super().__init__()

    def create_table(self, team):
        insert_dt = f"CREATE TABLE {team.name} (name VARCHAR(255), age DATE, type_m VARCHAR(255), " \
                    f"is_graduated BOOLEAN, sit_pay_curse VARCHAR(255), start_curse DATE, " \
                    f"finish_curse DATE);"
        self.cursor.execute(insert_dt)
        self.conexao.commit()
