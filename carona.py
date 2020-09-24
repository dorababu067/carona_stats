import json
import requests
from colorama import Fore
import pandas as pd

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "345f529b75msh54ef897a76821c9p1ebb47jsn761311f759a8"
    }

response = requests.request("GET", url, headers=headers)
print(Fore.GREEN + str(response.status_code))
print(Fore.RESET)

# data = json.loads(response.text)
# df = pd.DataFrame(data)
# print(df)
