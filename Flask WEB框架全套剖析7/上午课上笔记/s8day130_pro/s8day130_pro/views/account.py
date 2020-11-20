from flask import blueprints
from s8day130_pro import models
from s8day130_pro import db
ac = blueprints.Blueprint('ac',__name__)

@ac.route('/login',methods=['GET','POST'])
def login():
    data = db.session.query(models.Users).all()
    print(data)
    db.session.remove()
    return 'Login'