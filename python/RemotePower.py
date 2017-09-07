##################################
# Title - Remote Power Server
# Date - 05/09/2017
##################################

import socket
import subprocess as sp
import sys

##########Functions###############


##########Body####################

host = '0.0.0.0'
port = 443

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(10)
conn, addr = server.accept()

print "Connecion etablie depuis %s" % addr[0]

while 1:
	command = raw_input ("> ")

	if command != "exit()":
		if command == '':
			continue

		conn.send(command)
		result=conn.recv(1024)

		total_size = long(result[:16])
		result = result[16:]

		while total_size > len(result):
			data = conn.recv(1024)
			result += data

		print result.rstrip("\n")

	else:
		conn.send ("exit()")
		print "Disconnect"
		break

server.close()