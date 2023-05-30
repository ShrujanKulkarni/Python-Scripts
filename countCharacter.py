# Exercise: Count all letters, digits, and special symbols from a given string

def countcharacters(str):
    c=0
    s=0
    n=0
    for x in str:
        if x.isalpha():
            c=c+1
        elif x.isnumeric():
            n=n+1
        else:
            s=s+1
    
    print("Number of characters=",c, "Number of digits=",n, "Number of special characters=",s)



str= input("Enter few characters, digits and special symbols: ")
countcharacters(str)




