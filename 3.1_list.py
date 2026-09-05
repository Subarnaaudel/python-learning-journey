friends = ["apple", "orange", 5,345.06,"Akash","ROhan"]
print(friends[0])
friends[0]="Grraphs" # list are muteable changeable
print(friends[0])
print(friends[0:4])

# adding in last
friends.append("subarna")
print(friends)


# sorting the value
l1 =[1,2,3,4,5,6,7,43,2,556,43,5,6,3,3,445,345]
l1.sort()
print(l1)


# reversing the value
l1 =[1,2,3,4,5,6,7,43,2,556,43,5,6,3,3,445,345]
l1.reverse()
print(l1)

# inserting the value 
l1 =[1,2,3,4,5,6,7,43,2,556,43,5,6,3,3,445,345]
l1.insert(3, 3333)
print(l1)



# deleting the value from this index
l1 =[1,2,3,4,5,6,7,43,2,556,43,5,6,3,3,445,345]
l1.pop(3)
print(l1)




