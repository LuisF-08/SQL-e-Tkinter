import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Inserindo Dados
cursor.execute(
    """
        INSERT INTO filmes(nome,ano,nota)
        VALUES('It a coisa', 2018, 9.0)
    """
)
conexao.commit()
conexao.close()
print('Dados inseridos na tabela')