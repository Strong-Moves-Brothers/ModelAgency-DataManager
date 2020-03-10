from App.DateTreatment import DateTreatment
from datetime import date


class Team:

    def __init__(self, name : str, course_type : str, shift: str, start_course_date : str, finish_course_date : date, team_id : int):
        self.start_course_date = start_course_date
        self.course_type = course_type
        self.shift = shift
        self.finish_course_date = finish_course_date
        self.name = name
        self.team_id = team_id


class Student:

    def __init__(self, name, age, type_m, is_graduated, sit_pay_course):
        self.name = name
        self.age = age
        self.type_m = type_m
        self.is_graduated = is_graduated
        self.sit_pay_curse = sit_pay_course
