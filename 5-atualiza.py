import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor  = conexao.cursor()

# 2 - Atualizar dados
id = 1
cursor.execute(
    """
        UPDATE filmes SET nome = ?
        WHERE id = ?
    """,
    ("Shang shi", id)
)

conexao.commit()

print("Dados Atualizados")