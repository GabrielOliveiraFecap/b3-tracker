import psycopg2
def conectar():
    return psycopg2.connect(
        host="localhost",
        dbname="b3_tracker",
        user="postgres",
        password="Carrocci$1010",
    )

def listar_tickers():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT ticker FROM carteira ORDER BY ticker;") 
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return [linha[0] for linha in resultado]



def adicionar_ticker(ticker):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO carteira(ticker) VALUES(%s);", (ticker,))
    conexao.commit()
    cursor.close()
    conexao.close()

def  remover_ticker(ticker):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM carteira WHERE ticker = %s;",(ticker,))
    conexao.commit()
    cursor.close()
    conexao.close()

print(listar_tickers())



