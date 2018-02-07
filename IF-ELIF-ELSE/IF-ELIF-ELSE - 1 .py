num_rooms=int(input("eenter the num of rooms 3-4-5 "))
if (num_rooms==3):
    price = 120;
elif (num_rooms==4):
    price = 150;
else:
    duplex=int(input("is duplex?"))
    if(duplex==1):
        price = 200;
    else:
        price = 180;

print("please py me nis \n", price);





