from flask import render_template,url_for,jsonify,request,flash,redirect
from werkzeug.utils import secure_filename
import uuid
import os
from package import app,db
from package.models import user,demande,domaine
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    try:
        # 1️⃣ Récupération des données
        nom = request.form.get('nom')
        email = request.form.get('email')
        telephone = request.form.get('telephone')
        ville = request.form.get('ville')

        domaine_stage = request.form.get('domaine_stage')
        type_stage = request.form.get('type_stage')
        duree = request.form.get('duree')
        date_debut = request.form.get('date_debut')
        competences = request.form.get('competences')
        motivation = request.form.get('motivation')

        # 2️⃣ Récupération des fichiers
        cv = request.files.get('cv')
        attestation = request.files.get('attestation')

        cv_path, attestation_path = None, None

        # 3️⃣ Vérification utilisateur existant
        user1 = user.query.filter_by(nom_complet=nom).first()
        user2 = user.query.filter_by(email=email).first()
        user3 = user.query.filter_by(telephone=telephone).first()

        if user1 or user2 or user3:
            print("✅ Insertion non  réussie, flash exécuté !")
            flash("Erreur : utilisateur déjà existant ou contrainte violée !", "danger")
            return redirect(url_for('home'))

        # 4️⃣ Création d’un nouvel utilisateur
        user1 = user(nom_complet=nom, email=email, telephone=telephone, ville=ville)
        db.session.add(user1)
        db.session.flush()

        # 5️⃣ Domaine : insérer seulement s’il n’existe pas
        domaine1 = domaine.query.filter_by(nom=domaine_stage).first()
        if not domaine1:
            domaine1 = domaine(nom=domaine_stage)
            db.session.add(domaine1)
            db.session.flush()

        # 6️⃣ Sauvegarde des fichiers
        if cv:
            
            original_filename = cv.filename
            unique_filename = f"{uuid.uuid4().hex}_{secure_filename(original_filename)}"
            cv_path = os.path.join(UPLOAD_FOLDER, unique_filename)
            cv.save(cv_path)

        if attestation:
            
            original_filename = attestation.filename
            unique_filename = f"{uuid.uuid4().hex}_{secure_filename(original_filename)}"
            attestation_path = os.path.join(UPLOAD_FOLDER, unique_filename)
            attestation.save(attestation_path)

        # 7️⃣ Création de la demande
        demande1 = demande(
            type_stage=type_stage,
            duree=duree,
            date_debut=date_debut,
            competence_cle=competences,
            lettre_motivation=motivation,
            cv=cv_path,
            attestation_de_stage=attestation_path,
            id_user=user1.id_user,
            id_domaine=domaine1.id_domaine
        )
        db.session.add(demande1)
        db.session.commit()

        
        flash("Votre demande de stage a été enregistrée avec succès.", "success")
        return redirect(url_for('home'))

    except Exception as e:
        db.session.rollback()
        flash(f"Erreur lors de la soumission : {str(e)}", "danger")
        return redirect(url_for('home'))



