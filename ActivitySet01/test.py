'''txt = 'but soft what light in yonder window breaks'
words = txt.split()
print("words:",words)
t = list()
for word in words:
    t.append((len(word), word))
print("t",t)
print(type(t[1]))
t.sort(reverse=True)
print(t)
res = list()
for length, word in t:
    res.append(word)
    print("individual res",res)

print("final res:",res)'''
from xml.etree.ElementTree import PI


x = "Python is "
y = "awesome"
z =  x + y
print(z)
print()
