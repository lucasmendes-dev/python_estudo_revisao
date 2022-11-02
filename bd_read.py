import mysql.connector
from mysql.connector import Error

banco = {
    "host": "localhost",
    "db": "financas",
    "user": "root",
    "password": "Easy976020-1"
}

try:

    connection = mysql.connector.connect(host=banco["host"],
                                         database=banco["db"],
                                         user=banco["user"],
                                         password=banco["password"]
                                         )
    if connection.is_connected():
        cursor = connection.cursor()

        query = "Select * from pessoa;"
        cursor.execute(query)
        # connection.commit()  #serve para casos de create

        dado = cursor.fetchall()




except Error as e:
    print("Erro na conexao", e)


finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão com banco encerrada.")
