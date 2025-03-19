## Lentokentat

def main():
    import mysql.connector

    yhteys = mysql.connector.connect (
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='pythonuser',
        password='salainen-sana',
        autocommit=True,
        collation='utf8mb3_general_ci'
    )
    
    
    print("Anna maan tunniste (esim. FI)")
    tunniste = input("> ")
    kentat = hae_lento(yhteys, tunniste)

    try:
        print(kentat[5][0])
        print(f"pienet lentokentät: {kentat[0]}, keskikokoiset lentokentät: {kentat[1]}, suuret lentokentät: {kentat[2]}")
        print(f"helikopterien kentät: {kentat[3]}, muut: {kentat[4]}")
    except TypeError:
        print("Tunnisteella ei löytynyt mitään")

def hae_lento(yhteys, tunniste):
    sql = f"SELECT type FROM airport where iso_country='{tunniste}'"
    sql_nimi = f"SELECT name FROM country where iso_country='{tunniste}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    kursori.execute(sql_nimi)
    tulos_nimi = kursori.fetchone()


    # muuttujat lentokenttien laskemiseen
    small = 0
    medium = 0
    large = 0
    heli = 0
    muut = 0

    # for loop laskee kenttien määrän
    for airport in tulos:
        if airport[0] == "small_airport":
            small += 1
        elif airport[0] == "medium_airport":
            medium += 1
        elif airport[0] == "large_airport":
            large += 1
        elif airport[0] == "heliport":
            heli += 1
        else:
            muut += 1
        
    if kursori.rowcount >0:
        return small, medium, large, heli, muut, tulos_nimi
    else:
        return None

main()
