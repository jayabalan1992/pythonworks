import re
import csv
entry=[]
temp = ""
with open('BetteDavisFilms.txt') as f_input, open('output.csv', 'wb') as f_output:
    csv_output = csv.writer(f_output)

    for line in f_input:
        line=line.strip().replace(".","")

        if not line.isdigit():
            templist = (re.split(r'\((\d+)\)',line))
            for element in templist:
                entry.append(element)
            print entry
        else:
            if len(entry)>0:
                csv_output.writerow(entry)
                del entry[:]
            entry.append(line)
            print entry
    csv_output.writerow(entry)
f_output.close()
f_input.close()
