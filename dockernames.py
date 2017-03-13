f=open('C:/Users/jai/Desktop/docker.txt','r+')
file=f.readlines()
for i in file:
    temp=i.split()
    print(temp[0],end=' ')
