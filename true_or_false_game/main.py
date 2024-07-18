from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions_bank = []

for questions in question_data:
    new_q = Question(questions["question"], questions["correct_answer"])
    questions_bank.append(new_q)

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(questions_bank)}.")
