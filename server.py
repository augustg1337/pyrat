# coding: utf-8

from thread import *

import socket
import sys
import os

# config

host = "127.0.0.1"
port = 2600

# end config 

print "他妈的你"

class DevNull: # just to supress the broken pipe errors
	def write(self, msg):
		pass

sys.stderr = DevNull()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket object

s.bind((host, port))
s.listen(5) # listens for 5 clients, I suggest you change this

def clientThread(conn, msg): # kind of self explanitory 
	while True:
		conn.send(msg)

		data = conn.recv(1024)
		print data

while 1:
	msg = raw_input("") # our input
	conn, addr = s.accept()
	start_new_thread(clientThread, (conn, msg)) # starts a new thread for each new client