import sqlite3


def insert_films():
    conn = sqlite3.connect('films.db')
    cursor = conn.cursor()

    films = [
        {
            'titre': 'Film 1',
            'description': 'Description du film 1',
            'annee': 2021,
            'acteurs': 'Acteur 1, Acteur 2',
            'realisation': 'Réalisateur 1',
            'producteur': 'Producteur 1',
            'image': 'https://exemple.com/affiche_film1.jpg'
        },
        {
            'titre': 'Film 2',
            'description': 'Description du film 2',
            'annee': 2022,
            'acteurs': 'Acteur 1, Acteur 3',
            'realisation': 'Réalisateur 2',
            'producteur': 'Producteur 2',
            'image': 'https://exemple.com/affiche_film2.jpg'
        },
        {
            'titre': 'Film 3',
            'description': 'Description du film 3',
            'annee': 2023,
            'acteurs': 'Acteur 2, Acteur 3',
            'realisation': 'Réalisateur 3',
            'producteur': 'Producteur 3',
            'image': 'https://exemple.com/affiche_film3.jpg'
        }
    ]

    for film in films:
        cursor.execute(
            'INSERT INTO films (titre, description, annee, acteurs, realisation, producteur, image) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (
            film['titre'], film['description'], film['annee'], film['acteurs'], film['realisation'], film['producteur'],
            film['image']))

    conn.commit()
    conn.close()

def update_image_urls(new_url):
    conn = sqlite3.connect('films.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE films SET image = ?', (new_url,))

    conn.commit()
    conn.close()


# Appel de la fonction pour insérer les films
insert_films()

# Appel de la fonction pour mettre à jour les URL des images
new_image_url = 'example.jpg'
update_image_urls(new_image_url)