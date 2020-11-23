
number_of_students = int(input('How many students!'))

for i in range(number_of_students):
  grades = input(('Enter student grades.'))
  student_grades.append(list(grades))

avg=[]

for i in range(len(student_grades)):
  for j in range(len(student_grades[i])):
    a = 0
    if j==0 and j ==1:
      a += student_grades[i][j]*0.3
    else:
      a += student_grades[i][j]*0.4 
      avg.append(a)

print(avg)