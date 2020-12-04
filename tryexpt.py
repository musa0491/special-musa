#this code is written to print out the largest odd number in
#if given three different values
print("code by Musa Friday ")

numa = int(input("enter a value for A: "))
numb = int(input("enter a value for B: "))
numc = int(input("enter a value for C: "))

if numa > numb and numa > numc and numa % 2 == 1:
    print(str(numa) + " is largest odd number: ")
elif numb > numa and numb > numc and numb % 2 == 1:
    print(str(numb) + " is largest odd number: ")
elif numc > numa and numc > numb and numc % 2 == 1:
    print(str(numc) + " is largest odd number:")
elif numa > numb and numa > numc and numa % 2 == 0:
    print(str(numa) + " is largest of all input was even numbers.")
elif numb > numa and numb > numc and numb % 2 == 0:
    print(str(numb) + " is largest of all input was even numbers.")
elif numc > numa and numc > numb and numc % 2 == 0:
    print(str(numc) + " is largest of all input was even numbers.")
else:
    print("syntax error please try again.")



