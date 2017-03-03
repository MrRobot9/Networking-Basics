import socket
import threading
import time

tlock = threading.Lock()
shutdown = False  #tells the thread to shut down when the program exits


def receiving(name,sock):
	while not shutdown:
		try:
			tlock.aquire()
			while True:
				data,addr = sock.revfrom(1024)
				print str(data)
		except:
				pass
		finally:
				tlock.release()

host = "127.0.0.1"
port =  0  #pick any free host

server = ('127.0.0.1',5000)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

rT = threading.Thread(target=receiving,args=("RecvThread",s))
rT.start()

alias = raw_input("Name:")
message = raw_input(alias+"-->")
while message != "q":
	if message != '':
		s.sendto(alias + ": "+ message,server)
	tlock.acquire()
	message = raw_input(alias + "-->")
	tlock.release()
	time.sleep(0.2)
shutdown = True
rT.join()
s.close()