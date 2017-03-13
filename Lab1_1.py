names=['Bob','Don','Sally','Cyndi','Charles','Ken','Steve','Martha']
#Print out the list

print "\nPrinting out the list"
for i in names:
    print(i)

#Creating new copy of the list names
names_cpy=names[:]

#Adding new name to the list
names_cpy.append('John')

#Printing new and original list
print "\nPrinting New list"
for i in names_cpy:
    print i

print "\nPrinting Original List"
for i in names:
    print i


# Creating copy of the list in reverse order
rev_names=names_cpy[::-1]

#Printing reverse list
print "\nPrinting Reverse List"
for i in rev_names:
    print i

print "\n \nThe first and last elements of the original list are: ",names[0]," and ",names[-1]