import random
from words import wordList
from images import stages, logo


print(logo)
chosenWord = random.choice(wordList)
lettersRemaining = len(chosenWord)
lives = 6
print(f'chosen word is {chosenWord}')
result = ["_" for letter in chosenWord]
gameWon = False

while not gameWon:
	guess = input("guess a letter: ").lower()
	correctGuess = False
	alreadyGuessed = False

	for i in range(0, len(chosenWord)):
		if chosenWord[i] == guess:
			if result[i] == "_":
				result[i] = guess
				lettersRemaining -= 1
				correctGuess = True
			else:
				alreadyGuessed = True
			

	gameWon = lettersRemaining == 0

	if alreadyGuessed:
		print(f'you have already guessed {guess}')

	elif not correctGuess:
		lives -= 1
		print('Wrong guess')
		print(stages[lives])
		if lives == 0:
			break
	print(result)

if gameWon:
    print("You win")
else:
    print("You lose")





