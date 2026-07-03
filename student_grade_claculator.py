English=int(input("Enter your English marks: "))
Math=int(input("Enter your Math marks: "))
Science=int(input("Enter your Science marks: "))
French=int(input("Enter your French marks: "))
Python=int(input("Enter your Python marks: "))
Total_marks=English+Math+Science+French+Python
Average_marks=Total_marks/5
print("Total marks:",Total_marks)
print("Average marks:",Average_marks)
if Average_marks>=90:
    print("Grade: A")
elif Average_marks>=80:
    print("Grade: B")
elif Average_marks>=70:
    print("Grade: C")
elif Average_marks>=60:
    print("Grade: D")
else:
    print("Grade: F")
if Average_marks<50:
    print("You have failed the exam.")