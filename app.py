from flask import send_file, send_from_directory
from flask import Flask, flash, request, redirect, url_for ,render_template,session
import json
import ip2proxyTest
import ipqualityTest
import shodanTest
import whoisTest
import vpnapiTest
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from datetime import datetime
import csv
import json_to_other
import readfromcsv
import os
from nocache import nocache

app = Flask(__name__)
GoogleMaps(app)

@app.route('/',methods=["POST","GET"])
def dashboard():
	file_list = ["pdf_reports.zip", "html_reports.zip", "json_reports.zip", "txt_reports.zip", "ip2proxyout.txt", "whoisout.txt", "shodanout.txt", "ipqualityout.txt", "ip2proxyout.json", "whoisout.json", "shodanout.json", "ipqualityout.json", "ip2proxyout.html", "whoisout.html", "shodanout.html", "ipqualityout.html", "ip2proxyout.pdf", "whoisout.pdf", "shodanout.pdf", "ipqualityout.pdf", "vpnapiout.json", "vpnapiout.txt", "vpnapiout.html", "vpnapiout.pdf"]
	for filename in file_list:
		if os.path.exists(filename):
			os.remove(filename)

	recent_ips = readfromcsv.read_csv()
	return render_template("dashboard.html", recent_ips=recent_ips[0], total_ips=recent_ips[1])


# download reports --------------------------------------
@app.route('/pdf_report',methods=["POST","GET"])
@nocache
def pdf_report():
    #return send_file('pdf_reports.zip', attachment_filename = 'pdf_reports.zip', as_attachment = True)
    return send_from_directory("",'html_reports.zip', as_attachment=True)

@app.route('/html_report',methods=["POST","GET"])
@nocache
def html_report():
    #return send_file('html_reports.zip', attachment_filename = 'html_reports.zip', as_attachment = True)
    return send_from_directory("",'html_reports.zip', as_attachment=True)

@app.route('/json_report',methods=["POST","GET"])
@nocache
def json_report():
    #return send_file('json_reports.zip', attachment_filename = 'json_reports.zip', as_attachment = True)
    return send_from_directory("",'html_reports.zip', as_attachment=True)

@app.route('/txt_report',methods=["POST","GET"])
@nocache
def txt_report():
    #return send_file('txt_reports.zip', attachment_filename = 'txt_reports.zip', as_attachment = True)
    return send_from_directory("",'html_reports.zip', as_attachment=True)


#-----------------------------------------------------------


@app.route('/search',methods=["POST","GET"])
def ip_search():
    if request.method == 'POST':
        given_ip = request.form
    
    ip = given_ip["IP"]

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    ip2proxy_out = ip2proxyTest.ip2proxy_fun(ip)
    # with open('ip2proxyout.json') as f:
    #     ip2proxy_out = json.load(f) 
    ipquality_out = ipqualityTest.ipquality_fun(ip)
    shodan_out = shodanTest.shodan_fun(ip)
    whois_out = whoisTest.whois_fun(ip)
    vpnapi_out = vpnapiTest.vpnapi_fun(ip)

#-------------------------------------------------------------------- 
    if(whois_out != {} and whois_out['nets']):
        data = whois_out['nets'][0]
    else:
        data = {}

#---------------------------------------------------------------------
    whois_final = []

    if(data != {}):
        if(data['cidr']):
            whois_final.append("Cidr        : " + data['cidr']) 
        else:
            whois_final.append("Cidr        : " + "NA")

        if(data['name']):
            whois_final.append("Name        : " + data['name'])
        else:
            whois_final.append("Name        : " +"NA")

        if(data['handle']):
            whois_final.append("Handle      : " + data['handle'])
        else:
            whois_final.append("Handle        : " +"NA")

        if(data['range']):
            whois_final.append("Range       : " + data['range'])
        else:
            whois_final.append("Range        : " +"NA")

        if(data['description']):
            whois_final.append("Description : " + data['description'])
        else:
            whois_final.append("Description        : " +"NA")

        if(data['country']):
            whois_final.append("Country     : " + data['country'])
        else:
            whois_final.append("Country        : " +"NA")

        if(data['state']):
            whois_final.append("State       : " + data['state'])
        else:
            whois_final.append("State       : " +"NA")

        if(data['city']):
            whois_final.append("City        : " + data['city'])
        else:
            whois_final.append("City        : " +"NA")

        if(data['address']):
            whois_final.append("Address     : " + data['address'])
        else:
            whois_final.append("Address     : " +"NA")

        if(data['postal_code']):
            whois_final.append("Postal Code : " + data['postal_code'])
        else:
            whois_final.append("Postal Code : " +"NA")

        if(data['created']):
            whois_final.append("Created     : " + data['created'])
        else:
            whois_final.append("Created     : " +"NA")

        if(data['updated']):
            whois_final.append("Updated     : " + data['updated'])
        else:
            whois_final.append("Updated     : " +"NA")

        if(data['emails']):
            whois_final.append("Email       : " + str(data['emails']))
        else:
            whois_final.append("Email       : " +"NA")

