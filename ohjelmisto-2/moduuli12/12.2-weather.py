# Weather.py

import json
import requests


def main():
    key = str(open("/home/coy/.config/rp-avain/weather", "r").read()).strip()
    #key = oma avain tähän
    city = input("Anna kaupunki\n> ")
    for item in api_call(key, city):
        print(item)

def api_call(key, city):
    request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?"
    f"lang=fi&q={city}&appid={key}&units=metric").json()
    #json.dumps(request.json(), indent=2)
    return (request["weather"][0]["main"], request["main"]["temp"])

if __name__ == "__main__":
    main()
