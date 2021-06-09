from newsapi import NewsApiClient
import pprint
import requests
newsapi = NewsApiClient(api_key='55930f2b4f6f419bb78050fef47d3acd')
url = 'https://newsapi.org/v2/everything?'
parameters = {
    'q': 'big data', # query phrase
    'pageSize': 20,  # maximum is 100
    'apiKey': '55930f2b4f6f419bb78050fef47d3acd' # your own API key
}
response = requests.get(url, params=parameters)
response_json = response.json()
print(response_json)
print("Testing")