import sqlite3

nome_banco = "boardgame.db"
con = sqlite3.connect(nome_banco)
cur = con.cursor()
# id INTEGER, como jogar TEXT, idade INTEGER, preco REAL
Boardgame = [
    ('zombicide', 'RPG', 12, 400.00,),
    ('Dixit', 'Tabuleiro', 10 ,250.00,),
    ('Banco Imobiliario', 'Tabuleiro', 10, 80.00,),
    ('Cashn Guns','Tabuleiro',10, 215,00)
    ]
cur.executemany("INSERT INTO Boardgame VALUES (?,?,?,?)", Boardgame)

con.commit()
con.close()