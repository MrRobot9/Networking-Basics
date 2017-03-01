import socket

def main():
	host = "127.0.0.1"
	port = 8080

	s = socket.socket()
	s.bind((host,port))

	s.listen(1)
	c , addr = s.accept()
	print "Connection from:",str(addr)

	while True:
		data = c.recv(1024)
		if not data:
			break
		print "from user" + str(data)
		data = str(data).upper()
		print "Sending:"+ str(data)
		c.send(data)
	c.close()


if __name__ == '__main__':
	main()


