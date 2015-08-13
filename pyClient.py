#!/usr/bin/env python
import socket

def Main():
	host = '178.62.91.83'
	port = 5000

	s = socket.socket()
	s.connect((host, port))

	message = raw_input("-> ")

	while message != "q":
		s.send(message)
		print "Sending: " + str(message)
		data = s.recv(1024)
		print "Received: " + str(data)		
		message = raw_input("-> ")
	s.close()

if __name__ == '__main__':
	Main()
