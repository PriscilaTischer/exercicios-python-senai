import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ideb_bd',

)
cursor= conexao.cursor()


comando =  f"SELECT * FROM ideb WHERE anos_escolares = 'finais (6-9)';"
cursor.execute(comando)

resultado = cursor.fetchall()


print(resultado)

for ideb in resultado:
   print(ideb)

conexao.close()

