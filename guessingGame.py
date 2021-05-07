print("Number guessing game")
print("Enter a number (between 1 and 9)")
guess = int(input("Enter your guess:- "))
number = 9
chances = 0

while chances < 5:
    guess = int(input("Enter your guess:- "))
    
    if guess == number:
        print("Congratulations! You won")
    elif guess < number:
        print("Your guess was too low: Guess a number higher than ",guess)
    chances = chances + 1

if chances > 5:
    print("You lose!!! The number is ",number)




