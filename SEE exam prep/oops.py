'''class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("the name:{} \n the age {}".format(self.name,self.age))

obj1=person("sachin",46)
obj1.display()'''


'''class complex():
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def display(self):
        print("{}+{}j is the complex you entered".format(self.real,self.img))
obj1=complex(1,2)
obj1.display()'''


'''class car:
    def __init__(self,cmpn,mdl,clr,mfy,price):
        self.cmpn=cmpn
        self.mdl=mdl
        self.clr=clr
        self.mfy=mfy
        self.price=price
    def display(self):
        print("the details are companyname={}\nmodel={}\ncolor={}\nmanufacturingyear={}\nprice={}\n".format(self.cmpn,self.mdl,self.clr,self.mfy,self.price))
carobj=[]
n=int(input("enter the number of cars you want to enter\n"))
for i in range(n):
    cmpn=input("enter the company name")
    mdl=input("enter the model")
    clr=input("enter the model")
    mfy=input("enter the manufacturing year")
    price=input("enter the price")
    carobj.append(car(cmpn,mdl,clr,mfy,price))

for obj in carobj:
    obj.display()'''

'''Airlineobject=[ ]
class ARS:
    def __init__(self,name,source,destination,travel_date):
        self.name=name
        self.source=source
        self.destination=destination
        self.travel_date=travel_date
    def display_pass_details(self):
         print(self.name,"\t",self.source,"\t",self.destination,"\t",self.travel_date)
Airlineobject.append(ARS("Sachin","bangalore","USA","1/oct/2020"))
Airlineobject.append(ARS("Dravid","bangalore","London","2/oct/2020"))
Airlineobject.append(ARS("Rahul","bangalore","China","3/oct/2020"))
Airlineobject.append(ARS("Kiran","bangalore","London","5/oct/2020"))
Airlineobject.append(ARS("Supreeth","USA","China","10/Feb/2020"))

for i in Airlineobject:
    if i.source=="bangalore"and i.destination=="London":
        i.display_pass_details()
'''

'''class user:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
class programer(user):
    def disp1(self):
        print("programer")


p1=programer("jake")
p1.display()
'''

'''class computer:
    def __init__(self,price,model):
        self.model=model
        self.__price=price
    def disprice(self):
        print(self.__price)
    def chngprice(self,price):
        self.__price=price

c=computer(3434,"lkjkj")
c.__price=2323
c.disprice()
c.__price=3434
c.disprice()
c.chngprice(343455)
c.disprice()'''

