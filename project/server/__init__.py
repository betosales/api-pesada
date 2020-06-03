# -*- coding: utf-8 -*-
import os
import random

from flask import Flask, url_for, request
from flask_cors import CORS

from flask import jsonify, make_response

from .dicts import basket, fruits

app = Flask(__name__, static_folder=os.path.abspath('project/static'))
# app._static_folder = 'static'
CORS(app)


@app.route('/')
@app.route('/basket/')
def index():
    response_object = {
        'status': 'success',
        'message': 'Deu certo, você conseguiu entrar',
        'basket': basket,
        'fruits': url_for('get_fruits')
    }
    return make_response(jsonify(response_object)), 200


@app.route('/fruits/')
@app.route('/fruits/<fruit>')
def get_fruits(fruit=None):
    f = [f.update({'uri': url_for('get_fruits', fruit=f['name'])}) for f in fruits]
    _fruits = [f['name'] for f in fruits]
    if fruit:
        fruit = fruit.lower()
        if fruit in _fruits:
            response_object = {
                'status': 'success',
                'fruits': [f for f in fruits if f['name'] == fruit]
            }
        else:
            response_object = {
                'status': 'fail',
                'message': f'This fruit <{fruit}> does not exists.'
            }
            return make_response(jsonify(response_object)), 404
    else:
        response_object = {
            'status': 'success',
            'fruits': fruits
        }
    return make_response(jsonify(response_object)), 200

@app.route('/webhook/dummy', methods=['POST'])
def webhook_dummy():
    print(f'o retorno foi: {request.data}')
    return request.data