PRICE_FOR_PAPER = 5;
taxes =1.18;
EXTRA_SIZE= 1.12;

price=float(input("enter price"))
Box_width=float(input("enter Box_width"))
Box_depth=float(input("enter Box_depth"))
Box_height=float(input("enter Box_height"))



#You have to double it twice because it's a box with 6 corners
Box_size =  (Box_width*Box_height + Box_width*Box_depth + Box_height*Box_depth) * 2 * EXTRA_SIZE;  
total_price = price + Box_size * PRICE_FOR_PAPER;

print("You need to pay " , total_price , " NIS");

#Calculate the price of a packaging product box and consider bottles including taxes
