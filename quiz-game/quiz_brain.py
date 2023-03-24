class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def has_next_question(self):

        return self.question_number < len(self.question_list)

    def next_question(self):
        entered_answer = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False) : ")
        self.question_number += 1
        check = entered_answer.title() == self.question_list[self.question_number-1].answer
        if check:
            self.score += 1
            print(f"It's correct. Current score : {self.score}/{self.question_number}")
        else:
            print(f"It's wrong. Current score : {self.score}/{self.question_number}")
        print()
        return check



