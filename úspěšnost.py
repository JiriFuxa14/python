correct_answers = [4 , 3]
user_answers = [4 , 4]
user_points = 0
question_count = len(correct_answers)
for i in range(question_count):
    if correct_answers[i] == user_answers[i]:
        user_points += 1
    else: 
        user_points == user_points

print(user_points, question_count, user_points / question_count * 100)
    