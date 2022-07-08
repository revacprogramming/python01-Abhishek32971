def dictofallcom(a):
    d=dict()
    l=-1
    for i in a:
        if l==len(a)-3:
            break
        o=list()                           #create list to add all possible combinations 
        l=l+1                              #::::l::::; is used to indicate the perticular index 
        for j in range(l+2,len(a)):        #add all possible combinations form that index till end of string length(3 or more)
            o.append(a[l:j+1])
        d[l]=o                             #add individual list to dictionary with key as the index
    print(d)           
    return d


def isPalindrome(s):
    return s == s[::-1]


def output(l):
    for i in l:
        for p in range(len(l[i])):
            if isPalindrome(l[i][p]):
                print(i,l[i][p])


def main():
    z=int(input("enter the length of string"))
    a=input("enter the string")
    l=dictofallcom(a)
    output(l)


main()