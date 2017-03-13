import csv

iplist = []

# Reading from csv file
with open("CapturedFile.csv","r") as capture:
    capturereader=csv.reader(capture)
    dest=[]
    for row in capturereader:
        if len(row)!=0:
            if row[3] not in dest:
                ip = row[3].split('.')
                if len(ip) > 1:
                    dest.append(row[3])
                    iplist.append(row[3])

capture.close()

for i in range(len(iplist)):
    for j in range(len(iplist) - 1):
        x = iplist[j].split('.')
        y = iplist[j+1].split('.')
        if int(x[0]) > int(y[0]):
            iplist[j], iplist[j+1] = iplist[j+1], iplist[j]
        elif int(x[0]) == int(y[1]):
            if int(x[1]) > int(y[1]):
                iplist[j], iplist[j + 1] = iplist[j + 1], iplist[j]
            elif int(x[1]) == int(y[1]):
                if int(x[2]) > int(y[2]):
                    iplist[j], iplist[j + 1] = iplist[j + 1], iplist[j]
                elif int(x[2]) == int(x[2]):
                    if int(x[3]) > int(y[3]):
                        iplist[j], iplist[j + 1] = iplist[j + 1], iplist[j]

# Writing to text file
with open("Destination.txt","w+") as output:
    for ip in iplist:
        output.write(ip)
        output.write("\n")


output.close()