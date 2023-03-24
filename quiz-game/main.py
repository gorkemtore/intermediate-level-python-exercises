from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(text=q_text, answer=q_answer)
    question_bank.append(new_question)

random.shuffle(question_bank)  # mixes the question bank array

quiz_brain = QuizBrain(question_bank)

while quiz_brain.has_next_question():
    quiz_brain.next_question()

print(f"You completed the quiz. Your final score: {quiz_brain.score}/{quiz_brain.question_number}")