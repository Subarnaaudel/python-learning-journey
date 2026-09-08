# project1: snake , water , Gun game
# we all have played snake , water gun game in our childhood . if you haven't , google the rules of this game and write a python program capable of playing this game with the user.
import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([1, -1 , 0])
youstr = input("enter your choice(s/w/g): ")
youDict = {
  "s":1,
  "w":-1,
  "g": 0
  }

you = youDict[youstr]

if(computer == you):
  print("its a draw!")
elif(computer == -1 and you ==1):
 print("you draw")
elif(computer == -1 and you ==0):
  print("you loose:")
elif(computer ==1 and you ==-1):
  print("you loose")
elif(computer == 1 and you ==0):
  print("you win")
elif(computer == 0 and you ==-1):
  print("you win")
elif(computer == 0 and you ==1):
  print("you loose ")


else:
 print("something wrong")