name=input("enter the name: ")
english=int(input("enter the english_marks: "))
math=int(input("enter the math_marks : "))
science=int(input("enter the science_marks: "))

total=english+math+science
average=total/3

print("\n Student Marksheet")
print("----------")
print("Student name:",name)
print("Total_marks",total)
print("Average:",average)
