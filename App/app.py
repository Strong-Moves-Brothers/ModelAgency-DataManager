from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from App.Team import TeamFactory, StudentFactory
from App.Register import TeamRegister, StudentRegister
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from App.Initializer import DatabaseInitializer
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button


class Manager(ScreenManager):
    pass


class DatabaseRegisterMenu(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainMenu(Screen):

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)


class TeamRegisterMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.items = TeamFactory.available_values

    def team_register(self):

        if App.get_running_app().has_database():

            self.register = TeamRegister(App.get_running_app().database)
            team = TeamFactory.factory(self.ids.courseTypeInput.text, self.ids.courseShiftInput.text,
                                       self.ids.courseStartDateInput.text)
            self.register.registrate(team)
            del self.register
            self.update()

        else:

            def go(*args):
                App.get_running_app().root.current = 'databaseRegisterMenu'

            box = BoxLayout(orientation='vertical')
            pop = Popup(title='Nenhum banco de dados cadastrado', content=box)

            label = Label(text='Deseja cadastrar?')
            box.add_widget(label)

            box2 = BoxLayout()
            sim = Button(text='Sim', on_press=go, on_release=pop.dismiss)
            nao = Button(text='Não', on_press=pop.dismiss)
            box2.add_widget(sim)
            box2.add_widget(nao)

            box.add_widget(box2)

            pop.open()

    def get_items_course_type(self):
        return self.items['course_type']

    def get_items_course_shift(self):
        return self.items['course_shift']

    def update(self, *args):

        self.ids.courseStartDateInput.text = ''

        self.ids.courseTypeInput.values = self.get_items_course_type()
        self.ids.courseTypeInput.text = self.ids.courseTypeInput.values[0]

        self.ids.courseShiftInput.values = self.get_items_course_shift()
        self.ids.courseShiftInput.text = self.ids.courseShiftInput.values[0]


class StudentRegisterMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.generate_cache()
        except:
            pass
        self.items = StudentFactory.available_values

    def student_register(self):

        if App.get_running_app().has_database():
            student = StudentFactory.factory(self.ids.nameInput.text, self.ids.birthDateInput.text, self.ids.modelTypeInput.text,
                                          self.ids.isGraduatedInput.text, self.ids.paymentSituationInput.text)
            register = StudentRegister(App.get_running_app().database)
            register.registrate(student, self.ids.teamNameInput.text)
            self.update()
        else:
            def go(*args):
                App.get_running_app().root.current = 'databaseRegisterMenu'

            box = BoxLayout(orientation='vertical')
            pop = Popup(title='Nenhum banco de dados cadastrado', content=box)

            label = Label(text='Deseja cadastrar?')
            box.add_widget(label)

            box2 = BoxLayout()
            sim = Button(text= 'Sim', on_press=go, on_release=pop.dismiss)
            nao = Button(text='Não', on_press=pop.dismiss)
            box2.add_widget(sim)
            box2.add_widget(nao)

            box.add_widget(box2)

            pop.open()

    def generate_cache(self):
        register = StudentRegister(App.get_running_app().database)
        register.database.cursor.execute('SHOW TABLES;')
        tables = register.database.cursor.fetchall()
        cache = []
        if not tables:
            cache.append('NENHUM TIME CADASTRADO')
        for tupla in tables:
            for team_name in tupla:
                cache.append(team_name)
        self.cache = cache

    def get_team_names(self):

        if hasattr(App.get_running_app(), 'database'):
            return self.cache
        else:
            team_names = ['']

        return team_names

    def get_items_model_type(self):
        return self.items['model_type']

    def get_items_is_graduated(self):
        return self.items['is_graduated']

    def get_items_payment_situation(self):
        return self.items['sit_pay_course']

    def update(self, *args):

        if hasattr(App.get_running_app(), 'database'):
            self.generate_cache()

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


class DateInput(TextInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def insert_text(self, substring, from_undo=False):
        if len(self.text) == 2:
            t = f'/{substring}'
        elif len(self.text) == 5 and self.text.count('/') == 1:
            t = f'/{substring}'
        else:
            t = substring

        return super(DateInput, self).insert_text(t, from_undo=from_undo)


class ModelAgencyDataManagerApp(App):

    database_info = DatabaseInitializer.get_database_info()

    def build(self):
        try:
            self.database = DatabaseInitializer(self.database_info)
        except:
            pass

        return Manager()

    @classmethod
    def has_database(cls):
        if hasattr(App.get_running_app(), 'database'):
            return True
        else:
            return False

    def _call_database_register(self, host, user, port, password, database):
        if not port:
            self.database_info = DatabaseInitializer.registrate_database_info(host=host, user=user, password=password,
                                                                              database=database)
        else:
            self.database_info = DatabaseInitializer.registrate_database_info(host, user, port, password, database)
        self.database = DatabaseInitializer(App.get_running_app().database_info)

    def exit(self):
        self.database.cursor.close()
        self.database.conn.close()
        self.stop()


if __name__ == '__main__':
    ModelAgencyDataManagerApp().run()