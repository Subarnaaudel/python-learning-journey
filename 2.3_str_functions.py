


#  login /registration system:

username = input("enter username: ").strip().lower()
password = input("enter password: ").strip()

if len(username)<3:
  print("username is too short")

elif not username.isalnum():
  print("username can contain only letter and numbers")

elif len (password)<8:
  print("password must contain at least 8 characters")

else:
  print("registration sucessfull")


# Most-used Python String Functions/Methods
# len method
name = "subarna"
print(len(name))
print (name.lower())
# real use :
email = input("enter email: ").lower()
if email == "admin@gmail.com":
  print("welcome admin")


# upper method
name = "python"
print(name.upper())


# strip method
print(name.strip())
# real use :
username= input("enter username: ").strip()



# Replace method
text = "I love Java"
new_text = text.replace("Java", "python")
print(new_text)
# real use:
phone = "9848-12-334"
phone = phone.replace("-","")
print(phone)




# split method
text = "python HTML CSS JAVASCRIPT"
languages = text.split()
print(languages)
# example
data = "apple, banana, mango"
fruits = data.split(",")
print(fruits)



# join method
fruit = ["apple", "banana", "mango"]
result = ", ".join(fruit)
print(fruit)



# find method
text = "I love python"
print(text.find("python"))
print(text.find("java"))
# exampple
emails = "user@gmail,com"
if emails.find("@")!= 1:
  print("valid email format")



# count method
texts = "banana"
print(text.count("a"))
# real use 
emailss ="user@gmail.com"
print(emailss.count("@"))



# startsith method
url= "https://google.com"
print(url.startswith("https"))
# real use:
urls = "https://example.com"
if url.startswith("https"):
  print("secure connection")


  # endswith() method
  filename = "photo.jpg"
  print(filename.endswith(".jpg"))
# real use 
filename = "resume.pdf"
if filename.endswith(".pdf"):
  print("PDF file")



# isdidgit method
age = "24"
print(age.isdigit())

age = input("enter your age:")
if age.isdigit():
  print("valid age")
else:
  print("please enter number only")


  # isalpha method
  name = "subarna"
  print(name.isalpha())
  name = "subarna123"
  print(name.isalpha())

# isalnum() method
username = "subarna123"
print(username.isalnum())



# isspace method
text = " "
print(text.isspace())




# title  method
name = "subarna paudel"
print(name.title())



# format () method\
name = "subarna"
age = 24
message = "my name is {} and i am {} years old".format(name,age)
print(message)


name = "hari"
age = 21
print(f"my name is {name} and i am {age} years old")

product = "laptop"
price= 90000
print(f" {product } cost rs .{price}")
