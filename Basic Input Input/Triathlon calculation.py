SWIMMING = 1.5
RUNNIG =40
RIDING = 10

Swimming_speed=float(input("enter Swimming_speed"))
Running_speed=float(input("enter Running_speed"))
Speed_riding=float(input("enter Speed_riding"))

Swimming_time = SWIMMING/Swimming_speed
Running_time = RUNNIG/Running_speed
time_riding = RIDING/Speed_riding


total = Swimming_time + Running_time + time_riding;
		
		
		
print("Swimming_time -  " ,Swimming_time );
print("Running_time -  " , Running_time );
print("time_riding -  ", time_riding );
print("total -  " , total );
		
