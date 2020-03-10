from App.Register import TeamRegister, StudentRegister
from App.Team import TeamFactory, StudentFactory

def on_press1():
    team = TeamFactory.factory('VIP', 'NOTURNO', '06/04/2020')
    TeamRegister().registrate(team)
    return team.name

def on_press2(table):
    student = StudentFactory.factory('Thammer Giovanni', '25-07-1997', 'PASSARELA', False, 'PAGO')
    return StudentRegister(table).registrate(student)

table = on_press1()
on_press2(table)