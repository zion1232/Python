num=int(input("enter number"))
loc = 1
binary = 0
while (num>0):
    numleft = num % 2
    num //= 2
    binary += loc*numleft
    loc *= 10
print(  binary) 
