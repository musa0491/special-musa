import re

keyword = input("enter your chioce keyword: ")
check = re.search("\w", keyword)
correct = False

while correct:
    if int(len(keyword)) <= 8:
        if re.search("\w", keyword):
            print("congratulations")
        elif not keyword == re.search("\w", keyword):
            print("keyword weak add lowercase letters:")

        elif not keyword == re.search("\w", keyword):
            print("keyword not valid add uppercase:")

        elif not keyword == re.search("\w", keyword):
            print("keyword not valid add uppercase and numbers:")

        else:
            print("congratulation you made a strong password!")
else:
        print("password too short its not acceptable:")



