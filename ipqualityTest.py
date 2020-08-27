import json
import requests

def ipquality_fun(IP) :
	str1 = "https://ipqualityscore.com/api/json/ip/u5Anqu9G5vFHgyxyD3DFpeZldLWLqVSE/"
	str2 = "?strictness=1&allow_public_access_points=true&fast=true"

	try :
		r = requests.get(str1 + IP + str2)
		x = r.json()
	except :
		x = {}

	f = open("ipqualityout.json",'w')
	json.dump(x, f, indent=4)
	f.close()
	return x