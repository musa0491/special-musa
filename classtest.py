start = 2
number = 1000

for i in range(start, number):
    if i>1:
        for j in range(2, i):
            if (i % j ==0):
                break
            else:
                print(i)
