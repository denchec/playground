import playground

from flask import Flask
from flask_restful import Api, Resource, reqparse
import psycopg2
from psycopg2 import Error

app = Flask(__name__)
api = Api(app)


class Query(object):
	def __init__(self, id, information, status):
		self.id = id
		self.information = information
		self.status = status

	def insert(self):
		try:
			connection = psycopg2.connect(user = "postgres",
									  	password = "1234",
									 	host = "localhost",
									 	port = "5432",
									 	database = "MessageDB")

			cursor = connection.cursor()

			insert_query = "INSERT INTO message (id, information, status) VALUES (%s, %s, %s)"
			arguments = [self.id, self.information, self.status]
			cursor.execute(insert_query, arguments)
			connection.commit()
			print("Вставили запись")

		except (Exception, Error) as error:
			print("Ошибка при работе с PostgreSQL", error)

		finally:
			if connection:
				cursor.close()
				connection.close()
			print("Соединение с PostgreSQL закрыто")
	
	def update(id, status):
		try:
			connection = psycopg2.connect(user = "postgres",
									password = "1234",
									host = "localhost",
									port = "5432",
									database = "MessageDB")

			cursor = connection.cursor()

			update_query = "UPDATE message set status = %s where id values %s"
			arguments = [self.status, self.id]
			cursor.execute(update_query, arguments)
			connection.commit()
			count = cursor.rowcount
			print(count, "Запись успешно изменена")

		except (Exception, Error) as error:
			print("Ошибка при работе с PostgreSQL", error)

		finally:
			if connection:
				cursor.close()
				connection.close()
			print("Соединение с PostgreSQL закрыто")


def listner(text):
	text.split(" ")

	for i in text:
		if i.lower() == "абракадабра":
			return False

	return True

if __name__ == "__main__":
	listner()
