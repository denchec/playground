from psycopg2 import Error
import psycopg2


class Query:
    def __init__(self, data=None):
        self.data = data

    def update_token(self):
        # Добавляем нового пользователя в базу данных
        try:
            connection, cursor = self.connect_to_db()

            wb_token = self.data['wb_token']
            wb_refresh_token = self.data['wb_refresh_token']
            supplier_name = self.data['supplier_name']

            insert_query = f"UPDATE wb_client_accounts " \
                           f"SET wb_token = %s, wb_refresh_token = %s " \
                           f"WHERE name = %s"

            cursor.execute(insert_query, [wb_token, wb_refresh_token, supplier_name])
            connection.commit()

            print(f"Заменили токены в БД для {supplier_name}")

            session_close(connection, cursor)

        except (Exception, Error) as error:
            session_close(connection, cursor)
            print("Ошибка при работе с PostgreSQL", error)

    def get_client_info(self):
        try:
            connection, cursor = self.connect_to_db()

            update_query = f"SELECT name, supplier_id, wb_token, wb_refresh_token FROM wb_client_accounts"
            cursor.execute(update_query)

            records = cursor.fetchall()
            print("Данные получены")

            session_close(connection, cursor)

            client_accounts = list()
            for record in records:

                client_accounts.append({
                    'name': record[0],
                    'supplier_id': record[1],
                    'wb_token': record[2],
                    'wb_refresh_token': record[3],
                })

            return client_accounts

        except (Exception, Error) as error:
            session_close(connection, cursor)
            print("Ошибка при работе с PostgreSQL", error)

    @staticmethod
    def connect_to_db():
        # Подключаемся к базе данных
        connection = psycopg2.connect(user="postgres",
                                      password="1234",  # postgres
                                      host="127.0.0.1",
                                      port="5432",
                                      database="monitoring_app")

        print("Соединение с PostgreSQL открыто")

        cursor = connection.cursor()

        return connection, cursor


def session_close(connection, cursor):
    # Закрываем соединение с базой данных
    if connection:
        cursor.close()
        connection.close()
    print("Соединение с PostgreSQL закрыто")
