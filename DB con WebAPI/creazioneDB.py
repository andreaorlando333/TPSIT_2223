# Script che CREA il database e lo popola
# Nota: eseguire SOLO UNA VOLTA

import sqlite3
conn = sqlite3.connect('Percorsi.db')
cursor = conn.cursor()

# Creo le tabelle necessarie
cursor.execute('''CREATE TABLE Percorso (id INTEGER PRIMARY KEY, nome TEXT)''')

cursor.execute('''CREATE TABLE Mossa (codPercorso INTEGER, posizione INTEGER, 
                                       codMovimento INTEGER, tempo INTEGER, 
                                       PRIMARY KEY (codPercorso, posizione))''')

cursor.execute('''CREATE TABLE Movimento (id INTEGER PRIMARY KEY, nome TEXT)''')


# Inserisco dati nella tabella Percorso
cursor.execute("INSERT INTO Percorso VALUES (1, 'Percorso 1')")
cursor.execute("INSERT INTO Percorso VALUES (2, 'Percorso 2')")
cursor.execute("INSERT INTO Percorso VALUES (3, 'Percorso 3')")

# Inserisco dati nella tabella Mossa
cursor.execute("INSERT INTO Mossa VALUES (1, 1, 1, 10)")
cursor.execute("INSERT INTO Mossa VALUES (1, 2, 2, 20)")
cursor.execute("INSERT INTO Mossa VALUES (1, 3, 3, 30)")
cursor.execute("INSERT INTO Mossa VALUES (2, 1, 2, 40)")
cursor.execute("INSERT INTO Mossa VALUES (2, 2, 3, 50)")
cursor.execute("INSERT INTO Mossa VALUES (3, 1, 1, 60)")
cursor.execute("INSERT INTO Mossa VALUES (3, 3, 3, 30)")

# Inserisco dati nella tabella Movimento
cursor.execute("INSERT INTO Movimento VALUES (0, 'AVANTI')")
cursor.execute("INSERT INTO Movimento VALUES (1, 'INDIETRO')")
cursor.execute("INSERT INTO Movimento VALUES (2, 'DESTRA')")
cursor.execute("INSERT INTO Movimento VALUES (3, 'SINISTRA')")

# Salvo le modifiche e chiudo
conn.commit()
conn.close()

