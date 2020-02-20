print("********************************","Welcome to our guessing game!", "********************************", sep = "\n")
secret_number = 42

try1 = int(input("tell us your first guess"))
print("You said: ", try1)
its_right= try1 == secret_number
its_higher= try1 > secret_number

if (its_right):
        print("you actually got it right!! congrats (:")
else:
        if (its_higher):
                print ("yeah... not this time. your try is now crossing the sky on it's way to the moon. wanna try again? please, lower this time")
        else:
                print("this was a good try!! for a ant. please, try again (more like an elephant this time).")

print("no more tries for you, buddie")