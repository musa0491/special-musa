# def getDoubleAlphabet(alphabet):
#     doubleAlphabet = alphabet + alphabet
#     return doubleAlphabet()
# alphabet = "ABC"
#
#
# def getmessage():
#     stringToEncrypt = input("please enter a message to encrypt: ")
#     return stringToEncrypt
#
# def getCipherKey():
#     shiftAmount = input("please enter a key (whole number from 1-25): ")
#     return shiftAmount



def add_nums(num1, num2):
    num1 = int(input("enter any number for num1: "))
    num2 = int(input("enter any number for num2: "))
    summn = (num1 + num2)
    return summn
add_nums("num1", "num2")

average = add_nums("num1", "num2")/2
print(average)


#python conditional statement code for AWS

def conditional():
    banana = int(input("enter the number of banana: "))
    if banana >= 5:
        print(str(banana) + " your bunch is large.")
    elif banana <= 4:
        print(str(banana) + " your bunch is small. ")
    else:
        print(str(banana) + " you dont have any banana")

conditional()

#python code to print i love you four times
counter = 0
while counter <= 3:
    print("i love python. ")
    counter += 1


#while loop to print 1 to eleven
number = 0
while number <= 12:
    print(number)
    number += 1
print("upper while loop in one line of code! ")

# num = 11
for i in range(12): print( i + 1)

number 