import json

from flask import Flask, request, jsonify, render_template
import requests

from app.Utils.DynamoDB import DynamoDB

app = Flask(__name__)
dynamoDB = DynamoDB()

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


@app.route('/register', methods=['post'])
def register():
    email = (request.form.get('email'))
    password = (request.form.get('password'))
    response = dynamoDB.putUser(email, password)

    #return jsonify({'summary': email, "password" : password})
    return render_template("/browse.html")


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




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
    app.run(debug=True)


