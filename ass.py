#  Check if the list is already sorted or not. Ascending or descending
list1=[1,2,3,4,5]
desc=0
acce=0
for i in range(len(list1)-1):
        if(list1[i] > list1[i+1]):
           desc+=1
        elif(list1[i] < list1[i+1]):
           acce+=1

if(acce==len(list1)-1):
    print("acce")
elif(desc==len(list1)-1):
    print("dcce")
else:
    print("not any order")

# 2. Missing number in a list. [1, 2, 3, 5,6,7,9, 8]
# 1. Sum of n numbers using formulae - Sum of elements in list
# 2. 2 loops method
# 3. xor method.
# 4. Sorting
list1=[1,2,3,5,6,7,8,9]
count=1
for i in range(len(list1)):
    if(list1[i]!=count):
        print(count)
        break
    count+=1

# 2 loops
list1=[1,2,3,5,6,7,8,9]

for i in range(1,10):
    mis=True
    for j in list1:
        if i==j:
            mis=False
            break
    if mis:
        print(i)



# xor
list1=[1,2,3,5,6,7,8,9]
res=0
for i in range(1,10):
       res=res^i
       
for j in list1:
        res=res^j
print(res) 

# Sorting
list1=[1,2,3,5,6,7,8,9]
for i in range(len(list1)):
    if(list1[i]!=i+1):
        print(i+1)
        break

         



# Check if an array is a subset of another or not.

arr=[1,2,3,7]
count=0
arr1=[1,2,3,4,5,6,7]
for i in arr:
    if i in arr1:
        count+=1
    else:
        print("not there")
if(count==len(arr)):
    print(True)
else:
    print(False)

# Check if a + b = target exists in a list
list1=[4,5,6,7,3,8,2,4,5,7]
target=9
arr=[]
for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
          if list1[i]+list1[j]==target:
             arr.append([list1[i], list1[j]]) 
        
print(arr)
            



    

    