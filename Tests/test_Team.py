from App.DateTreatment import DateTreatment
from unittest import TestCase


class TeamTester(TestCase):

    def setUp(self):
        self.start_course = DateTreatment.convert_string_to_date('17-03-2020')

    def test_generate_team_id(self):
        self.assertEqual(32020, int(f"{self.start_course.month}{self.start_course.year}"))

    def test_create_name(self):
        month = DateTreatment.months[self.start_course.month-1].upper()
        self.assertEqual('MARÇO 2020 - NORMAL - DIURNO', f"{month} {self.start_course.year} - NORMAL - DIURNO")
