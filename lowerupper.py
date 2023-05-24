#Exercise: Arrange string characters such that lowercase letters should come first

s1 = input("Enter a word with upper and lower cases:")

print("Original word:",s1)
l=[]
u=[]
for x in s1:
    if x.islower():
        l.append(x)
    elif x.isupper():
        u.append(x)
newstr=''.join(l+u)


print('New word:',newstr)
