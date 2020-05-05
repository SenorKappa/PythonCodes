# create = input("Enter candisse: " )
# myfile = open(create + ".txt" ,"w+")
# for line in range(5):
#     #myfile.write("this is line %i\n" %(line+1))
#     myfile.write(input("Enter whatever u want: %i" %(line+1)) + "\n")
#
# myfile.close()

def foo(myfile):

    create = open(myfile + ".txt", "w+")
    n = int(input("enter number of lines: "))
    for line in range(n):
        create.write(input("write anything %i" % (line+1) ) + "\n")

    create.close()




