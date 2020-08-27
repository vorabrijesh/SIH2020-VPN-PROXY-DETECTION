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


def extract_ips(in_file):
    buffer1 = []

    for line in in_file:
        #Used here to match
        x = line.split(':')
        y = x[1].split('-')
        z = y[1].split('\n')
        print(y[0])
        print(z[0])
        l = ip_to_integer(y[0])
        r = ip_to_integer(z[0])
        for i in range(l,r+1) :
            buffer1.append(i)

    in_file.close()
    return buffer1


def write_to_file(buffer1, out_file):
    for proxy in buffer1:
        with open(out_file, "a") as res:
            res.write(str(proxy)+'\n')


if __name__ == '__main__':
    print ("Running....")
    in_file = "sample1.txt"
    out_file = "results.txt"
    write_to_file(extract_ips(open(in_file)), out_file)