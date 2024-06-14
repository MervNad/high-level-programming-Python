#input a list of student scores

student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
my_score = 0
for score in student_scores:
    if(score > my_score):
        my_score = score
    else:
        my_score = my_score
print(f"The Highest score in the class is: {my_score}")
