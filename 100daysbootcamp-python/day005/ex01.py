#inout a python list of studnet heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = 0
num_students = 0
for height in student_heights:
    total_height += height
    num_students += 1 
print(f"total height = {total_height}")
print(f"number of students = {num_students}")
print(f"average height = {int(total_height/num_students)}")

