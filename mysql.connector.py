import mysql.connector
from mysql.connector import Error

banco = {
    "host": "localhost",
    "db": "financas",
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

        query = "Select * from teste;"
        cursor.execute(query)
        # connection.commit()  #serve para casos de create

        dado = cursor.fetchall()


        # coluna = cursor.description  #pega o nome das colunas do Banco
        # nome = [nome[0] for nome in coluna] #ideia de LIST COMPREHENSION




except Error as e:
    print("Erro na conexao", e)


finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão com banco encerrada.")
