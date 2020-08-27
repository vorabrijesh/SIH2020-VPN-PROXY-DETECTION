import socket
import binascii

def ip_to_integer(ip_address):
 
    """
    Converts an IP address expressed as a string to its
    representation as an integer value and returns a tuple
    (ip_integer, version), with version being the IP version
    (either 4 or 6).
 
    Both IPv4 addresses (e.g. "192.168.1.1") and IPv6 addresses
    (e.g. "2a02:a448:ddb0::") are accepted.
    """
    for version in (socket.AF_INET, socket.AF_INET6):
        try:
            ip_hex = socket.inet_pton(version, ip_address)
            ip_integer = int(binascii.hexlify(ip_hex), 16)
 
            return ip_integer
        except:
            pass
 
    raise ValueError("invalid IP address")

def find_in_list(in_file, ip) :
    with open(in_file) as f:
        if str(ip) in f.read():
            f.close()
            return True

    f.close()
    return False

def find_in_all_files(ip) :
    suspect_flag = 0
    int_ip = ip_to_integer(ip)
    in_file = "sure_results.txt"
    list_of_files = ["results1.txt", "results2.txt", "results3.txt", "results4.txt", "results5.txt",
                     "results6.txt", "results7.txt", "results8.txt", "results9.txt","results10.txt"]
    if find_in_list(in_file, int_ip) :
        return ("VPN detected", True)
    else :
        for file in list_of_files :
            if find_in_list(file, int_ip) :
                return ("Proxy/VPN detected", True)
                suspect_flag = 1
                break

        if suspect_flag == 0:
            return ("Go for Shodan", False)
