randict = {}
n = int(input("Enter number of entries: "))
for i in range(n):
     key = input("Enter a KEY: ")
     entry = input("Enter an Entry for the KEY: ")
     randict[key] = entry


print(randict)