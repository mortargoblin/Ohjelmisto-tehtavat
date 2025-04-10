from flask import Flask, request, Response
import mysql.connector
import json

app = Flask(__name__)
@app.route("/alkuluku/<num>")

yhteys = mysql.connector.connect (
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='pythonuser',
    autocommit=True,
    collation='utf8mb3_general_ci'
)

def prime_num_check(num):
    try:
        num = int(num)
        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "number": num, 
            "isPrime": None}
        for i in range(2, num -1):
            if num % i == 0:
                vastaus["isPrime"] = False
                break
        if vastaus["isPrime"] == None:
            vastaus["isPrime"] = True

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "description": "Improper number"}
    return Response(
        response=json.dumps(vastaus), 
        status=tilakoodi, 
        mimetype="application/json"
    )

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": 404,
        "description": "Improper endpoint"}

    return Response(response=json.dumps(vastaus), status=404, mimetype="application/json")

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
