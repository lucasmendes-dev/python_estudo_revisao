import mysql.connector
from mysql.connector import Error

banco = {
    "host": "localhost",
    "db": "testes",
    "user": "root",
    "password": ""
}

try:

    connection = mysql.connector.connect(host=banco["host"],
                                         database=banco["db"],
                                         user=banco["user"],
                                         password=banco["password"]
                                         )
    if connection.is_connected():
        cursor = connection.cursor()

        query = "UPDATE pessoa SET nome = 'Cleiton' WHERE id = 2;"

        cursor.execute(query)
        connection.commit()  #serve para casos de create


except Error as e:
    print("Erro na conexao", e)


finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão com banco encerrada.")
