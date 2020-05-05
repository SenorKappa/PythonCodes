
name = input("Enter File name: ") #initialize file name
file = open(name +".txt","w+") #Initialize file itself
file.close() #close open file
container = [] #initialize list to be appended to the text file

n = int(input("Specify the size of the square matrix: ")) # size of the square matrix
for i in range(n):  # looping for the entries of the matrix
    Temp_row = []  # temporary storage of entries
    for j in range(n):  # loop for matrix entries
        Temp_row.append(int(input("Enter the matrix entries: ")))
    container.append(Temp_row)

#for viewing
# for i in range(n):  # row
#     for j in range(n):  # column
#         print(container[i][j], end='')
#     print()  # for new line


file = open(input("Enter the file name w/ file extension: "), "a")
file.writelines(str(container))
