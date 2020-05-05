def raise_num(base_num,power_num):
    result = 1
    for i in range(power_num):
        result *=  base_num
    return result

print(raise_num(base_num=int(input("enter a base number: ")),power_num=int(input("enter a power: "))))

