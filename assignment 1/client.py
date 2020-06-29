import socket
host = socket.gethostname()
#host = "192.168.31.22"
print ("host name of client is "+host)
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host , port))
s.send(b"Hello")
s.close()