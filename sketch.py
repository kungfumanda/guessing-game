import random

print("********************************","Welcome to our guessing game!", "********************************", sep = "\n")
print("Your goal is to guess a random number that's in the 1-100 range\n")

secret_number = int(round(random.randrage(1, 101))) #generates an random number that's between 1-100, round it and cast it into a int

total_tries = 3
tries_left = total_tries
current_turn = 1


for current_turn in range(1,total_tries+1):
        print("this is your turn number {}, be aware you just have {} more tries.".format(current_turn, tries_left))
        tries_left = tries_left - 1

        current_try = int(input("\ntell us your guess"))
        print("You said: ", current_try)
        if (current_try < 1 or current_try >100):
                print("And that's an impossible choice. We're sorry, can you please say a number that's between 1-100?")
                continue

        its_right= current_try == secret_number
        its_higher= current_try > secret_number

        if (its_right):
                print("you actually got it right!! congrats (:")
                break
        else:
                if (its_higher):
                        print ("yeah... not this time. your try is now crossing the sky on it's way to the moon. wanna try again? please, lower this time")
                else:
                        print("this was a good try!! for an ant. please, try again (more like an elephant this time).")


print("this is the end, my friend.")