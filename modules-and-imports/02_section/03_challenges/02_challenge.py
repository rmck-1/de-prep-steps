# ADD YOUR IMPORTS HERE

import requests
import json

#r = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
# PLEASE DO NOT MAKE CHANGES BELOW THIS LINE

def get_simpsons_quote():
    r = requests.get("https://official-joke-api.appspot.com/random_joke")

    body = json.loads(r.content)#[0]
    print(body)

    return f"{body['setup']}: {body['punchline']}"


print(get_simpsons_quote())
