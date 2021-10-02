# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_of_student_heights = 0
for student_height in student_heights:
  sum_of_student_heights += student_height

total_students = 0
for height in student_heights: 
  total_students += 1

print(f"Sum of all students heights: {sum_of_student_heights} cms.")
average_of_heights = sum_of_student_heights / (total_students)
print(f"Average of all students height = {average_of_heights} cms.")

