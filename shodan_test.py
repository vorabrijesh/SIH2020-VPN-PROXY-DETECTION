import shodan
import nmap1 

def shodan1(IP) :
    # Setup the API wrapper
    api = shodan.Shodan('c4D4wJe0kdCyDOI60sAP4GEwCfkmj0mK') # Free API key from https://account.shodan.io
    result = ""
    # Lookup the list of services an IP runs
    try:
        ipinfo = api.host(IP)
    except shodan.APIError as error:
        return ("Shodan didn't find anything", 0)
    #print(ipinfo)
    # Check whether the IP runs a VPN service by looking for the "vpn" tag
    vpn_flag=0
    if 'tags' in ipinfo and 'vpn' in ipinfo['tags']:
        result = result + str(IP) + ' is connecting from a VPN' + '\n'
        vpn_flag = 1

    # Print general info
    # try :
    #     result = result+'IP: ' + str(ipinfo['ip_str']) + '\n' + 'Organization: '+ str(ipinfo.get('org', 'n/a')) + '\n'+ 'Operating System: '+ str(ipinfo.get('os', 'n/a'))+'\n'
    # except shodan.APIError as error:
    #     return (result + "Shodan didn't find anything more.\n", vpn_flag)
    # # Print all banners
    # vpn_flag1 = 0
    # ports = [1723,1194,22,1701,500,4789,443]
    # for item in ipinfo['data']:
    #     result = result + 'Port: ' + str(item['port']) + '\n' + 'Banner: ' + str(item['data']) + '\n'
    #     if nmap1.nma(IP, str(item['port'])):
    #         result = result + 'VPN detected on port - ' + str(item['port']) + '\n'
    #         vpn_flag1 = 1
    # if vpn_flag == 1:
    #     result = result + "IPSec vpn detected" + '\n'
    #     return (result, 1)
    # elif vpn_flag1 == 1:
    #     result = result + 'VPN detected' + '\n'
    #     return (result, 1)
    # else:
    # 	result = result + 'All good' + '\n'

    return (result, 0)
