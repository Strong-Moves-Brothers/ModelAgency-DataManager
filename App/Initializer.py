import pymysql

class DatabaseInitializer:
	"""
	Classe cuja unica função é: Quando instanciada, abrir uma conexão com o banco de dados específicado na __init__
	"""
	def __init__(self):
		self.conexao = pymysql.connect(
			host="localhost",
			user="sora",
			passwd="senha123",
			database="class_db"
			)
		self.cursor = self.conexao.cursor()