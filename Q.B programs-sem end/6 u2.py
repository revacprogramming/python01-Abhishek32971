import re
count=0
str1='efdifhhu4huh5jhbbsiaa'
for i in str1:
    if re.match("(a|e|i|o|u)",i):
        print('yes')
        count+=1
print(count)

