import time
import socket
s=socket.socket()
s.connect(("127.0.0.1",5000))

while True:
    data=raw_input("Enter data: ")
    if data=="q":
        s.sendall("I am quitting")
        break
    s.send(data)
s.close()