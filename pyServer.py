#!/usr/bin/env python
import socket

def Main():
    host = '127.0.0.1'
    host = '178.62.91.83'
    port = 5000
    print "Starting Socket, LISTENING ON: " + str(host) + ":" + str(port)
    s = socket.socket()
    s.bind((host, port))

    s.listen(100)

    c, addr = s.accept()
    print "Connection from: " + str(addr)

    while True:
	data = c.recv(1024)
 	if not data:
	    break
	print "Received: " + str(data)
	data = str(data).upper()
	print "Sending: " + str(data)
	c.send(data)

    print "Connection Closed"
    c.close()

if __name__ == '__main__':
    Main()
