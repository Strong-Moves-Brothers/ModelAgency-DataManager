from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from App.Team import TeamFactory, StudentFactory
from App.Register import TeamRegister,StudentRegister


class Manager(ScreenManager):
    pass


class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TeamRegisterMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def team_register(self):
        team = TeamFactory.factory(self.ids.courseTypeInput.text, self.ids.courseShiftInput.text, self.ids.startCourseDateInput.text)
        TeamRegister().registrate(team)


class StudentRegisterMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def student_register(self):
        team = StudentFactory.factory(self.ids.nameInput.text, self.ids.birthDateInput.text, self.ids.modelTypeInput.text,
                                      self.ids.isGraduatedInput.text, self.ids.paymentSituationInput.text)
        StudentRegister(self.ids.teamNameInput.text).registrate(team)


class MyApp(App):

    def build(self):
        return Manager()


if __name__ == '__main__':
    MyApp().run()