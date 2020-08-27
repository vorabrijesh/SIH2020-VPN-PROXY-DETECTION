import csv

fields = ['ip', 'vpn_level', 'proxy_level', 'fraud_score', 'datetime']

with open('log.csv', 'a+') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile)

    # writing the data rows 
    csvwriter.writerow(fields)