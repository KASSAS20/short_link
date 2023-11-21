# получение KEY:     https://rapidapi.com/BigLobster/api/url-shortener-service/

import requests
from key import KEY

url = "https://url-shortener-service.p.rapidapi.com/shorten"

site = input("Введите ссылку: ")
site = site.replace('https://', '')

payload = { "url": f'https://{site}' }
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": KEY,
	"X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(f'\nРезультат:	{response.json()['result_url'].replace('https://', '')}\n')