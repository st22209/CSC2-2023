lolies = int(input("How many lollies do you have? "))
students = int(input("How many students are there? "))

each_student, left_over = divmod(lolies, students)

print(
    f"Give each student {each_student} lollies and there should be {left_over} lollies left over which will go to ME"
)
