import random;
x= int(input(" enter your number from1 to 100="))
for i in range(50):
    z=100
    y=random.randint(1,101)
    
    
    
    if y>x:
        print("lowwer")
        z-=2
        print("your piont{}".format(z))
    if y<x:
        print("lowwer")
        z-=2
        print("your piont{}".format(z))
    if y==x:
        print("win")
        print("your piont{}".format(z))
        break
    if z==0 :
        print("you faild")
        print("your piont {}".format(z))
        break
