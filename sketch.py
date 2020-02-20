print("********************************","Welcome to our guessing game!", "********************************", sep = "\n")
secret_number = 42

try1 = int(input("tell us your first guess"))
print ("You said: ", try1)

if (try1 == secret_number):
        print("you actually got it right!! congrats (:")
else:
        print ("yeah... not this time. wanna try again?")

print("no more tries for you, buddie")