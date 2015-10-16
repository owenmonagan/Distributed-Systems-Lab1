import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


message= b"wOrk"
server = 'localhost'
port = 8000

request =  "GET /echo.php HTTP1.0\r\n"

s.connect((server,port))

s.sendall(b'GET /echo.php?message=' +
      message +
      b' HTTP/1.0\r\n\r\n'
    );

data = s.recv(1024)
data2 = data.decode("ascii")

for item in data2.split("\n"):
	if message.upper().decode("ascii") in item:
		print (item.strip())
s.close()

