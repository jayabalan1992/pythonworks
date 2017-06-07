import random
with open("G:\pycharm projects\dictionary.txt",'r') as dict:
    dictionary=dict.read().split()
def hangman():

    word=random.choice(dictionary)
    length,i=len(word),6
    ans=["_"]*length
    print(" ".join(ans))
    chances=[]
    while i>0:
        print("\nYou have ", i, " chances.",end=" " )
        while True:
            a=str(input(" Enter a letter "))
            a=a.upper()
            chances.append(a)
            print("\nWritten letters "," ".join(chances))
            if a in word:
                for count in range(len(ans)):
                    if word[count]==a:
                        ans[count]=a
                    count+=1
                print(" ".join(ans))
            else:
                print("wrong")
                break
        if "_" in ans:

            i -= 1
        else:
            print("\nYou have won and helped the man from hanging")
            break
    if "_" in ans:
        print("\nYou Lost and the correct answer is ",word)


hangman()