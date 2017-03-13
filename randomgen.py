import random
spechar="!@#$"
lowers="abcdefghijklmnopqrstuvwxyz"
uppers=lowers.upper()
numbers="1234567890"
def specs():
    return random.choice(spechar)
def lower():
    return random.choice(lowers)
def upper():
    return random.choice(uppers)
def number():
    return random.choice(numbers)


def pwgen():
    password=" "

    funs = [specs, lower, upper, number]
    for i in range(10):
        password+=random.choice(funs)()
    return password
pwgn=pwgen()
print("Welcome to Password Generator! Here is your temporary password",pwgn)

def pwdchk():

    spechar = "!@#$"
    lowers = "abcdefghijklmnopqrstuvwxyz"
    uppers = lowers.upper()
    numbers = "1234567890"
    password = input("Enter your new password with length 8 chars with combination of upper, lower, numbers and spec chars")
    if len(password)==8:
        if any([c in spechar for c in password]):
            if any([c in lowers for c in password]):
                if any([c in uppers for c in password]):
                    if any([c in numbers for c in password]):
                        print("Your password has been changed to ",password)
                        return password
                    else:
                        print("Does your pwd contain numbers?")
                        pwdchk()
                else:
                    print("Does your pwd contain Uppercase?")
                    pwdchk()
            else:
                print("Does your pwd contain Lowercase?")
                pwdchk()
        else:
            print("Does your pwd contain Special chars?")
            pwdchk()
    else:
        print("Does your pwd has 8 chars?")
        pwdchk()


answer=input("\nDo you want to change your password? y/n")
if answer=='y':
    attempts = 0
    while attempts<3:
        temp = input("Enter your temp password")
        if temp==pwgn:
            print("Thank You")
            break
        else:
            print("Sorry! Try again")
        attempts+=1
    new = pwdchk()
else:
    print("Your password is same as temporary "+pwgen()+" when you login the next time")
