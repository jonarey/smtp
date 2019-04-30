# server for secure connection SMTP application
# encodes/decodes messages 
# user authentication 
# server log management 
# multithreading through process management 
# TCP connection with client

import sys
import socket
import threading 
# cmd line inputs

port = 55001
if len(sys.argv) < 3:
    #print("Please provide 2 files: a json file for input, and a text file with starting points")
    print("Usage: python server.py hostname port_number")
    exit(2)
else:
    print("Parameters accepted. \n")
    hostname_str = sys.argv[1]
    hostname = int(hostname_str)
    port = sys.argv[2]

    #print("Hostname: " + hostname) 
    #print("Port: " + port) 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#associates  hostname & port -> socket
sock.bind((hostname,port))

# parameter defines connection backlog size 
sock.listen(5)



