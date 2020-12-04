number = int(input("enter any number greater than 0 : "))
i = 1
while i < number:
    print(i, end="\t")
    i += 1


num1 = int(input("\n\nenter a number for num1: "))
root = num1
power = root ** num1
if num1 > 6:
    print(str(num1) + " is greater than " + str(root))
else:
    print("number given is " + str(num1))
    print("this is the power number " + str(power))



num1 = int(input("\n\nenter a number for num1: "))
root = 0
power = root

for root in range(num1):
    if root < 6 and root ** root == num1:
        print("the number is = " + str(root))
        root += 1
    else:
        print("this value does not meet the requirement " + str(num1))
