def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x
def inputvalues(n):
    l=list()
    for i in range(n):
        x=int(input("enter the denomenators"))
        l.append(x)
    return l 
def calcnum(x):
    v=0
    y=list()
    for i in x:
        num=calcden(x)/i
        y.append(num)
    for i in y:
        v=v+i
    return v
        
def calcden(x):
    den=1
    for i in x:
        den=den*i
    return den

def calcFinal(x):
    n=calcnum(x)
    d=calcden(x)
    t=compute_hcf(n,d)
    y=n/t
    z=d/t
    return y,z

def main():
    n=int(input("enter the number of denominators"))
    x=inputvalues(n)
    y,z=calcFinal(x)
    print("the fractinal value of the number of items entered is %d/%d \n"%(y,z))
main()
