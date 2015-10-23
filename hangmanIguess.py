def get_word_from_list(dificultylevel,wordvalue):
    '''retrieves word from list, given requested dificulty level and word to choose'''
    pass

def set_lives(x):
    '''sets the number of incorrect guesses a player can make before a game over'''


def player_life():
    '''
    pass

def check_guess(guess):
    '''#checks if letter is in the selected word, and returns true or false.'''
    pass

def update_word():
    pass

def do_victory_thing():
    pass

def display_lives (set_lives):
    print 'You have ',set_lives,'lives'
    if set_lives==1:
		print 'Ah snap dood, you only got ', set_lives, 'life left!'

def get_player_guess (): pass

def main ():
    set_lives(10)
    wordlist = ['foo','bar']
    word = get_word_from_list(wordlist,7)
    while set_lives:
        display_lives(set_lives)
        guess = get_player_guess()
        right = check_guess(guess)
	if right: 
            victory = update_word(word, guess)
            if victory:
                do_victory_thing()
                return
        else:
            set_lives = set_lives - 1
	if set_lives==0:
		print 'game over man, game over.'
		

def test_get_word ():
    get_word_from_list(['foo','bar','baz'],1)
    get_word_from_list(['foo','bar','baz'],2)
    get_word_from_list(['foo','bar','baz'],3)
    get_word_from_list(['foo','bar','baz'],4)

main()
