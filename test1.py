import threading
import time

def square(n):

    for i in n:

        print "The square of "+str(i)+" is ",i*i

def cube(n):
    time.sleep(0.2)
    for i in n:
        print "The cube of "+str(i)+" is ",i*i*i

n=[2,4,6,8]
t=time.time()
t1=threading.Thread(target=square,args=(n,))
print "There are",threading.active_count()," Active count"
t2=threading.Thread(target=square,args=(n,))

t1.start()
t2.start()

t1.join()
t2.join()
print (time.time()-t)
