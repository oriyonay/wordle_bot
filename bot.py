import random

# get words from word list:
words = [w.strip() for w in open('five_letter_words.txt').readlines()]
more_than_two_vowels = lambda word: sum(word.count(v) for v in 'aeiou') > 2

# list of letters in the word
in_word = set()

num_guesses = 1
while len(words) > 1:
    # make a guess. first guess is an 'educated' guess to get vowel placement:
    if num_guesses == 1:
        guess = random.choice(list(filter(more_than_two_vowels, words)))
    else:
        guess = random.choice(words)
    print('guess %d: %s' % (num_guesses, guess))

    print('input x for bullseye, - for total miss, o for wrong location:')
    feedback = input().lower()

    # process feedback:
    for i, (letter, mark) in enumerate(zip(guess, feedback)):
        if mark == 'x':
            in_word.add(letter)
            words = list(filter(lambda w: w[i] == letter, words))
        elif mark == 'o':
            in_word.add(letter)
            words = list(filter(lambda w: w[i] != letter and letter in w, words))

    for letter in guess:
        if letter not in in_word:
            words = list(filter(lambda w: letter not in w, words))

    if len(words) > 1:
        print('narrowed down to %d words\n' % len(words))

    num_guesses += 1

if len(words) == 1: print('final guess: %s' % words[0])
else: print('no words in the dictionary fit!')
