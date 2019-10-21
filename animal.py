from flask import Flask
from flask.views import MethodView
from requests import session

app = Flask(__name__)

class Animal(MethodView):
    def get(self):
        return 'Returned an animal'

    def post(self):
        return ' Created an animal'

    def put(self):
        return 'Modified an animal'


    def delete(self):
        return 'Deleted an animal'

app.add_url_rule('/animal', view_func=Animal.as_view('animal'))
app.run




    
