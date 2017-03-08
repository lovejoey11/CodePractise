
def cacmedian(arr):
    if len(arr) % 2 == 0:
        return (arr[int(len(arr) / 2)] + arr[int((len(arr) / 2) - 1)]) / 2
    else:
        return arr[int(len(arr) / 2)]


def insertnum(num, dstarr, currentmedian):
    d = len(dstarr)
    if d == 1:
        if dstarr[0] > num:
            dstarr.insert(0, num)
        else:
            dstarr.insert(1, num)
        #print (dstarr)
        return dstarr
    else:
        farr = dstarr[0:int(d / 2)]
        larr = dstarr[int(d / 2):d]
        # print(farr,larr)
        if num > currentmedian:
            res = farr + insertnum(num, larr, cacmedian(larr))
        else:
            res = insertnum(num, farr, cacmedian(farr)) + larr
        #print (res)
        return res

count = 0
movarr = arr[:d]
sortedmovarr = sorted(movarr)

for i in range(d, n):
    # print(movarr)
    currentmedian = cacmedian(sortedmovarr)
    if arr[i] >= 2 * currentmedian:
        count += 1
    sortedmovarr.remove(arr[i - d])
    # print(sortedmovarr.remove(arr[i-d]))
    sortedmovarr = insertnum(arr[i], sortedmovarr, currentmedian)

    # movarr.pop(0)
    # movarr.append(arr[i])
print(count)
