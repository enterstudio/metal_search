from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse

from search import search_apmex
from search import search_provident
from search import search_shinybars
from search import search_goldeneaglecoins
from search import search_silvertowne
from search import search_gainesvillecoins


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('query', type=str, required=True, help='Query string to submit to search functions')


class Apmex(Resource):
    def post(self):
        args = parser.parse_args()
        return search_apmex(args['query'])


class Provident(Resource):
    def post(self):
        args = parser.parse_args()
        return search_provident(args['query'])


class Shinybars(Resource):
    def post(self):
        args = parser.parse_args()
        return search_shinybars(args['query'])


class Golden(Resource):
    def post(self):
        args = parser.parse_args()
        return search_goldeneaglecoins(args['query'])


class Silvertowne(Resource):
    def post(self):
        args = parser.parse_args()
        return search_silvertowne(args['query'])


class Gainesville(Resource):
    def post(self):
        args = parser.parse_args()
        return search_gainesvillecoins(args['query'])


api.add_resource(Apmex, '/api/apmex')
api.add_resource(Provident, '/api/provident')
api.add_resource(Shinybars, '/api/shinybars')
api.add_resource(Golden, '/api/goldeneagle')
api.add_resource(Silvertowne, '/api/silvertowne')
api.add_resource(Gainesville, '/api/gainesville')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api')
def api_page():
    return render_template('api.html')


if __name__ == '__main__':
    app.run(debug=True)

