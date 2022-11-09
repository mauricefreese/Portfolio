# Maurrice Freese
# Project: ECON312 Data Science Tools Project 11/2022
# API Key - {REDACTED}

import requests
import json

#API Request for daily BTC  prices
url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY&apikey={REDACTED}'
r = requests.get(url)
data = r.json()
pretty_json = json.loads(r.text)


#writing json file
# a - append x - create r - read w - write
with open("btcusd.json", "x") as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data)


# Turns API pull into a data frame
'''
data = response.text
data_dict = json.loads(data)

df = pd.DataFrame(data_dict)
print(df)
'''
# converts json output of API to csv to being cleaning
'''
with open('btcusd.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('btcusd.csv', encoding='utf-8', index=False)
'''

