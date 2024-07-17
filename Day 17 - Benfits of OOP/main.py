# class User:
#     def __init__(self, name, age, race):
#         self.name = name
#         self.age = age
#         self.race = race

# user1 = User("Talal", 34, "African-American")


# print(user1.name)
# print(user1.age)
# print(user1.race)


# user2 = User("Neet", 18, "Indian")
# # user2.name = "Neet"
# # user2.age = 18
# # user2.race  = "Indian"

# print(user2.name)
# print(user2.age)
# print(user2.race)

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question = Question(i["text"], i["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_quesion:
    quiz.next_question()
