import sqlite3

nome_banco = "boardgame"
con = sqlite3.connect(nome_banco)
cur = con.cursor()
# id INTEGER, como jogar TEXT, idade INTEGER, preco REAL
Jogos = [
    (None, 'zombicide', 'RPG', 12,  400.00,)
    (None, 'Dixit', "Tabuleiro", 10 ,250.00,)
    (None, 'Banco Imobiliario', "Tabuleiro", 10,  80.00,)
    ]

cur.executemany("INSERT INTO Boardgame VALUES (?, ?, ?, ?, ?)", boardgame)

con.commit()
con.close()