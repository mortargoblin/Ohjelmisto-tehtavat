from flask import Flask, request, Response
import mysql.connector
import json

app = Flask(__name__)
@app.route("/kentta/<icao>")



def get_airport(icao):
    yhteys = mysql.connector.connect (
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='pythonuser',
        password='salainen-sana',
        autocommit=True,
        collation='utf8mb3_general_ci'
    )
    kursori = yhteys.cursor(dictionary=True)
    try:
        tilakoodi = 200
        kursori.execute(
            f"SELECT ident AS ICAO, " 
            f"name AS Name, "
            f"municipality AS Municipality "
            f"FROM airport "
            f"WHERE ident='{icao}'"
        )
        vastaus = kursori.fetchone()
    except Exception as e:
        vastaus = e
#    return str(vastaus)
    return Response(
        response=json.dumps(vastaus), 
        status=tilakoodi, 
        mimetype="application/json"
    )

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": 404,
        "description": "Improper endpoint"
    }

    return Response(response=json.dumps(vastaus), status=404, mimetype="application/json")

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
