from tkinter import * 
global r
import ping
import ip_in_file
import shodan_test
import whois

r = Tk() 
r.title("check ip")
r.geometry("500x400")
r.resizable(0, 0)
l1 = Label(r,text="Enter IP in the box below")
l1.pack()

e1 = Entry(r)
e1.pack()

def scroll():
	ip = e1.get()
	l3 = Label(r,text="VPN/Proxy")
	l3.pack()
	
	scrollbar = Scrollbar(r)
	scrollbar.pack(side = RIGHT,fill =Y)
	mylist = Listbox(r, yscrollcommand = scrollbar.set, width = 200, height= 300)

	ping_out = ping.ping1(ip).split('\\'+'n')
	for pings in ping_out :
		mylist.insert(END, pings)

	ipout = ip_in_file.find_in_all_files(ip)
	mylist.insert(END, ipout[0])

	ipout_fl = ipout[1]

	if not ipout_fl :
		shodan_res = shodan_test.shodan1(str(ip))
		shodan_out = shodan_res[0].split('\n')
		for lines in shodan_out :
			mylist.insert(END, lines)

		if shodan_res[1] == 1 :
			l4 = Label(r,text="Yes")
			l4.pack()
		else :
			l4 = Label(r,text="No")
			l4.pack()

	whois_out = whois.whois1(ip)
	whois_res = whois_out.split('\n')
	for lines in whois_res :
		mylist.insert(END, lines)
	mylist.pack( side = LEFT, fill = BOTH ) 
	scrollbar.config( command = mylist.yview )
	

bt = Button(r, text='Check if VPN', width=25,command =scroll)
bt.pack() 

l2 = Label(r,text="Output")
l2.pack()

r.mainloop() 