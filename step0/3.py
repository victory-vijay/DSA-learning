#    1
#   12
#  123
# 1234

n = 5
for i in range(1, n+1):
    spaces = " "*(n-i)
    str1 = ""
    for j in range(1, i+1):
        str1 = str1 + str(j)
    print(spaces+str1, end=" ")
    print()
