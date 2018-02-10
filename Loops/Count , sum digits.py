###count digit in number

number = int(input("Enter a number "))
count = 0
while (number > 0):
  number = number//10
  count = count + 1
print (count)


###sum digit in number
num = int(input("Enter a number "))
sum = 0
while(num>0):
    temp=num%10
    sum=sum+temp
    num=num//10
print (sum)
