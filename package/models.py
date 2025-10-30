from package import db

class user(db.Model) :
    id_user=db.Column(db.Integer,primary_key=True)
    nom_complet=db.Column(db.String(100),unique=True,nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    telephone=db.Column(db.String(10),unique=True,nullable=False)
    ville=db.Column(db.String(10),nullable=False)
    demande=db.relationship('demande',backref='damandeur',lazy=True)
    def __repr__(self):
        return f'({self.nom_complet},{self.email},{self.telephone},{self.ville})'
class domaine(db.Model):
    id_domaine=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(50),unique=True,nullable=False)
    demande=db.relationship('demande',backref='domaine',lazy=True)
    def __repr__(self):
        return f'({self.nom})'
class demande(db.Model):
    id_demande=db.Column(db.Integer,primary_key=True)
    type_stage=db.Column(db.String(50),nullable=False)
    duree=db.Column(db.Integer,nullable=False)
    date_debut=db.Column(db.Date,nullable=False)
    competence_cle=db.Column(db.Text,nullable=False)
    lettre_motivation=db.Column(db.Text,nullable=False)
    cv=db.Column(db.String(200),nullable=False)
    attestation_de_stage=db.Column(db.String(200),nullable=True)
    id_user=db.Column(db.Integer,db.ForeignKey('user.id_user'),nullable=False)
    id_domaine=db.Column(db.Integer,db.ForeignKey('domaine.id_domaine'),nullable=False)
    def __repr__(self):
        return f'({self.type_stage},{self.duree}moi,{self.date_debut},{self.competence_cle},{self.lettre_motivation},{self.domaine},{self.damandeur})'

