def dictofallcom(a):
    d=dict()
    l=-1
    for i in a:
        if l==len(a)-3:
            break
        o=list()
        l=l+1
        for j in range(l+2,len(a)):
            o.append(a[l:j+1])
        d[l]=o
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