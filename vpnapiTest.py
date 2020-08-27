# https://vpnapi.io/

import json
import requests

def vpnapi_fun(IP):
	str1 = "https://vpnapi.io/api/"
	str2 = "?key=F9J3K1V02MFO1C93KA7B"

	try:
		r = requests.get(str1 + IP + str2)
		x = r.json()
	except :
		x = {}

	f = open("vpnapiout.json",'w')
	json.dump(x, f, indent=4)
	f.close()
	return x

# to include in app.py
# keep the minimalistic weight for this api , will keep only 5 
# vpnapi_vpn = False
# vpnapi_proxy = False

# vpnapi_vpn = x["security"]["vpn"]
# vpnapi_proxy = x["security"]["proxy"]

# print(vpnapi_vpn)
# print(vpnapi_proxy)









