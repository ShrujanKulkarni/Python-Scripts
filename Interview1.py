
l1 = [1,2,3,4,5]
l2= [6,7,8,9]
flag = 10
l1.extend(l2)
print(l1)

for x in l1:
    for y in l2:
        if x+y==10:
            print('Values that add up to 10:', x,y)
            