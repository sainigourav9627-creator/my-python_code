
print("------Student Details--------")

name=input("\nenter the name: ")
age=int(input("enter the age : "))
city=input("enter the city: ")
print(f"Student Name  : {name} ")
print(f"Age           : {age}  ")
print(f"City          : {city} ")

print("\n------Student Marks--------")
python_marks=int(input("\nenter the python marks          : "))
html_marks=int(input("enter the html marks            : "))
css_marks=int(input("enter the csss marks            : "))
sql_marks=int(input("enter the sql marks             : "))
english_marks=int(input("enter the english marks         : "))
print(f"Python_Marks             : {python_marks}  ")
print(f"Html_Marks               : {html_marks}    ")
print(f"Css_Marks                : {css_marks}     ")
print(f"Sql_Markss               : {sql_marks}     ")
print(f"English_Marks            : {english_marks}")

total_marks=python_marks+html_marks+css_marks+sql_marks+english_marks
print(f"Total_Marks: = {total_marks}")

percentage=total_marks/5
print(f"Percentage: = {percentage}")

if percentage>=33:
 print("Pass")
else:
    print("Fail")
    
if percentage>=90:
    print("Grade A")
