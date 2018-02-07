Sum=int(input("Enter the sum of the products "))
Products=int(input("Enter the products "))
Dis1 = Sum - (Sum / 300) * 50;
if (Products >= 3):
 Dis2 = (int) (0.8 * Sum);
else:
 Dis2 = Sum;
if (Dis1 < Dis2):
    print("please pay " , Dis1 , "NIS after dicount 1\n");
else:
	
 print("please pay " , Dis2 , "NIS after dicount 2\n");