#---------------------------------------------------------------------
    ipquality_final=[]

    if(ipquality_out != {}):
        if(ipquality_out['country_code']):
            ipquality_final.append("Country code:      " + ipquality_out['country_code'])
        else:
            ipquality_final.append("Country code:      " + "NA")

        if(ipquality_out['region']):
            ipquality_final.append("Region:      " + ipquality_out['region'])
        else:
            ipquality_final.append("Region:      " + "NA")

        if(ipquality_out['city']):
            ipquality_final.append("City:      " + ipquality_out['city'])
        else:
            ipquality_final.append("City:      " + "NA")

        if(ipquality_out['ISP']):
            ipquality_final.append("ISP:      " + ipquality_out['ISP'])
        else:
            ipquality_final.append("ISP:      " + "NA")

        if(ipquality_out['organization']):
            ipquality_final.append("Organization:      " + ipquality_out['organization'])
        else:
            ipquality_final.append("Organization:      " + "NA")

#----------------------------------------------------------------------------

    fraud = ""  
    if(ipquality_out != {} and ipquality_out['fraud_score']):
        fraud += str(ipquality_out['fraud_score'])
    else:
        fraud += str(0)

#---------------------------------------------------------------------------

    lat_log = []
    if(ipquality_out != {} and ipquality_out['latitude']):
        lat_log.append(ipquality_out['latitude'])
    else:
        lat_log.append(0)

    if(ipquality_out != {} and ipquality_out['longitude']):
        lat_log.append(ipquality_out['longitude'])
    else:
        lat_log.append(0)
    str_lat_log = "https://maps.google.com/maps?q="+str(lat_log[0])+","+str(lat_log[1])+"&hl=en&z=9&amp;output=embed"

#-----------------------------------------------------------------------------

    mymap = Map(
        identifier="view-side",
        lat=str(lat_log[0]),
        lng=str(lat_log[1]),
        markers=[(str(lat_log[0]), str(lat_log[1]))]
    )

#------------------------------------------------------------------------------

    proxy_score = 0
    vpn_score = 0

    ipquality_vpn = False
    ipquality_proxy = False

    if(ipquality_out != {}):
        if(ipquality_out["vpn"]==True):
            ipquality_vpn = True
            vpn_score += 40
        if(ipquality_out["proxy"]==True) :
            ipquality_proxy = True
            proxy_score += 50
    
    shodan_vpn=False
    if(shodan_out != {}):
        if(shodan_out['tags']):
            if 'vpn' in shodan_out['tags']:
                shodan_vpn = True
                vpn_score = 100

    ip2proxy_proxy = False
    ip2proxy_vpn = False
    if(ip2proxy_out != {}):
        if(ip2proxy_out["isProxy"] != 'NO' and ip2proxy_out["proxyType"] == "VPN") :
            ip2proxy_vpn = True
            vpn_score += 40
            proxy_score += 10
        elif(ip2proxy_out["isProxy"] != 'NO') :
            ip2proxy_proxy = True
            proxy_score += 50
        elif(ip2proxy_out["proxyType"] == "DCH") :
            ip2proxy_proxy = True
            ip2proxy_vpn = True
            vpn_score += 20
            proxy_score += 25

    vpnapi_proxy = False
    vpnapi_vpn = False
    if(vpnapi_out != {} and vpnapi_out['security'] != {} and vpnapi_out['security']['vpn'] == True):
        vpnapi_vpn = True
        #vpn_score += 0
    elif(vpnapi_out != {} and vpnapi_out['security'] != {} and vpnapi_out['security']['proxy'] == True):
        vpnapi_proxy = True
        #proxy_score += 0

#-----------------------------------------------------------------------------

    vpn_level = ""
    proxy_level = ""

    if(vpn_score <= 20) :
        vpn_level = "Clean"
    elif(vpn_score <= 40) :
        vpn_level = "Low"
    elif(vpn_score <= 60) :
        vpn_level = "Moderate"
    else :
        vpn_level = "High"

    if(proxy_score <= 25) :
        proxy_level = "Clean"
    elif(proxy_score <= 50) :
        proxy_level = "Low"
    elif(proxy_score <= 75) :
        proxy_level = "Moderate"
    else :
        proxy_level = "High"

    json_to_other.generate_reports()
#--------------------------------------------------------------------------

    # ip, vpn_level, proxy_level, fraud, time to be stored in a csv file
    temp = []
    temp.append(ip)
    temp.append(vpn_level)
    temp.append(proxy_level)
    temp.append(fraud)
    temp.append(dt_string)

    with open('log.csv', 'a+') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile)
        # writing the data rows 
        csvwriter.writerow(temp)
    return render_template("result.html",ip=given_ip, whois_res=whois_final, ipquality_final=ipquality_final, mymap=mymap, lat_log=str_lat_log, shodan_vpn=shodan_vpn, fraud=fraud, vpn_level=vpn_level, proxy_level=proxy_level, ipquality_vpn=ipquality_vpn, ipquality_proxy=ipquality_proxy, ip2proxy_proxy=ip2proxy_proxy, ip2proxy_vpn=ip2proxy_vpn, vpnapi_proxy=vpnapi_proxy, vpnapi_vpn=vpnapi_vpn)

if __name__ == '__main__':
    app.run(host='localhost',port =5544,debug=True)

