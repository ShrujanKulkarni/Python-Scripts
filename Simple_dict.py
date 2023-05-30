person = {"name": "Jessa", "country": "USA", "telephone": 1178}

print("All Keys in the Dictonary:",end=' ')
for x in person.keys():
    print(x)

print("All Values in the Dictonary:",end=' ')
for x,y in person.items():
    print(y)

print("All Key, Value pairs in the Dictonary:")
for x,y in person.items():
    print("Key:",x +' '+ 'Value:',y)
