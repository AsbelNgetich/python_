

#Ask how many students
#Make a loop that loops the amount of entries
#Enter student name, grade and select a course
#ask to view report when complete.
#If they want a report, print the list.

num_of_students = int(input("How many students do you have? "))

def iscorrect_name(s_name):
    if s_name.isalpha():
        return True
    else:
        return False

def iscorrect_grade(s_grade):
    if s_grade.isnumeric():
        return True
    else:
        return False

def iscorrect_course(s_course):
    if (s_course >= 1) and (s_course <= 3):
        return True
    else:
        return False


def create_student():
    
    student_name = input("Student's Name: ")  
    while(iscorrect_name(student_name)== False):
        student_name = input("You made an Error. Please re-enter Student's Name: ") 

    student_grade = input("student's Grade: ")
    while(iscorrect_grade(student_grade)== False):
        print(student_grade)
        student_grade = input("You made an Error. Please re-enter Student's Grade: ") 


    course_picked = int(input("Select a course: 1 - Math, 2 - Science, 3 - History: "))
    while(iscorrect_course(course_picked) == False):
        course_picked = int(input("You made an Error. Please re-select course: "))

    if course_picked == 1:
        course = "Math"
    elif course_picked == 2:
        course = "Science"
    elif course_picked == 3:
        course = "History"

    student={}
    student["name"] = student_name
    student["grade"] = student_grade
    student["course"] = course 
    return student

whole_class=[]
for i in range(0,num_of_students):
    x = create_student()
    whole_class.append(x)

for s in whole_class:
    print(f"Name: {s['name']}, Grade: {s['grade']}, Course: {s['course']}")

