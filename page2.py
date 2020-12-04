# number = int(input("enter any decimal number: "))
# while number == 0 or 1:
#     if int(number) >= 2:
#         bin_eqv = int(number) % 2
#         print(bin_eqv)
#
#
#     else:
#         print("number already in binary state")

def conv_to_binary(num):

    if num != 1:
        conv_to_binary(int(num) // 2)
        print(num % 2 , end="")
    print(conv_to_binary(num)

num = int(input("enter any decimal value: "))
conv_to_binary(num)


# if __name__ == "__main__":


reply = input("do you want to ship a parkage? (yes or no) ")
check = reply.upper()
if check == "YES":
    print("we can help you ship the parkage")
elif check == "NO":
    print("we cant ship your product")
else:
    print("unknown operation")