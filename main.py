from requests import get
import re
import time

def getPriceOfBitCoin():
	file = open('output.txt','a+',encoding='utf-8')
	realtime = time.strftime("%d/%m/%Y %H:%M:%S")
	request = get('https://www.coindesk.com/price/bitcoin')
	request = request.text
	data = re.findall('<div class=\"price-large\"><span class=\"symbol\">\$</span>(\d*,\d*.\d*)</div>', request)
	print(data[0])
	file.write(str(data[0]))
	file.write(realtime)
	file.write('\n')
	file.close()
if __name__ == "main":
	getPriceOfBitCoin()