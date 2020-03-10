import pymysql

class DatabaseInitializer:
	def __init__(self):
		self.conexao = pymysql.connect(
			host="localhost",
			user="sora",
			passwd="senha123",
			database="class_db"
			)
		self.cursor = self.conexao.cursor()