print("Number guessing game")
print("Guess a number(between 5 and 9)")
guess=3
chances=5
number=(int(input("Enter your guess: ")))
if (number<guess):
    print("The number entered by u is low")
elif (number>guess):
    print("The number entered by u is high")
elif (number==guess):
    print("CONGO!! U HAVE GUESSED THE RIGHT NUMBER.")

        
