n = 5
li = [2*i+1 for i in range(n)]
print(str("".join(map(str, li))))
for i in range(1, n):
    li = "".join(map(str, li[1:])) + str(li[0])
    print(li)
