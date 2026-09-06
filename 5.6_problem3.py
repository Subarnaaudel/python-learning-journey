#  A spam comment is defined as a text containing following keywords: "make a lot of money", "buy it", "subscribe this ", "click this ". Write a program to detect these spams.

p1= "make a lot of money"
p2 = "buy it"
p3 = "subscribe this"
p4= "click this"

message = input("enter your comment: ")

if(p1 in message or p2 in message or p3 in message or p4 in message):
  print("this messge is spam :--", message)

else:
  print("message is correct and not spam " , message)

