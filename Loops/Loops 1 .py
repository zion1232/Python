
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
