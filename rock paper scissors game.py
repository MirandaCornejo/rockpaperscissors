rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#code below this line 
import random
game=random.randint(1,3)

print("Welcome to rock, paper, scissors game!")
print("To play you have to choose an option...")
x=str(input("Rock, Paper, or Scissors?:"))

if game==1:
  print(rock)
  if x=="rock":
    print(rock)
    print("Its a tie!")
  elif x=="paper":
    print(paper)
    print("You win!")
  elif x=="scissors":
    print(scissors)
    print("You lose :(")
  else:
    print("play again")
elif game==2:
  print(paper)
  if x=="rock":
    print(rock)
    print("You lose :(")
  elif x=="paper":
    print(paper)
    print("Its a tie!")
  elif x=="scissors":
    print(scissors)
    print("You win!")
  else:
    print("play again")
elif game==3:
  print(scissors)
  if x=="rock":
    print(rock)
    print("You win!")
  elif x=="paper":
    print(paper)
    print("You lose :(")
  elif x=="scissors":
    print(scissors)
    print("Its a tie!")
  else:
    print("play again")
else:
  print(...)