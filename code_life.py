y = 1919
# your code goes here
days = [31, 0, 31, 30, 31, 30, 31, 31]
if y < 1917:  # julian
    if y % 4 == 0:  # leap year
        days[1] = 29
    else:
        days[1] = 28
elif y > 1919:  # Gergorian
    if ((y % 4 == 0) & (y % 100 != 0)) | (y % 400 == 0):  # leap
        days[1] = 29
    else:
        days[1] = 28
else:  # trans
    days[1] = 15
i = 1
sumday = 0
for num in days:
    if sumday < 228:
        sumday += num
        i += 1
    else:
        break

print('%d.0%d.%d' % ((256 - sumday), i, y))
