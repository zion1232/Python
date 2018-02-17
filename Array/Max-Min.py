max=0
arr=[]
for i in range(5):
    arr.append(int(input("add number:")))
if arr[i]>arr[max]:
    max=i
print("The max is at index " ,max ,"  and its value is ",arr[max])


min=0
arr=[]
for i in range(5):
    arr.append(int(input("add number:")))
if arr[i]<arr[min]:
    min=i
print("The min is at index " ,min ,"  and its value is ",arr[min])

