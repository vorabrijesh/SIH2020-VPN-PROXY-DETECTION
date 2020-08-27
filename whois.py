from ipwhois import IPWhois
import sys 
import ipwhois

def whois1(ip):
	ans = ""
	try:
		obj = IPWhois(ip)
	except ipwhois.exceptions.IPDefinedError:
		res = {}
	else:
		try :
			res = obj.lookup_whois()
		except ipwhois.exceptions.ASNRegistryError:
			res = {}

	if (res=={}):
		ans = ans + 'Private Network'+ '\n'
		return ans
	j=1
	for i in res:
		if i=='nets' :
			str1 = str(res[i])
			str1 = str1.split(",")
			for k in str1:
				ans =ans + '         ' + str(k)+ ' \n '
		else:
			ans = ans + str(i) + ' : '+ str(res[i]) +' \n '

		j = j+1
	return ans