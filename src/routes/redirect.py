# Libs
from flask import Blueprint, jsonify, request,redirect,url_for,render_template

# Modules
from src.Database.functions import retrieve_url



# define the blueprint
blueprint_redirect = Blueprint(name="blueprint_redirect", import_name=__name__)




@blueprint_redirect.route('/<id>')
def url_redirect(id):
    if id:
        original_url= retrieve_url(id)
        if not original_url:
            return redirect(url_for('blueprint_index.index'))
        return redirect(original_url)
    else:
        return redirect(url_for('blueprint_index.index'))

