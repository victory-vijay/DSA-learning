n = 5
for i in range(1, n+1):
    sum = 0
    str1 = ""
    for j in range(1, i+1):
        str1 = str1 + str(j) + "+"
        sum = sum + j
    print(str1[:-1] + "=" + str(sum))
