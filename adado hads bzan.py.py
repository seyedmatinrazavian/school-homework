import random;
for i in range(50):
    z=100
    y=random.randint(1,100)
    x=float(input("enter your number="))
    if x>y :
        print("lower")
        z-=2
        print("your point {}".format(z))
    if x<y :
        print("upper")
        z-=2
        print("your point {}".format(z))
    if x==y :
        print('good job')
        print("your point {}".format(z))
        break
    if z<=0 :
        print("you fiald")
        print("your point {}".format(z))
        break
