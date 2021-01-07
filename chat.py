import socket
import threading

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

s.bind(("192.168.43.106",5678))

def a():
   while True: 
      x = s.recvfrom(1024)
      y=x[0]  
      print(y)

def b():
   while True:
     e = input()
     s.sendto( e.encode(),("192.168.43.47",1234) )
  
x1 = threading.Thread( target=a )
x2 = threading.Thread( target=b )

x1.start()
x2.start()
