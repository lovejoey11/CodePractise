import sys


a = sorted(a)
b = sorted(b)
mut = int(b[0] / a[-1])
count = 0
subcount = 0
if mut >= 1:
    for i in range(1, mut + 1):
        for num in b:
            if num % (a[-1] * i) == 0:
                subcount += 1
                print(a[-1] * i)
        if subcount == len(b):
            count += 1
            #subcount =0
        subcount = 0
    print(count)
else:
    print(0)
