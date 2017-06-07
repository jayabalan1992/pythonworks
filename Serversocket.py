import time
import socket
from threading import Thread
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="localhost"
port=5000
s.bind((host,port))

def chat(c,addr):
    print "Connected from " + str(addr) + "\n"
    while True:
        data=c.recv(1024)
        if data=='q':c.close()
        if not data: break
        print "Jayabalan says  "+repr(data)+"\n"
def Main():
    while True:
        s.listen(5)
        c,addr=s.accept()
        chat(c,addr)
if __name__=='__main__':
    Main()



