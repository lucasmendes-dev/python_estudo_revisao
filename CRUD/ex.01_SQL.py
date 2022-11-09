import pandas as pd
import sqlite3

conexao = sqlite3.connect('../salarios.sqlite')

query = "SELECT * FROM Salaries;"
tabela_salarios = pd.read_sql(query, conexao)

#forma diferente de usar o WHERE -- pandas
# var_tabela.loc[var_tabela["Coluna"] == "String", nº da linha]
tabela = tabela_salarios.loc[tabela_salarios["Agency"] == "San Francisco", :]
#print(tabela)

#groupby -- pandas
# var_tabela.groupby("Coluna").ação()
tabela_media = tabela_salarios.groupby("Year").mean()

#print(tabela_media[["TotalPay", "TotalPayBenefits"]])


tabela_qte = tabela_salarios.groupby("Year").count()
tabela_qte = tabela_qte[["Id"]]
print(tabela_qte)



conexao.close()

