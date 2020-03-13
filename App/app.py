from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from App.Team import TeamFactory, StudentFactory
from App.Register import TeamRegister, StudentRegister


class Manager(ScreenManager):
    pass


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TeamRegisterMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register = TeamRegister()
        self.items = TeamFactory.available_values

    def team_register(self):
        team = TeamFactory.factory(self.ids.courseTypeInput.text, self.ids.courseShiftInput.text,
                                   self.ids.courseStartDateInput.text)
        TeamRegister().registrate(team)

        self.update()

    def get_items_course_type(self):
        return self.items['course_type']

    def get_items_course_shift(self):
        return self.items['course_shift']

    def update(self, *args):
        try:
            self.register.conexao.close()
        except:
            pass
        finally:
            self.register = TeamRegister()

            self.ids.courseStartDateInput.text = ''

            self.ids.courseTypeInput.values = self.get_items_course_type()
            self.ids.courseTypeInput.text = self.ids.courseTypeInput.values[0]

            self.ids.courseShiftInput.values = self.get_items_course_shift()
            self.ids.courseShiftInput.text = self.ids.courseShiftInput.values[0]


class StudentRegisterMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register = StudentRegister()
        self.items = StudentFactory.available_values

    def student_register(self):
        print(self.ids.birthDateInput, self.ids.birthDateInput.text)
        team = StudentFactory.factory(self.ids.nameInput.text, self.ids.birthDateInput.text, self.ids.modelTypeInput.text,
                                      self.ids.isGraduatedInput.text, self.ids.paymentSituationInput.text)
        self.register.registrate(team, self.ids.teamNameInput.text)

        self.update()

    def get_team_names(self):

        self.register.cursor.execute('SHOW TABLES;')
        tables = self.register.cursor.fetchall()
        if not tables:
            return ['NENHUM TIME CADASTRADO']
        team_names = []
        for tupla in tables:
            for team_name in tupla:
                team_names.append(team_name)
        return team_names

    def get_items_model_type(self):
        return self.items['model_type']

    def get_items_is_graduated(self):
        return self.items['is_graduated']

    def get_items_payment_situation(self):
        return self.items['sit_pay_course']

    def update(self, *args):
        try:
            self.register.conexao.close()
        except:
            pass
        finally:
            self.register = StudentRegister()

            self.ids.nameInput.text = ''

            self.ids.birthDateInput.text = ''

            self.ids.modelTypeInput.values = self.get_items_model_type()
            self.ids.modelTypeInput.text = self.ids.modelTypeInput.values[0]

            self.ids.isGraduatedInput.values = self.get_items_is_graduated()
            self.ids.isGraduatedInput.text = self.ids.isGraduatedInput.values[0]

            self.ids.paymentSituationInput.values = self.get_items_payment_situation()
            self.ids.paymentSituationInput.text = self.ids.paymentSituationInput.values[0]

            self.ids.teamNameInput.values = self.get_team_names()
            self.ids.teamNameInput.text = self.ids.teamNameInput.values[0]


class MyApp(App):

    def build(self):
        return Manager()


if __name__ == '__main__':
    MyApp().run()