# Geo
from geopy import distance
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='pythonuser',
    password='salainen-sana',
    autocommit=True,
    collation='utf8mb3_general_ci'
)

def main():
    print("Lentokenttä 1 [ISAO]")
    sij_1 = input("> ")
    print("Lentokenttä 2 [ISAO]")
    sij_2 = input("> ")

    print(f"Kenttien välinen etäisyys: {int(mittaa(sij_1, sij_2).km)}km")

def mittaa(field_1, field_2):
    pos_1 = f"SELECT longitude_deg, latitude_deg from airport where ident='{field_1}'"
    pos_2 = f"SELECT longitude_deg, latitude_deg from airport where ident='{field_2}'"

    kursori = yhteys.cursor()
    
    kursori.execute(pos_1)
    pos_1 = kursori.fetchall()

    kursori.execute(pos_2)
    pos_2 = kursori.fetchall()


    return distance.distance(pos_1, pos_2)


main()