import socket
host = host = socket.gethostname()
print ("Host name of server is"+host)
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
s.listen(1)
print ("Server waiting to receive files in accept state")
sock , address = s.accept()
veri = str(sock.recv(512))
print(veri)
print(type(veri))
sock.close()
s.close()
