## developed by eshan soni

import socket

print ("//////____loading.................")
print("\n## ***DEVWLOPED BY ESHAN SONI ##******")
lines = /\/\^^^^^/\/\||||||||>>>>>>Loaded
for i in lines:
print(i)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print (s)

port = 80
print("entre the hostname")
hostname = input()
server_ip = socket.gethostbyname(hostname)
print(server_ip)

request = "GET / HTTP / 1.1\nHOST"+hostname+"\n"

s.connect((hostname,port))
s.send(request.encode())
result = s.recv(4096)

#please hit the like
