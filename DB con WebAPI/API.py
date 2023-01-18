
import json
import sqlite3
from flask import Flask, jsonify


# Funzione che restituisce la lista dei percorsi:
def get_percorsi(cursor):
    cursor.execute('''SELECT id, nome FROM Percorso''')
    percorsi = cursor.fetchall()
    return [{"id": percorso[0], "nome": percorso[1]} for percorso in percorsi]


# Funzione che restituisce i dettagli di un percorso:
def get_percorso(id, cursor):
    cursor.execute('''SELECT id, nome FROM Percorso WHERE id = ?''', (id,))
    percorso = cursor.fetchone()
    mossa = cursor.execute('''SELECT codPercorso, posizione, codMovimento, tempo FROM Mossa WHERE codPercorso = ?''', (id,))
    mossa = cursor.fetchall()
    return {"id": percorso[0], "nome": percorso[1], "mossa": mossa}


app = Flask(__name__)
# Restituisce il JSON con tutti i percorsi
@app.route("/api/v1/percorsi")
def ListaPercorsi(): 
    # Mi connetto a SQL 
    conn = sqlite3.connect('Percorsi.db')
    cursor = conn.cursor()
    # Eseguo query
    percorsi = get_percorsi(cursor)
    temp = jsonify(percorsi)
    # Chiudo connessione a SQL
    conn.close()
    return temp

# Restituisce il JSON con i dettagli del percorso indicato nell'URL
@app.route("/api/v1/percorsi/<id>")
def DettagliPercorso(id):
    conn = sqlite3.connect('Percorsi.db')
    cursor = conn.cursor()
    percorso = get_percorso(id, cursor) 
    temp= jsonify(percorso) 
    conn.close()
    return temp


def main():
    app.run()

if __name__ == "__main__":
    main()










