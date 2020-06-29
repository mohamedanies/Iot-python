'''Python - Bluetooth programming!
Clien'''


import bluetooth

bd_addr = "AC:72:89:21:8B:43"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
