student_name = input("what is your name: ")
coursework_mark =int(input("what is your coursework score "))
exam_score = int(input("what is your examscore "))


exam_score_out_70 = (exam_score/100)* 70
print(f"Your exam score out of 70 is {exam_score_out_70}")

final_score = float(exam_score_out_70) + coursework_mark
print(f"Your final score is {final_score}")

