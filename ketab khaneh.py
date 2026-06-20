class Ketab:
    def __init__(self,name,janer):
        self.name=name
        self.janer=janer
    def show(self):
              
              print(self.name,"/",self.janer)
               
def chap():
     for i,book in enumerate(d,1):
           print(i,end="_")
           book.show()
           
      



d=[]
while 1:
    start=int(input("add=1/delete=2/show=3/change=4  :"))
    if start ==1:

           name=str(input("enter the name="))
           janer=str(input("enter th janer="))
           u=Ketab(name,janer)
           d.append(u)
    if start==2:
           chap()
           de=int(input("enter your number for delete="))
           d.pop(de-1)

    if start==3:
         chap()
    if start==4:
         chap()
         ch=int(input("enter your number to change="))
         name=str(input("enter the name="))
         janer=str(input("enter th janer="))
         b=d[ch-1]
         b.name=name
         b.janer=janer
         