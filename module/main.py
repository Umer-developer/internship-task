import myfirstmodule
import re

person=myfirstmodule.person1
print(person)

person=myfirstmodule.person2["age"]
print(person)

person=myfirstmodule.person3["name"]
print(person)

#REgEXpressions

x = re.findall("ali", person)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")