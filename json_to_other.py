# install these before running this file
# 1. sudo apt-get install wkhtmltopdf
# 2. pip install json2html
# 3. pip install pdfkit
# 4. pip install zipfile36
from json2html import *
import json
import pdfkit

from zipfile36 import ZipFile 

def generate_reports():
	with open("shodanout.json") as f:
		js = json.load(f)
		x = json2html.convert(json = js)

		f1 = open("shodanout.html",'w')
		f1.write(x)
		f1.close()

	with open("shodanout.json") as f:
		data = f.read().replace('\n', '')

		f2 = open("shodanout.txt", 'w')
		f2.write(data)
		f2.close()

	with open("ip2proxyout.json") as f:
		js = json.load(f)
		x = json2html.convert(json = js)
		
		f1 = open("ip2proxyout.html",'w')
		f1.write(x)
		f1.close()

	with open("ip2proxyout.json") as f:
		data = f.read().replace('\n', '')

		f2 = open("ip2proxyout.txt", 'w')
		f2.write(data)
		f2.close()

	with open("ipqualityout.json") as f:
		js = json.load(f)
		x = json2html.convert(json = js)

		f1 = open("ipqualityout.html",'w')
		f1.write(x)
		f1.close()

	with open("ipqualityout.json") as f:
		data = f.read().replace('\n', '')

		f2 = open("ipqualityout.txt", 'w')
		f2.write(data)
		f2.close()

	with open("whoisout.json") as f:
		js = json.load(f)
		x = json2html.convert(json = js)

		f1 = open("whoisout.html",'w')
		f1.write(x)
		f1.close()

	with open("whoisout.json") as f:
		data = f.read().replace('\n', '')

		f2 = open("whoisout.txt", 'w')
		f2.write(data)
		f2.close()

	with open("vpnapiout.json") as f:
		js = json.load(f)
		x = json2html.convert(json = js)

		f1 = open("vpnapiout.html",'w')
		f1.write(x)
		f1.close()

	with open("vpnapiout.json") as f:
		data = f.read().replace('\n', '')

		f2 = open("vpnapiout.txt", 'w')
		f2.write(data)
		f2.close()

	pdfkit.from_file('whoisout.html','whoisout.pdf')
	pdfkit.from_file('ipqualityout.html','ipqualityout.pdf')
	pdfkit.from_file('ip2proxyout.html','ip2proxyout.pdf')
	pdfkit.from_file('shodanout.html','shodanout.pdf')
	pdfkit.from_file('vpnapiout.html','vpnapiout.pdf')

	with ZipFile('pdf_reports.zip', 'w') as zipObj2:
	   	# Add multiple files to the zip
	   	zipObj2.write('whoisout.pdf')
	   	zipObj2.write('shodanout.pdf')
	   	zipObj2.write('ipqualityout.pdf')
	   	zipObj2.write('ip2proxyout.pdf')
	   	zipObj2.write('vpnapiout.pdf')

	with ZipFile('html_reports.zip', 'w') as zipObj2:
	   	# Add multiple files to the zip
	   	zipObj2.write('whoisout.html')
	   	zipObj2.write('shodanout.html')
	   	zipObj2.write('ipqualityout.html')
	   	zipObj2.write('ip2proxyout.html')
	   	zipObj2.write('vpnapiout.html')

	with ZipFile('txt_reports.zip', 'w') as zipObj2:
	   	# Add multiple files to the zip
	   	zipObj2.write('whoisout.txt')
	   	zipObj2.write('shodanout.txt')
	   	zipObj2.write('ipqualityout.txt')
	   	zipObj2.write('ip2proxyout.txt')
	   	zipObj2.write('vpnapiout.txt')

	with ZipFile('json_reports.zip', 'w') as zipObj2:
	   	# Add multiple files to the zip
	   	zipObj2.write('whoisout.json')
	   	zipObj2.write('shodanout.json')
	   	zipObj2.write('ipqualityout.json')
	   	zipObj2.write('ip2proxyout.json')
	   	zipObj2.write('vpnapiout.json')
