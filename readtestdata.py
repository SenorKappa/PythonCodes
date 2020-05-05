#file streaming
#r read file
#w write on a file
#a append information to a file
#r+ read and write to a file

def filestream(filename):
    variable = open(filename, "r")
    for line in variable.readlines():
       print(line)


