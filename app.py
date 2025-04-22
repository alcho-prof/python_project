import random
print("Welcome to the number guessing game\nRules:\n You have 7 guesses and you have to guess it correctly\n let the game begins\ngood luck")
guess=random.randrange(100)
chance=7
i=0

while i<chance:
    i+=1
    my_guess=int(input("Enter your guess : "))
    if guess==my_guess:

        print(f"Congratulations!!!!!\nthe number is {guess} \nyou have guessed it correctly!!!!")
    elif i>=chance and my_guess!=guess:
        print(f"Oops!!!!!!!sorry,Better luck next time\n You have guessed it wrong\n the number is {guess}")    
    elif my_guess>guess:
        print("Your guess is higher.Try to guess lower number")   
    elif my_guess<guess:
        print("Your guess is lesser,guess a higher number")    
