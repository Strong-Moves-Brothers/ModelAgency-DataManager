from App.DateTreatment import DateTreatment


class Team:

    def __init__(self, course_type : str, shift: str, start_course: str):
        self.start_course = DateTreatment.convert_string_to_date(start_course)
        self.course_type = course_type.strip().upper()
        self.shift = shift.strip().upper()
        self.finish_course = DateTreatment.add_7_years(self.start_course)
        self.name = self.create_name()
        self.team_id = self.generate_team_id()

    def generate_team_id(self):
        return int(f"{self.start_course.month}{self.start_course.year}")

    def create_name(self):
        month = DateTreatment.months[self.start_course.month].upper()
        return f"{month} {self.start_course.year} - {self.course_type} - {self.shift}"


class Student:

    def __init__(self, name, age, type_m, is_graduated, sit_pay_course, team_id):
        self.name = name.strip().upper()
        self.age = age
        self.type_m = type_m.strip().upper()
        self.is_graduated = is_graduated
        self.sit_pay_curse = sit_pay_course.strip().upper()
        self.team_id = team_id
