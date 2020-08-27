from ipwhois import IPWhois
import json

def whois_fun(IP):
	try:
		obj = IPWhois(IP)
	except ipwhois.exceptions.IPDefinedError:
		res = {}
	else:
		try :
			res = obj.lookup_whois(asn_methods=['dns', 'whois', 'http'])
		except ipwhois.exceptions.ASNRegistryError:
			res = {}

	f = open("whoisout.json",'w')
	json.dump(res, f, indent=4)
	f.close()
	return res