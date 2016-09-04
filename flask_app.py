from flask import Flask
from flask import render_template
from Battles import Battles
from flask import jsonify
from flask import request
import logging

log = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def GOT():
    return render_template("index.html")

@app.route('/list', methods = ['GET', 'POST'])
def get_all_battles():
    return jsonify(result = Battles.get_all_battles())

@app.route('/count', methods = ['GET', 'POST'])
def get_count():
    return jsonify(count = Battles.get_number_of_batles())

@app.route('/stats', methods = ['GET', 'POST'])
def get_stats():
    return jsonify(result = Battles.get_battles_stats())

@app.route('/search', methods = ['GET', 'POST'])
def search():
    query_map = {}
    if request.method == 'GET':
        query_map['name'] = request.args.get('name')
        query_map['attacker_king'] = request.args.get('attacker_king')
        query_map['defender_king'] = request.args.get('defender_king')
        query_map['battle_type'] = request.args.get('battle_type')
        query_map['location'] = request.args.get('location')

    if request.method == "POST":
        query_map['name'] = request.form.get('name')
        query_map['attacker_king'] = request.form.get('attacker_king')
        query_map['defender_king'] = request.form.get('defender_king')
        query_map['battle_type'] = request.form.get('battle_type')
        query_map['location'] = request.form.get('location')

    return jsonify(result = query_map)

    return jsonify(result = Battles.search_battles(query_map))






