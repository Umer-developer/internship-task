class Person:
  def __init__(User, name, age):
    User.name = name
    User.age = age


  def myfunc(User):
    print("Hello my name is " + User.name)
    print("my age is :",User.age)

p1 = Person("Umer",21)
p1.myfunc()