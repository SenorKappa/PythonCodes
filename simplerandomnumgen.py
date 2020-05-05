import random

def rand_num_gen(num1,num2):
    a = []
    for i in range(num2):


        a.append(random.randint(num1,num2))
        return a



print(rand_num_gen(num1 = int(input("enter a min: ")),num2 = int(input("enter a max: "))))
