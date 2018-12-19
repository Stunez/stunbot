# ниже egov берет инфу доллара в наст. время 
import requests


url = 'https://api.telegram.org/bot641542217:AAHj-pmdV9Gg9IZ6epNOQDUCiLokDhKZiWs/getupdates'

resp = requests.get(url=url)
data = resp.json()


for result,a in zip(range(len(data)),data):
	print(a)
	"""


USD = "USD"
USD = list(filter(lambda x: x['kod'] == USD, data))
if len(USD) > 0:
	USD = USD[0]

print (USD)
"""

lat = list(filter(lambda x: x['result']['message']['location']['lalitude'] > 0, data))
if len(lat) > 0:
	lat = lat[0]
print (lat)
