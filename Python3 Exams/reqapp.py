import requests
import json


api_url = "http://api.exchangeratesapi.io/v1/latest?access_key=bdda33f54fe5d4c9b2b48ffbe2297865&format="
bozulan_doviz = input('bozulan doviz türü: ')
alınan_doviz = input('alınan doviz türü: ')

miktar = int(input(f'Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: '))


result = requests.get(api_url+bozulan_doviz)

result = json.loads(result.text)
print(result)