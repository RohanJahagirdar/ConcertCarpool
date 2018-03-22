import json

from flask import Flask, request, jsonify, render_template
import pymongo
import requests

app = Flask(__name__)


@app.route('/')
def browse():
    return render_template("/index.html")


@app.route('/test/')
def test():
    send_url = 'http://freegeoip.net/json/'
    r = requests.get(send_url)
    j = json.loads(r.text)
    print(j)
    return 'Hello World Again!'


@app.route('/register', methods=['get'])
def register():
    email = (request.args.get('email'))
    password = (request.args.get('password'))
    return jsonify({'summary': email, "password" : password})


@app.route('/search', methods=['get'])
def search():
    pickup = (request.get('pickup'))
    destination = (request.args.get('destination'))
    session = (request.args.get('session'))
    pickup_date = (request.args.get('pickup_date'))
    pickup_time = (request.args.get('pickup_time'))
    return_date = (request.args.get('return_date'))
    return_time = (request.args.get('return_time'))
    return jsonify({'summary': "Done!!"})


@app.route('/book', methods=['get'])
def book():
    trip_id = (request.args.get('trip_id'))
    session = (request.args.get('session'))
    return jsonify({'summary': "Sent notification to driver. In review!!"})


@app.route('/db')
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.get_database("ConcertCapool")
    con = db.get_collection("Concerts")
    #ind =


    #return jsonify({'summary': ind})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
    app.run(debug=True)


