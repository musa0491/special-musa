a = int(input("enter value for a: "))
b = int(input("enter value for b: "))
c = int(input("enter value for c: "))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print("value not defined")
