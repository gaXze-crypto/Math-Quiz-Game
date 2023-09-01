
import random
\
x = 1 
score = 0
while x < 11:
    number1 = random.randint(1,12)
    number2 = random.randint(1,12)
    correct_answer = number1 * number2
    user_answer = int(input(f"{x}. What is {number1} times {number2}? \n"))
    if(correct_answer == user_answer ):
      print("Correct answer")
      score = score + 1
    else:
      print(f"Wrong answer the answer is {correct_answer}")
    x = x + 1
print(f"Your total score is {score}")
if(score > 7 and score < 10):
  print("very good")
if(score > 5 and score < 8):
  print("good but you can do better")
if(score == 5):
  print("you got half of the questions correct, hope you can get the rest next time")
if(score == 10):
  print("Amazing, you got a perfect score, you're a genius")
if(score < 5):
  print("Below average that's not too good, better luck next time")
"""
x = 0 
while x < 10:
    print(x)
    x = x + 1
    
def arithmetic(a,b,c):
        result = a+b-c
        return result 
print(arithmetic(10,13,14))
"""