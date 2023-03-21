from art import logo, vs
from game_data import data
import random

data_list = []
for d in data:
    data_list.append(d)

print(logo)
score = 0
isTrue = True
while isTrue:
    a = random.choice(data_list)
    data_list.remove(a)
    print(f"Compare A: {a['name']}, {a['description']}, {a['country']}")
    print(vs)
    b = random.choice(data_list)
    data_list.remove(b)
    print(f"Against B: {b['name']}, {b['description']}, {b['country']}")
    answer = 'a' if a['follower_count'] > b['follower_count'] else 'b'
    entered_answer = input("Who has more followers? Type A or B : ").lower()
    if answer == entered_answer:
        score += 1
        print(f"Thats true! Current score : {score}\n")
    else:
        isTrue = False
        print(f"Sorry, its wrong! Your score is : {score}")
