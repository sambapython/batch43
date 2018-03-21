# usrl binding: hostname,port
# wait for the request
# once got a request accept
# process the request
# send the response back to client
def check_prime(number):
	for i in range(2,number):
		if number%i==0:
			return False
	else:
		return True
import socket
#print socket.gethostname()
host=socket.gethostname()
port = 9999
s=socket.socket()
try:
	s.bind((host,port))
	while True:
		s.listen(6)
		print "service running in %s:%s"%(host,port)
		print "waiting for the client request"
		#print s.accept()
		co, cinfo = s.accept()
		co.send("Hello firefox!! How are you doing??")
		req_data = co.recv(10)
		prime_result = check_prime(int(req_data))
		resp = "PRIME" if prime_result else "NOT A PRIME"
		co.send(resp)

except Exception as err:
	print err
finally:
	s.close()


