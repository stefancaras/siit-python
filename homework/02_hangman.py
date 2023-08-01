import random

pics = ['  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========',
        '  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========',
        '  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========',
        '  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========',
        '  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========',
        '  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========',
        '  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========']
words = ['crocodile', 'monkey', 'tiger', 'snake', 'armadillo', 'cockroach', 'hornet', 'butterfly']
word = [*words[random.randint(0, 7)]]
hidden = [*'_' * len(word)]
tries = [word[0], word[-1]]
lives = 6


def replace(char):
    for i in range(len(word)):
        if word[i] == char:
            hidden[i] = char


# Replace first and last characters in hidden word
replace(word[0])
replace(word[-1])

while True:
    # Print stuff
    print(pics[lives])
    print(''.join(hidden))
    print(f"Guesses: {', '.join(tries)}")
    # Check if you won or lost
    if ''.join(word) == ''.join(hidden):
        print("You won!")
        break
    if lives == 0:
        print("You lost, game over.")
        print(f"The word was {''.join(word)}.")
        break
    # Get input
    print('=============================')
    guess = input('Please enter a character: ').lower()[0]
    # Test situations
    if guess in tries:
        print("You've already tried that.")
        continue
    elif not guess.isalpha():
        print("Please enter only English letters.")
        continue
    elif guess in word:
        print("Good guess.")
        replace(guess)
    else:
        print("Wrong guess.")
        lives -= 1
    # Add guess to the list of guesses
    tries.append(guess)
