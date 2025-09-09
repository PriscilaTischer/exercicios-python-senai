import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='aula_pratica_1'

)

cursor= conexao.cursor()



#comando = f'select * from cliente'
comando = f'insert into cliente (nome, cpf, endereco, cidade, numero) values ("sakura", "811.811.811-10", "rua folha", "piracicaba", "23")'

cursor.execute(comando)
conexao.commit()

#resultado = cursor.fetchall()

#print(resultado)

#for cliente in resultado:
#  print(cliente)

conexao.close()
