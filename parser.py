import requests
import io
import xml.etree.ElementTree as et
from datetime import *

date = '{:%Y%m%d}'.format(datetime.now())
params = {'date': date}
r = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange', params=params)
content = r.text
print(r.url)
root = et.fromstring(content)
with io.open('currency.txt', 'w', encoding='utf-8') as file:
    for currency in root.findall('currency'):
        index = currency.find('cc')
        name = currency.find('txt')
        rate = currency.find('rate')
        date = currency.find('exchangedate')
        file.write('{}|{}|{}|{}\n'.format(date.text, index.text, name.text, rate.text))
    file.close()

