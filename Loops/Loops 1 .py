
### reverse
num=int(input("enter number"))
reverse=0
while(num>0):
    rem=num%10
    reverse=reverse *10 + rem
    num = num//10
print("sdfdsf" , reverse)


###add the number
num=int(input("enter number"))
newnumber = 0
addnumber=int(input("Enter a digit you want to add to the end of the number "))
newnumber=num * 10 + addnumber;
print("Your number is " , num , ".You have chosen to add the number " , addnumber ,".Your final number is" , newnumber)


###only the odd  number
newnumber = 0
location = 1
num=int(input("enter number"))
temp = num
while (temp>0):
        digit = temp % 10
        if (digit % 2 == 1):
              newnumber += digit*location
              location *= 10
        temp //= 10

print("orgin number is" , num , ". and only the odd  number are \n " , newnumber)


###only the even  number
newnumber = 0
location = 1
num=int(input("enter number"))
temp = num
while (temp>0):
        digit = temp % 10
        if (digit % 2 == 0):
              newnumber += digit*location
              location *= 10
        temp //= 10

print("orgin number is" , num , ". and only the even  number are \n " , newnumber)

