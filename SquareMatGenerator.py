#module for generating a square matrix
#call matrix(n) where n is the nxn matrix size


def matrix(n):
    myList = []  # initialize list
    for i in range(n): #looping for the entries of the matrix
        Temp_row = [] #temporary storage of entries
        for j in range(n): #for next set of entries
            Temp_row.append(int(input("Enter the matrix entries: ")))
        myList.append(Temp_row)

    for i in range(n): #row
        for j in range(n): #column
            print(myList[i][j], end='')
        print() #for new line


