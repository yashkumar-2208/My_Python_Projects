import random

questions = [
    ["Who is Shah Rukh Khan?", "WWE","Actor","Astronut","Joker",2],
    ["What is the capital of France?", "Earth", "Seoul","Delhi", "Paris",4],
    ["What is the square of 2?", "4","10","30","40",1]
]

prizes = [10000000, 20000000, 5000000, 600000]


i = 0
for question in questions:

    print(question[0])

    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d: "))

    if(a == question[5]):
        print("Correct Answer")
    else:
        print(f"Incorrect, the correct answer was: {question[5]}")
        print("Better luck next time!")
        break
    print(f"You won {prizes[i]} ")
    i += 1