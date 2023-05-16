import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('films.db')
cursor = conn.cursor()

# Création de la table 'films'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS films (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT NOT NULL,
        description TEXT,
        annee INTEGER,
        acteurs TEXT,
        realisation TEXT,
        producteur TEXT,
        image TEXT
    )
''')

# Fermeture de la connexion à la base de données
conn.close()
