name = input("What is your name?")
print("Hi there, " + name )
print(name + ", hope your day is going well.")
verify = input("Hi " + name + "! Let me make sure your name is, " + name + "? ")
if verify == "yes":
    print("Great! Let's move on.")
age = int(input("How old are you? "))
print("You are " + str(age) + " years old.") 
location = input("Where are you from? ")
print("Let's recap what we have so far. Your name is " + name + ", you are " + str(age) + " years old, and you are from " + location + ".")

