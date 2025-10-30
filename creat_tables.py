from package import app, db
from package.models import user,demande,domaine

with app.app_context():
     user1=user.query.all()
     print(user1)
     demande1=demande.query.all()
     print(demande1)
     domaine1=domaine.query.all()
     print(domaine1)