from App.Register import TeamRegister, StudentRegister

table_name = TeamRegister('VIP', 'NOTURNO', '06/04/2020').registrate()
StudentRegister(table_name, 'Thammer Giovanni', '25-07-1997', 'PASSARELA', False, 'PAGO').registrate_into_team()