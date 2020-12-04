n = int(input("enter any value for n: "))
for i in range(n):
    if i < 6 and i**1 == n:
        print(i, end="\t")
        i -= 1
    else:
        print(str(i) + " non is equal to that task: ")
else:
    print(" number greater than the range given:")