# write a program to greet al the person name stored in a list "t" and which starts with S.l=["subarna","Ramesh","Soham","Sachin","Rahul"]


l=["Subarna","Ramesh","Soham","Sachin","Rahul"]
for name in l:
  if(name.startswith("S")):
    print(f"Hello {name}")
