import pymysql
import json
from Tests.Exceptions import DatabaseRegisterError

class DatabaseInitializer:
	"""
	Classe cuja unica função é: Quando instanciada, abrir uma conexão com o banco de dados específicado na __init__
	"""
	def __init__(self, database_info):
		self.conn = pymysql.connect(
			host=database_info['host'],
			user=database_info['user'],
			port=database_info['port'],
			passwd=database_info['password'],
			database=database_info['database']
			)
		self.cursor = self.conn.cursor()

	@staticmethod
	def get_database_info():
		try:
			with open('database_info.json', 'r') as json_file:
				database_info = json.load(json_file)
			json_file.close()
			return database_info
		except:
			return None

	@classmethod
	def registrate_database_info(cls, host='localhost', user='root', port=3306, password='', database=''):

		database_info = {'host': f'{host}', 'user': f'{user}', 'port': f'{port}',
						 'password': f'{password}', 'database': f'{database}'}

		with open('database_info.json', 'w') as json_file:
			json.dump(database_info, json_file)
		json_file.close()
		database_info = cls.get_database_info()
		if all(database_info):
			return database_info
		else:
			raise DatabaseRegisterError()

