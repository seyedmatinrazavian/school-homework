#do what in day?
import tkinter
import pickle


class Need():
    def __init__(self, need,time1,time2):
        self.time1=time1
        self.time2=time2
        self.need=need
    def print(self):
        p=1
        print(self.need,"/","as",self.time1,"to",self.time2)   
        p+=1
class Want():
    
    def __init__(self,want,time1,time2):
        self.time1=time1
        self.time2=time2
        self.want=want
    def printt(self):
        po=1
        print(self.want,"/","as",self.time1,"to",self.time2)
        po+=1 
        
ufo=0        
uff=0                         
                

if ufo>0:               
    file=open("needs.pkl","wr")
    read=file.read()
    file.close()
    needs=pickle.load(read)

needs=[]



if uff>0:
    filew=open("wants.pkl","wr")
    readw=file.read()
    filew.close()
    wants=pickle.load(readw)

wants=[]




def chapn():
    print("what i need to do:")
    for i,j in enumerate(needs,1):   
         print(i,end="_")
         j.print()
    


def chapw():
    print("what i want to do:")
    for a,s in enumerate(wants,1):    
        print(a,end="_")
        s.printt()

    pass

while 1:
    x=int(input("append need work=1/append want work=2/ show=3/edit=4/remove=5/close and save=6   :"))
    if x==1:

        need=str(input("enter your need work="))
        time1=str(input("enter your time start:"))
        time2=str(input("enter our finish time:"))
        coc=Need(need,time1,time2)
        needs.append(coc)


    if x==2:

        want=str(input("enter your want work="))
        time1=str(input("enter your time start:"))
        time2=str(input("enter our finish time:"))
        coa=Want(want,time1,time2)
        wants.append(coa)


    if x==3:
        chapn()

        chapw()


    if x==4:
        chapn()
        chapw()
        print("_________________________________________")
        want_to_edit=int(input("edit need=1/edit want=2  :"))

        if    want_to_edit==1:
            change=int(input("enter your number to edit="))
            need=str(input("enter your need work="))
            time1=str(input("enter your time start:"))
            time2=str(input("enter our finish time:"))
            need1=needs[change-1]
            need1.need=need
            need1.time1=time1
            need.time2=time2

        if    want_to_edit==2:
            change=int(input("enter your number to edit="))
            want=str(input("enter your want work="))
            time1=str(input("enter your time start:"))
            time2=str(input("enter our finish time:"))
            want1=wants[change-1]
            want1.want=want
            want1.time1=time1
            want1.time2=time2

        if x==5:
            chapn()
            chapw()
            remove=int(input("delete from need work=1/delete from want work=3   :"))


            if remove==1:
               delete=int(input("what you want to delete  just choise the number!!!!:"))
               needs.pop(delete-1)


            if remove==2:
                delete=int(input("what you want to delete  just choise the number!!!!:"))
                wants.pop(delete-1)

        if x==6:
            file=pickle.dumps(needs)
            read=open("needs.pkl","wfile")
            read.write(file)
            read.close
            ufo+=1

 
  
            filew=pickle.dumps(wants)
            readw=open("wants.pkl","wfilew")
            readw.write(filew)
            readw.close()
            uff+=1


                