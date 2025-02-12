# 1 
# 1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,"",end="")
    print()
# 0
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0
for i in range(n):
    for j in range(i+1):
        print((i+j)%2,"",end="")
    print()
# * * * * *
#  * * * * *
#   * * * * *
#    * * * * * 
#     * * * * *
for i in range(n):
    for k in range(i):
        print(" ",end="")
    for j in range(n):
        print("* ",end="")
    print()




