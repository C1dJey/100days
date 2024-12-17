from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)


quiz_brain = QuizBrain(question_bank)

while quiz_brain.has_question():
    quiz_brain.next_quest()

print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")