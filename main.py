import random
'''stone: -1
   paper: 0
   cizer: 1
'''
computer=random.choice([-1,0,1])
youCho=input("Enter your choice (stone as s/paper as p/cizer as c):")

youDict={"s":-1,"p":0,"c":1}
you=youDict[youCho]

new_dict={-1:"Stone",0:"Paper",1:"Cizer"}

print(f"Your choise is {new_dict[you]}")
print(f"Computer choise is {new_dict[computer]}")


if(computer==you):
    print("Match Draw")
else:
    if(computer==-1 and you==0):  
        print("You Win!")
    elif(computer==-1 and you==1):
        print("You Lose!")

    elif(computer==0 and you==-1):
        print("You Lose!")
    elif(computer==0 and you==1):
        print("You Win!")

    elif(computer==1 and you==0):
        print("You Lose!")
    elif(computer==1 and you==-1):
        print("You Win!")
    else:
        print("Something went wrong")

