#######################################################
# Title - Hallo.py
# Date - 05/09/2017
#######################################################

import socket
import threading
#############Functions#################################


#############Body######################################

Host = "10.94.73.9"
Port = 443
msg = raw_input("Message a envoyer ?")
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((Host, Port))
socket.send(msg)
socket.close()