def greeting(name,age="28"):
  print("Hello " + name + ",you are " + age + "!")
  print(f"Hello {name}, you are {age}!")

name = input ("Enter your name: ")
age = input ("Enter your age: ")
greeting(name,age)
greeting("Judith")

