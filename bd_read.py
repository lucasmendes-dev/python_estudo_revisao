import mysql.connector
from mysql.connector import Error
import pandas as pd

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

        query = "Select * from pessoa;"
        cursor.execute(query)
        # connection.commit()  #serve para casos de create

        valores = cursor.fetchall()   #fetchall armazena dados em uma lista de tuplas

        descricao = cursor.description
        colunas = [nome[0] for nome in descricao]  # ideia de LIST COMPREHENSION

        tabela = pd.DataFrame.from_records(valores, columns=colunas)  #ideia do display no Jupyter

        print(tabela)


except Error as e:
    print("Erro na conexao", e)


finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão com banco encerrada.")
