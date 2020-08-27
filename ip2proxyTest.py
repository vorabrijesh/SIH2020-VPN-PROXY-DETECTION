from requests import get
import json

def ip2proxy_fun(IP) :
	in1 = 'https://api.ip2proxy.com/?ip='
	in2 = '&key=demo&package=PX8'

	inp = in1 + IP + in2

	try:
		response = get(inp).json()
	except :
		response = {}

	f = open("ip2proxyout.json",'w')
	json.dump(response, f, indent=4)
	f.close()
	return response