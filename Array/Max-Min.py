arr=[]
for i in range(5):
    arr.append(int(input("add number:")))
    indemax=arr.index(max(arr))

print("The max is at index " ,indemax,"  and its value is ",max(arr))

arr=[]
for i in range(5):
    arr.append(int(input("add number:")))
    indemin=arr.index(min(arr))

print("The max is at index " ,indemin,"  and its value is ",min(arr))

