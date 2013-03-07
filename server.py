import socket #Using socket module
from time import gmtime, strftime #Getting date and time

s = socket.socket()
host = ''
port = 4656
s.bind((host, port)) #Listening at port 4656

s.listen(3)
while True:
	c, addr = s.accept()

	headers = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\n' + strftime("%Y-%m-%d %H:%M:%S", gmtime())
	
	#Sending Response headers
	c.send(headers)
	c.send('\n')
	c.send('\n')
	c.send('Hello World!')

	c.close()