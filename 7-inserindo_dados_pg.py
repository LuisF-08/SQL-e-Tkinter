from conexao_post import conn

cursor_obj = conn.cursor()

games = [
    ('The Last os US', '2014', 9.9),
    ('God of War', '2018', 9.8),
    ('GTA V', '2013', 9.7),
    ('Red Dead Redemption II', '2018', 9.6),
    ('The Witcher 3: Wild Hunt', '2015', 9.5),
    ('Spider Man 2', '2023', 9.2),
        ]
for game in games:
    cursor_obj.execute(
        """INSERT INTO games(name,year,score)
        VALUES (%s, %s, %s)
        """,game
        )
    
conn.commit()
print("Dados inseridos com sucesso")
conn.close()
