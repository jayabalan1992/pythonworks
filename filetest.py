counter=0
f=open('jai.txt','r+')
file=f.readlines()
for i in file:
    if "python" in i:
        print(i)
f.close()