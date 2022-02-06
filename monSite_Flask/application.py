
from flask import *
import sqlite3
 
# Création d'un objet application web Flask
app = Flask(__name__, static_url_path='/static')

# Fonctions utilisées pour appeler des commandes SQL
def lire_base():
    """ Récupere des images dans la table
        Renvoie (list of tuples) : liste des images
    """
    connexion = sqlite3.connect("base/database_meme.db")
    curseur = connexion.cursor()
    requete_sql = """
    SELECT *
    FROM images
    ORDER BY Catégorie;"""
    resultat = curseur.execute(requete_sql)
    images = resultat.fetchall() 
    # On recupere les images on les mets sous forme de tuple
    connexion.close()
    return images

def lire_video():
    """ Récupére des vidéos dawns la table
        Renvoie (list of tuples) : liste des vidéos
    """
    connexion = sqlite3.connect("base/database_meme.db")
    curseur = connexion.cursor()
    requete_sql = """
    SELECT *
    FROM vidéos
    ORDER BY Catégorie;"""
    resultat = curseur.execute(requete_sql)
    videos = resultat.fetchall() 
    # On recupere les vidéos on les mets sous forme de tuple
    connexion.close()
    return videos
"""
def index_max():
     Récupére l'id du prochain enregistrement
        Renvoie un entier
    
    connexion = sqlite3.connect("bdd/database_meme.db")
    curseur = connexion.cursor()
    requete_sql = 
    
    3SELECT MAX(Id)
    FROM images;
    resultat = curseur.execute(requete_sql)
    index = resultat.fetchall()
    connexion.close()
    return int(index[0][0])+1 # Transtype le résultat de la recherche et ajoute 1
"""
"""
def ajoute_enregistrement(indice, donnees):
     Créé l'enregistrement avec le nouvel id et les données saisies
        Renvoire un booléen : True si l'ajout a bien fonctionné
    
    # Test si tous les champs sont renseignés
    parametre0 = donnees['Titre']
    parametre1 = donnees['Lien']
    parametre2 = donnees['Catégorie']
    parametre3 = donnees['Uploader']
    if parametre0 == "" or parametre1 == "" or parametre2 == "" or parametre3== "":
        return False
    parametres = (indice, parametre0, parametre1, parametre2, parametre3)
    connexion = sqlite3.connect("bdd/base_CNRS.db")
    curseur = connexion.cursor()
    requete_sql = 
    INSERT INTO images (Titre, Lien, Catégorie, Uploader') 
    VALUES (?,?,?,?);
    resultat = curseur.execute(requete_sql, parametres)
    connexion.commit()
    connexion.close()
    return True
"""
# Création d'une fonction accueillir() associee a l'URL "/"
# pour générer une page web dynamique
@app.route("/home")
def accueillir():
    """Présentation du site"""
    return render_template("accueil.html")

# Page utilisant une base de données
@app.route("/images")
def lire_complete():
    # Récupération des personnes de la base de données SQLite
    mdr = lire_base() 
    # Transmission pour affichage
    return render_template("images.html",memes=mdr)

@app.route("/vidéos")
def lire_base_vieos():
    # Récupération des personnes de la base de données SQLite
    rdm = lire_video()
    # Transmission pour affichage
    return render_template("videos.html",drole=rdm)

@app.route("/saisir")
def saisie_ligne():
    """ Ouvre le formulaire pour demander les champs nécessaires à la création d'un enregistrement
    """
    return render_template("saisie.html")

@app.route("/saisir", methods = ['POST'])
def valide_saisie():
    result = request.form # Récupération des informations en provenance du POST: C'est un dictionnaire
    
    ajoute_enregistrement(result)  # Créé l'enregistrement avec le nouvel id et les données saisies
    mdr = lire_base() # Interroge la base pour récupérer la liste des labos avant de l'afficher
    return render_template("lecture.html", memes=mdr)
"""
@app.route("/saisir", methods = ['POST'])
def valide_saisie():
    result = request.form # Récupération des informations en provenance du POST: C'est un dictionnaire
    index = index_max()
    ajoute_enregistrement(index, result)  # Créé l'enregistrement avec le nouvel id et les données saisies
    labos = lire_base() # Interroge la base pour récupérer la liste des labos avant de l'afficher
    return render_template("lecture.html", labos=labos)
"""

# Lancement de l'application web et son serveur
# accessible à l'URL : http://127.0.0.1:1664/home
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, debug=True)