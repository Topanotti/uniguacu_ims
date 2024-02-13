import pymysql

# Conectar ao banco de dados MySQL
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
)

# Criar o cursor
cursor = connection.cursor()

# Executar a query para criar o banco de dados
cursor.execute("CREATE DATABASE IF NOT EXISTS uniguacu_ims")

# Fechar a conexão
connection.close()

print("Database criado com sucesso!")