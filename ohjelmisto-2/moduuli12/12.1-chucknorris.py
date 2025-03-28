# Chuck Norris -ohjelma

import requests
import json

print(requests.get("https://api.chucknorris.io/jokes/random").json()["value"])
