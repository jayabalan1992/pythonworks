import random
def pwgenerator():
	lower = 'abcdefghijklmnopqrstuvwxyz'
	up = lower.upper()
	special = "~!@#$%^&*()_-+=}{|[]\?/:;'<>,."
	password = ""
	for i in range(3):
		password += random.choice(lower)
		password += random.choice(up)
		password += random.choice(special)
	return password
pwg = pwgenerator()
print ("Welcome to Password Generator 1.0!\nHere is your temporary password:" ,pwg)

def password():
	x = input("Enter your password: ")
	z = '1234567890'
	y = 'abcdefghijklmnopqrstuvwxyz'
	w = y.upper()
	special = "~!@#$%^&*()_-+=}{|[]\?/:;'<>,."
	if len(x)>9:
		if any([c in z for c in x]):
			if any([c in y for c in x]):
				if any ([c in w for c in x]):
					if any ([c in special for c in x]):
						print ("Your password has been changed to < %s >" % x)
					else:
						print ("Does your password contain a special charcater? (~!@#$%^&*()_-+=}{|[]\?/:;'<>,.)")
						password()
				else:
					print ("Does your password contain an uppercase letter?")
					password()
			else:
				print ("Does your password contain a lowercase letter?")
				password()
		else:
			print ("Does your password contain a number?")
			password()
	else:
		print ("Is your password at least 9 characters long?")
		password()

def pwchecker():
	user = input("Please enter your temporary password: ")
	attempts = 0
	while attempts < 3:
		if user != pwg:
			user = input("Incorrect. Please enter it again: ")
			attempts += 1
		elif user == pwg:
			print ("Your new password must be at least 9 characters long, contain an uppercase/lowercase letter, at least one number and a special character.")
			password()
			break
	else:
		print ("Too many incorrect entries!")

personal = input("Would you like to change your password? (y/n) ")
while personal != 'y' and personal != 'n':
	personal = input("Sorry, what was that? (y/n)")
if personal == 'y':
	pwchecker()
elif personal == 'n':
	print ("Your password will still be " ,pwg + " the next time you log in")