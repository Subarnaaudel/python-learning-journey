#  write a progrm to find whether a given username contains less than 10 character or not


username = input("enter your username:")

if(len(username)<10):
  print("your username contain less than 10 characters")

else:
  print("your username contain more than 10 character")