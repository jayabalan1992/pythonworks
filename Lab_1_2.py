print "========================================\n        Encryption of a string\n========================================"

a=raw_input("Enter a string with lowercase alphabet characters only:\t")

encrypt=[]
for i in a:
    if ord(i)%2==0:
        encrypt.append(ord(i)-1)
    else:
        encrypt.append(ord(i)+1)
print "\n\nThe encrypted string is:",
delim=''
word=[]
for i in encrypt:
    word.append(delim.join(chr(i)))
print "".join(word)