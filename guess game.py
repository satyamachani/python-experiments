import random
print("you are going to play guess game with computer")
print("rules are as follows")
print("computer guess and you too")
print("if ur guess equals computer guess")
print("you wins")
print("maximum guess allowed are 3")
print("we are strating game......")
print("ready to play with satya's computer")
num = 3
print(num,"guesses are left")
print("Guess the number between 1 to 10")
while True:
    guess = input()
    computer = random.randint(1,10)
    print("you guessed",guess)
    print("computer guessed",computer)
    print()
    if 0<int(guess)<11 and (int(guess) == computer):
        print("hurray! you wins")
        break
    elif num == 1:
        print("No guesses left\n you loose the game")
    else:
        print("sorry guess again")
        num = num-1
        print(num,"guesses left")
        print("guess the number between 1 to 10")
