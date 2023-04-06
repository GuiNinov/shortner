from flask import Blueprint, jsonify, request, render_template,url_for
from src.Database.functions import log_shorturl
from time import sleep
# Modules
import config


# define the blueprint
blueprint_index = Blueprint(name="blueprint_index", import_name=__name__)


@blueprint_index.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        url = request.json['url']

        if not url:
            return jsonify({'token':None,'message':'Missing URL field','status':'error'}), 400

        logged_id = log_shorturl(url)
        short_url = request.host_url[:-1] + url_for('blueprint_index.index') + logged_id

        return jsonify({'url':short_url,'message':'Token Generated: Validity: 3 weeks','status':'Sucess'})

    return render_template('index.html')