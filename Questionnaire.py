from QuestionClass import Tanong
import re

Questions = [
    "What is the color of a pineapple \nA. BLACK \nB. BLUE \nC. Yellow ",
    "What year is it? \nA. 2020 \nB. 2019 \nC. 2077",
    "What is an animal that barks? \nA. Dog \nB. Cat \nC. Cow"
]

Question_Prompts = [
    Tanong(Questions[0],"C"),
    Tanong(Questions[1],"A"),
    Tanong(Questions[2],"A"),
]

def examination(Question_Prompts):
    score = 0
    for line in Question_Prompts:
        answer = input(line.Question)
        if answer == line.Answer:
            score += 1
    print("your score is " + str(score) + " out of " + str(len(Question_Prompts)))

examination(Question_Prompts)
