
attendance=int(input("Enter the attendance "))
if (attendance < 80):
 finalGrade = 0;
 print("the Grade is " , finalGrade)
else:
 examGrade=int(input("Enter the examGrade "))
if (examGrade < 60):
 finalGrade = examGrade;    
 print("the Grade is " , finalGrade)
else:
 middleExam=int(input("Enter the middleExam "))
 tempGrade = 0.8*examGrade + 0.2*middleExam;
if(tempGrade < examGrade):
 tempGrade = examGrade
hwGrade=int(input("Enter the hwGrade "))
finalGrade = 0.1*hwGrade + 0.9*tempGrade;
print("the grade is " , finalGrade)



