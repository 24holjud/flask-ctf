from flask import Flask

def create_app():
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='')
    
    from .routes.ctfroute import ctfapp as ctf_blueprint

    app.register_blueprint(ctf_blueprint, url_prefix='ctf')