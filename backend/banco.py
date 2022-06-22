import sqlite3 # importa o módulo sqlite3
import os.path # importa o módulo os.path, para usar a exists()
import os      # importa o módulo os, para usar a unlink()

nome_banco = "boardgame"

if os.path.exists(nome_banco): # Exclui o arquivo caso ele exista
    os.unlink(nome_banco)

conexao = sqlite3.connect("boardgame") # Conecta no banco
cursor = conexao.cursor() # Obtém o cursor para o banco

consulta = """CREATE TABLE boardgame (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Informação sobre jogo TEXT,
    Como jogar TEXT,
    Idade indicada INTEGER,
    Preço REAL,
    )
    """
cursor.execute('boardgame') # Executa a consulta SQL
conexao.close() # Fecha a conexão com o banco