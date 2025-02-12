# transpose
matr=[[1,2,3,5],[7,8,3,5],[3.3,5.5,2,1],[3,4,5,6]]
for i in range(len(matr)):
    for j in range(i):
        matr[i][j],matr[j][i]=matr[j][i],matr[i][j]
print(matr)

# add two matrices
matr=[[1,2,3],[7,8,3],[3,5,2]]
matr1=[[4,5,6],[9,8,7],[1,1,3]]
matr3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matr)):
    for j in range(len(matr[i])):
        matr3[i][j]=matr[i][j]+matr1[i][j]
print(matr3)

# Diagonal sum
matr=[[1,2,3],[7,8,3],[3,5,2]]
sum=0
sum1=0
for i in range(len(matr)):
    sum+=matr[i][i]
    sum1+=matr[i][len(matr) - 1 - i] 


print(sum,sum1)


