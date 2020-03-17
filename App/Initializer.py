import pymysql

class DatabaseInitializer:
	"""
	Classe cuja unica função é: Quando instanciada, abrir uma conexão com o banco de dados específicado na __init__
	"""
	def __init__(self, host, user, passwd, database):
		self.conexao = pymysql.connect(
			host=host,
			user=user,
			passwd=passwd,
			database=database
			)
		self.cursor = self.conexao.cursor()