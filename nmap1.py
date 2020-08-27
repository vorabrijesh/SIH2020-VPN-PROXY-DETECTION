import nmap

def nma(host, port_no):
	nm = nmap.PortScanner()
	nm.scan(hosts=host, arguments=' -p ' +port_no)
	if int(port_no) in [1723,443]:
		print(nm.command_line())
		print(nm[host].state())		
		return nm[host].has_tcp(int(port_no))
	elif int(port_no) in [4789,500,1701,1194]:
		print(nm.command_line())
		print(nm[host].state())
		return nm[host].has_udp(int(port_no))