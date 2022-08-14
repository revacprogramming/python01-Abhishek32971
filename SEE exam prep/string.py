str1="everything is lost"
print(str1[1:40])


def slicing():
	m=int(input("Enter the starting index value or index1"))
	n=int(input("Enter the ending index value or index2"))
	substr=str1[m:n]
	print("String extracted between index1 and index2 is",substr)
str1=str(input("Enter the string"))
slicing()
del str1