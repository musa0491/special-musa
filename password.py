import re

def password_test():
    keyword = input("enter a keyword: ")

    if int(len(keyword)) >= 8:
        if keyword != re.search("\w", keyword):
            print("invalid add lower case letter to your password: ")
        elif keyword != re.search("\w", keyword):
            print("invalid add uppercase letter to your password")
        elif keyword != re.search("\w", keyword):
            print("invalid! add numbers to your password.")
        else:
            print("good password congratulations!")
    else:
        print("password not supported too short. ")

password_test()

