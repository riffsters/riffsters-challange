"""
Define App routes
"""
from flask import Flask
import yaml
from .app import App

APP_API = Flask(__name__)
APP = App()
with open("app/config.yml", 'r') as ymlfile:
    CFG = yaml.load(ymlfile)


@APP_API.route('/secret', methods=['GET'])
def secret_fetcher():
    """
    Secret route
    """
    secret = APP.fetch_secret(CFG['secret']['table_name'], CFG['secret']['key'])
    return secret


@APP_API.route('/health', methods=['GET'])
def health():
    """
    Health check route
    """
    healt_check = APP.health_check(CFG['health_check']['container'], \
                          CFG['health_check']['project'])
    return healt_check
