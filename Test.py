import socket

HOST = '127.0.0.1' 			#localhost
PORT = 50007 			#서버와 같은 포트를 사용함
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓 생성
s.connect((HOST,PORT))
s.send(b'12 12 12') 		#문자를 보냄
data = s.recv(1024) 		#서버로 부터 정보를 받음
s.close()
