from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson.json_util import dumps
import json

app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas
app.config["MONGO_URI"] = "mongodb+srv://mariagmenr:laravel8@cluster0.u0z54ln.mongodb.net/Educalumnos"
mongo = PyMongo(app)

@app.route('/add_score', methods=['POST'])
def add_score():
    data = request.get_json()
    print(data)
    name = data['Nombre']
    score = data['Puntuaje']
    mongo.db.jugadores.insert_one({'Nombre': name, 'Puntuaje': score})
    return jsonify(message="Score added successfully"), 201

@app.route('/top_scores', methods=['GET'])
def get_top_scores():
    top_scores = list(mongo.db.jugadores.find().sort('Puntuaje', -1).limit(5))
    for score in top_scores:
        score['_id'] = str(score['_id'])  # Convertir ObjectId a string
    return jsonify(top_scores), 200


if __name__ == "__main__":
    app.run(debug=True)