from bs4 import BeautifulSoup
from decimal import Decimal

def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?date_req={}'.format(date))  # Использовать переданный requests
    soup = BeautifulSoup(response.content,"xml")
    if cur_from == 'RUR':
        inRubs = amount
    else:
        curs = Decimal(soup.find('CharCode', text=cur_from).find_next_sibling('Value').string.replace(',','.'))
        nominal =  Decimal(soup.find('CharCode', text=cur_from).find_next_sibling('Nominal').string.replace(',','.')) 
        inRubs = amount*curs/nominal
    if cur_to == 'RUR':
        return inRubs.quantize(Decimal('.0001'), rounding='ROUND_UP')
    else:
        curs = Decimal(soup.find('CharCode', text=cur_to).find_next_sibling('Value').string.replace(',','.'))
        nominal =  Decimal(soup.find('CharCode', text=cur_to).find_next_sibling('Nominal').string.replace(',','.'))
        return (inRubs/curs*nominal).quantize(Decimal('.0001'), rounding='ROUND_UP')

