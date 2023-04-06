"""Flask Application"""

# load libaries
from flask import Flask, jsonify
import warnings
import logging
from time import sleep
import os

# Load modules PF
from src.routes.index import blueprint_index
from src.routes.redirect import blueprint_redirect

# init Flask app
app = Flask(__name__)

# Configurations
warnings.filterwarnings("ignore")
logging.getLogger().setLevel(logging.INFO)
stage=os.environ.get('stage')

#For local execution
if not stage:
  logging.warning("Base path not found on ENV")
  stage='dev'

basepath=f"/"


# register blueprints. ensure that all paths are versioned!
app.register_blueprint(blueprint_index,name='blueprint_index', url_prefix=f"{basepath}")
app.register_blueprint(blueprint_redirect,name='blueprint_redirect', url_prefix=f"{basepath}")



##################
# Error Handlers
###################
def handle_internal_error(e):
  return jsonify({"message":'UNKNOWN_ERROR'}), 500

app.register_error_handler(500, handle_internal_error)