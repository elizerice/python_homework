num = int(input())
students = []
for i in range(num):
    students.append(input())
for student in students:
    if student[-1] == '4' or student[-1] == '5':
        print(student)
