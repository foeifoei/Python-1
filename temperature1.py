from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv 
from datetime import datetime

def writetocsv(data):

	date = datetime.now().strftime('%Y-%m-%d')
	
	with open('data-temperature.csv','a',newline='',encoding='utf-8') as files:
		filewriter = csv.writter(file)
		filewriter.writerow(data)

alldata = {}

def checktemp(ID):
	url = "https://www.tmd.go.th/province.php?id=" + str(ID)

	webopen = urlopen(url)
	html_page = webopen.read()
	webopen.close()


	data = BeautifulSoup(html_page,"html.parser")

	try:
		temp = data.find('td',{'class':'strokeme'})
		title = data.find('span',{'class':'title'})

		city = title.text.strip()
		print(title.text.strip())
		print(temp.text)
	except:
		print('ไม่มีข้อมูล')

for i in range(1,30):
	checktemp(i)

print(alldata)

for k,v in alldata.items():
	data = [k,v]
	writetocsv(data)

print('save')