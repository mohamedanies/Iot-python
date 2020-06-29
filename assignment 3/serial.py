import serial
def main(args):
	ser_r = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.050)
	while True:
		read_serial = ser_r.readline()
		if (read_serial):
			print(read_serial)
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
