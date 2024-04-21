from random_word import Wordnik
r = Wordnik()

GoalWord = r.get_random_word(hasDictionaryDef="true", minCorpusCount=20, maxLength=10)
GoalLetters = [*GoalWord]
DontWant = "-"

while DontWant in GoalLetters:
    GoalLetters =  [*GoalWord]

#display as blank
Blanks = []
BlankLength = 0
while BlankLength < len(GoalLetters):
    Blanks.append("__ ")
    BlankLength += 1

#check if letter in word
print('GUESS TO START')
print(''.join(Blanks))
GuessesLeft = 7
Guesses = []
while "__ " in Blanks and GuessesLeft > 0:
    Guess = input()
    if Guess in Guesses:
        print('YOU ALREADY GUESSED THAT, TRY AGAIN')
    elif Guess not in Guesses:
        if Guess in GoalLetters:
            while Guess in GoalLetters:
                Blanks[GoalLetters.index(Guess)] = Guess + ' '
                GoalLetters[GoalLetters.index(Guess)] = "@"
            print('CORRECT')
            print(''.join(Blanks))
        elif Guess not in GoalLetters:
            GuessesLeft -= 1
            print('WRONG, YOU HAVE', GuessesLeft, 'GUESSES LEFT')
            print(''.join(Blanks))
    Guesses.append(Guess)



#End Game
if GuessesLeft == 0:
    print('YOU LOSE TRY AGAIN')
    quit()
elif "__ " not in Blanks:
    print('YOU WIN CONGRATS')
    quit()





