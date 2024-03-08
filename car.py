import random

def randomize(word):
    print()
    otherword=""
    for i in word:
        rand=random.randint(0,10)
        if rand%2==0:
            otherword+=i.lower()
        else:
            otherword+=i.upper()
    return otherword

choice=input("What do you want to do? 1.Lowercase 2.Uppercase 3.Randomize \n")

if(choice=="1"):
    word = input("What is your word? \n")
    print()
    otherwordd=""
    for i in word:
        otherwordd+=i.lower()
    print(otherwordd)

elif (choice=="2"):
    word = input('What is your word?\n')
    print()
    otherword=""
    for i in word:
        otherword+=i.upper()
    print(otherword)

elif (choice=="3"):
    word = input('What is your word?\n')
    returner=randomize(word)
    print(returner)

