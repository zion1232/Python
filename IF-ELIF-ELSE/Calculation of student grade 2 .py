Grade=int(input("Enter the Grade "))
Tasks=int(input("Enter the Tasks "))
AVRg=float(input("Enter the AVRg "))
if (Tasks <= 4):
    TotalGrade = Grade;

elif (Tasks > 4 and Tasks < 8):
    TotalGrade = Grade;
    if (Grade >= 60):
      TotalGrade = (int)(0.8*Grade + 0.2*AVRg);
    else:
     TotalGrade = (int)(0.9*Grade + 0.1*AVRg);
else:
    if (Grade >= 60)		:
     TotalGrade = (int)(0.7*Grade + 0.3*AVRg);
    else:
     TotalGrade = (int)(0.6*Grade + 0.4*AVRg);
print("the Grade " , TotalGrade)
