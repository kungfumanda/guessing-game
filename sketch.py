print("********************************","Welcome to our guessing game!", "********************************", sep = "\n")
secret_number = 42
total_tries = 3;
current_turn = 0;


while(total_tries > 0):
        current_turn = current_turn + 1
        print("this is your turn number {}, be aware you just have {} more tries.".format(current_turn, total_tries))
        total_tries = total_tries - 1

        current_try = int(input("tell us your guess"))
        print("You said: ", current_try)

        its_right= current_try == secret_number
        its_higher= current_try > secret_number

        if (its_right):
                print("you actually got it right!! congrats (:")
        else:
                if (its_higher):
                        print ("yeah... not this time. your try is now crossing the sky on it's way to the moon. wanna try again? please, lower this time")
                else:
                        print("this was a good try!! for an ant. please, try again (more like an elephant this time).")


print("no more tries for you, buddie")