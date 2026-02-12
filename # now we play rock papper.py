# now we play rock papper 

import random 


p=["stone","papper","scissors"]


x=str(input("chosses -stone   . papper . scissors  ="))

y = random.choice(p)

if x=="stone" :
    if y=="stone":
     print("draw")  
    if y=="papper":
     print("you lose")
    if y=="scissors":
     print(" you win")

if x=="paper":
    if y=="stone":
     print("you win")  
    if y=="papper":
     print("draw")
    if y=="scissors":
     print(" you lose")

if x=="scissor":
    if y=="stone":
     print("you lose")  
    if y=="papper":
     print("you win")
    if y=="scissors":
     print(" draw")

else:
    print("try agian and hoisse ")