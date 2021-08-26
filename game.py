import random

number_games = ''

while number_games == '':
    try:
        number_games = int(input('Enter the number of games you want to play: '))
    except:
        print('Enter a number...')
for game in range(0, number_games):
    number_picked = random.randint(1, 25)
    guess = None
    attempts = 0

    while number_picked != guess:
        try:
            guess = int(input('Pick a new number: '))
        except:
            print('Select a number...')
            continue
        if guess != number_picked:
            attempts += 1
        else:
            print('That\'s the number! it took you: %d attempts' % attempts )