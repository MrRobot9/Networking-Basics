import socket

def main():
	host = '127.0.0.1'
	port = 5000

	s= socket.socket()
	s.connect((host,port))

	filename = raw_input("Filename ->")
	if filename != 'q':

		s.send(filename)

		data = s.recv(1024)
		if data[:6] == 'EXISTS' :
			filesize = long(data[6:])
			print filesize
			message =raw_input("FIle Exists"+str(filesize)+"Byes,download? (Y/N) ->")

			if message == 'Y':
				s.send('OK')
				f = open('new _'+filename,'wb')
				data = s.recv(1024)
				totalRecv = len(data)
				f.write(data)
				while  totalRecv < filesize:
					data = s.recv(1024)
					totalRecv += len(data)
					f.write(datass)
					f.write(data)
					print "{0:2f}".format((totalRecv/float(filesize))*100+ " % DOne")

				print "Download complete"
		else:
			print "File does not exist"

	s.close()


if __name__ == '__main__':
	main() 