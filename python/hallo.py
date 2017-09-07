#######################################################
# Title - Hallo.py
# Date - 05/09/2017
#######################################################

import socket
import threading
#############Functions#################################


#############Body######################################

Bindip = "0.0.0.0"
Bindport = 443

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind((Bindip, Bindport))

while True:
	Server.listen(5)
	conn, addr = Server.accept()
	print "%s connected." % conn

	reponse = conn.recv(255)
	if reponse != '':
		print reponse