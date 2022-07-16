def inptlst():
    '''while(t):
        a=input("enter the number of values")
        x=a.split()
    
        try:
            len(x)==a
            for i in x:
                i=int(i)
        except:
            print("the length of the string is not the right value , kindly enter the right value")
            continue
        t-=1
    '''
    a=input("enter the number of values")
    y=input("enter the values")

    try:
        x=y.split()
        len(x)==a
        y=list()
        for i in x:
            y.append(int(i))
    except:
        print("the length of the string is not the right value , kindly enter the right value")
        inptlst()
    return y

def finllst(x):
    y=list()
    i=0
    while(i<len(x)):
        if(x[i]==0):
            if(x[i+1]==0):
                y.append(0)
                i+=2
                continue
            else:#if(x[i+1]!=0 ):#and x[i+2]!=0):
                if (x[i+2]!=0):
                    for j in range(x[i+1]):
                        y.append(x[i+2])
                    i+=3
                    continue
                else :
                    y.append(x[i])
                    y.append(x[i+1])
                    y.append(x[i+2])
                    i+=3
                    continue
        else:
            y.append(x[i])
            i+=1
            continue

    '''elif(x[i]!=0):
            if(x[i+1]!=0):
                if(x[i+2]!=0):
                    y.append(x[i])
                    y.append(x[i+1])
                    y.append(x[i+2])
                    i+=3
                    print(y)
                    continue
                y.append(x[i],x[i+1])
                i+=3
                print(y)
                continue
            y.append(x[i])
            i+=1
            print(y)
    '''
    return y

        


         

def main():
    t=int(input("enter the number values you want to enter"))
    for i in range(t):
        x=inptlst()
        print(x)
        y=finllst(x)
        print(y)
        t-=t


main()