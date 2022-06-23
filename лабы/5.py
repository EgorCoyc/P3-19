a = (1,5,-6,3,-4)

summ = 0
summ1 = 0
summ2 = 0
count = 0
count1 = 0
count2 = 0



for i in range(5):
    if a[i] >= 0:
        summ += a[i]
        count +=1
    if a[i] < 0:
        summ1 += a[i]
        count1 +=1
    summ2 +=1
    count2 += 1

print("Nonoxmtenbutx:",summ/count, "OTpuyatensuex:", summ1/count1, "Bcex uncen:", summ2/count2)