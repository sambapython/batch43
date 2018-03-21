import socket
host="khyaathipython"
port=9999
s=socket.socket()
try:
	s.connect((host,port))
	ack = s.recv(1024)
	print "ack:",ack
	num=raw_input("Enter a number:")
	s.send(num)
	resp_service = s.recv(20)
	print "response=",resp_service
except Exception as err:
	print err
finally:
	s.close()