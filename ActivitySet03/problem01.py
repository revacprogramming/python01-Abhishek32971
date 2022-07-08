import math
def smallest2(a,b,c):
    if a<b and c<b:
        print(a,c)
        return a,c
    elif b<a and c<a:
        print(b,c)
        return b,c
    else :
        print(a,b)
        return a,b 
def dista(x1,y1,x2,y2):
    d=math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
    print(d)
    return d
def main():
    i=int(input('enter the number of times you want to exectute the loop'))
    while i!=0:
        #x1,x2,x3,y1,y2,y3=int(),int(),int(),int(),int(),int()
        x1,y1,x2,y2,x3,y3=input(""),input(""),input(),input(),input(),input()
        x1,x2,x3,y1,y2,y3=float(x1),float(x2),float(x3),float(y1),float(y2),float(y3)
        a=dista(x1,y1,x2,y2)
        b=dista(x2,y2,x3,y3)
        c=dista(x1,y1,x3,y3)
        z,t=smallest2(a,b,c)
        area=z*t
        print("Area of rectangle with vertices (%.1f,%.1f),(%.1f,%.1f),(%.1f,%.1f) is %.1f" %(x1,y1,x2,y2,x3,y3,area))
        i-=1

main()
print("thankyou for choosing me to execute your math problem!!!\n")
    