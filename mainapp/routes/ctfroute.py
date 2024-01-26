from flask import request, Response, render_template, Blueprint

CTFapp = Blueprint('ctfapp', __name__,
                   static_folder='static',
                   static_url_path='/',
                   template_folder='templates')

CTFapp.route('/add', methods=['GET', 'POST'])