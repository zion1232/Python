import random
count =0
number=random.randint(0,10)
while True:
    num=int(input("enter number - "))
    if(number==num):
        print("You found the number ")
        print("The number of guesses is - ",count)
        break
    else:
        count=count+1
    if(number<num):
        print("The number you chose is too large, try a smaller number")
    if(number>num):
        print("The number you chose is too small, try a larger number")
