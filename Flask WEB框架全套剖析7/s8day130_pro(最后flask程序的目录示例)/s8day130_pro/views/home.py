from flask import blueprints,render_template
from s8day130_pro import models
from s8day130_pro import db
hm = blueprints.Blueprint('hm',__name__)

@hm.route('/index')
def index():
    return render_template('index.html')