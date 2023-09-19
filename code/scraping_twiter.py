import requests
import pandas as pd
import json

twitter_data = []

payload = {
    'api_key':"937e372e9757d4d3e11aa5529df3a8a3",
    'query':'artificial intelligence',
    'num':100
}

response = requests.get(
    "https://api.scraperapi.com/structured/twitter/search/tweets",
    params=payload
)

data = response.json()

print(data)