from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from bdd_operations import get_all_films, get_film_by_id, create_film
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}  # Extensions de fichiers autorisées


# Fonctions pour gérer la base de données

# ...

# Route pour la page d'accueil
@app.route('/')
def index():
    films = get_all_films()
    return render_template('index.html', films=films)


# Route pour les détails d'un film
@app.route('/film/<int:film_id>')
def film_details(film_id):
    film = get_film_by_id(film_id)
    return render_template('film_details.html', film=film)


# Route pour ajouter un nouveau film
@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter_film():
    if request.method == 'POST':
        titre = request.form['titre']
        description = request.form['description']
        annee = request.form['annee']
        acteurs = request.form['acteurs']
        realisation = request.form['realisation']
        producteur = request.form['producteur']
        image_upload = request.files['image_upload']

        if image_upload and allowed_file(image_upload.filename):
            # L'utilisateur a téléchargé une image avec une extension autorisée
            filename = secure_filename(image_upload.filename)
            image_upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image = filename
        else:
            # Aucune image n'a été téléchargée ou l'extension du fichier n'est pas autorisée
            image = None

        # Effectuer les autres opérations pour ajouter le film à la base de données
        create_film(titre, description, annee, acteurs, realisation, producteur, image)

        return redirect('/')
    else:
        return render_template('ajouter_film.html')


# Route pour servir les fichiers téléchargés
@app.route('/uploads/<filename>')
def serve_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


if __name__ == '__main__':
    app.run()
