import requests
import re
resp= requests.get('http://cbr.ru')
html= resp.text
match= re.search(r'Доллар США\D+(\d+,\d+)', html)
rate= match.group(1)
print(rate)