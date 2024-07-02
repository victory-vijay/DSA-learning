# 5
# 45
# 345
# 2345
# 12345
n = 5

for i in range(n):
    string = ""
    for j in range(i, -1, -1):
        print(n-j-1, end=" ")
    print()
