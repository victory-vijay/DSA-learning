# 1
# 01
# 101
# 0101
# 10101
n = 5
k = "1"
for i in range(1, n+1):
    print(k)
    if (k[0] == "1"):
        k = "0" + k
    else:
        k = "1" + k
