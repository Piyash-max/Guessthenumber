print("Number guessing game")
print("Guess a number(between 5 and 9)")
guess=3
chances=3 
number=(int(input("Enter your guess: ")))
while chances < 5:
    if(number<guess):
        print("The number entered by u is low")
        number=(int(input("Enter your guess: ")))
    elif(number>guess):
        print("The number entered by u is high")
        number=(int(input("Enter your guess: ")))
    elif (number==guess):
        print("CONGO!! U HAVE GUESSED THE RIGHT NUMBER.")
        break
if not chances < 5:
    print("U lose!!")
