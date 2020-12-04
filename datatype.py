import datetime

birth_month = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july" : 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}





#user input details i need

name = input("whats your name: ")
print("enter D-O-B in the following format (yy/mm/dd)")
user_year = input("whats year were you born: ")
user_month = input("whats your birth month: ")
user_day = input("what day: ")

#end of user input

#process and computations

this_year = datetime.date.today().year
this_month = datetime.date.today().month
this_day = datetime.date.today().day

user_actual_year = int(this_year) - int(user_year)
user_actual_month = int(this_month) - int(user_month)
user_actual_day = int(this_day) - int(user_day)

if user_month == birth_month.get("january"):
    user_actual_month = int(this_month) - birth_month.get("january")
elif user_month == birth_month.get("february"):
    user_actual_month = int(this_month) - birth_month.get("february")
elif user_month == birth_month.get("march"):
    user_actual_month = int(this_month) - birth_month.get("march")
elif user_month == birth_month.get("april"):
    user_actual_month = int(this_month) - birth_month.get("april")
elif user_month == birth_month.get("may"):
    user_actual_month = int(this_month) - birth_month.get("may")
elif user_month == birth_month.get("june"):
    user_actual_month = int(this_month) - birth_month.get("june")
elif user_month == birth_month.get("july"):
    user_actual_month = int(this_month) - birth_month.get("july")
elif user_month == birth_month.get("august"):
    user_actual_month = int(this_month) - birth_month.get("august")
elif user_month == birth_month.get("september"):
    user_actual_month = int(this_month) - birth_month.get("september")
elif user_month == birth_month.get("october"):
    user_actual_month = int(this_month) - birth_month.get("october")
elif user_month == birth_month.get("november"):
    user_actual_month = int(this_month) - birth_month.get("november")
elif user_month == birth_month.get("december"):
    user_actual_month = int(this_month) - birth_month.get("december")
else:
    print("input not defined.")

#end of process and computations

print("hello mr/ma "+ name + " you are "+ str(user_actual_year) + " years, " + str(user_actual_month) + " months and "+ str(user_actual_day) + " days old.")

#today_date = (datetime.datetime.now())


#print(today_date)