import pymysql

class DatabaseInitializer:
	def __init__(self):
		self.conexao = pymysql.connect(
			host="localhost",
			user="root",
			passwd="",
			database="class_db"
			)
		self.cursor = self.conexao.cursor()