import shodan
import json

api = shodan.Shodan('bf46of5Z6w7ZVweWxb3oqm4DvR8DIRyk') 	#public api key

def shodan_fun(IP) :
	try:
		ipinfo = api.host(IP)
	except shodan.APIError as e:  #this line is resolved
		ipinfo = {}

	f = open("shodanout.json",'w')
	json.dump(ipinfo, f, indent=4)
	f.close()
	return ipinfo