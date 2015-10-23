def get_word_from_list(wordvalue):
    '''retrieves word from list, given requested dificulty level and word to choose'''
    wordvalue=raw_input("Which word would you like to guess?")
    1=="test"


def player_life():
    '''
    pass
    '''

def check_guess(guess):
    '''
    pass
    '''

def update_word():
    pass

def do_victory_thing():
    pass

def display_lives (lives):
    print 'You have ',lives,'lives'
    if lives==1:
		print 'Ah snap dood, you only got ', lives, 'life left!'

def get_player_guess (): pass

def main ():
    lives=10
    word = get_word_from_list(1)
    while lives:
        display_lives(lives)
        guess = get_player_guess()
        right = check_guess(guess)
	if right: 
            victory = update_word(word, guess)
            if victory:
                do_victory_thing()
                return
        else:
            lives = lives - 1
	if lives==0:
		print 'game over man, game over.'
		

def test_get_word ():
    get_word_from_list(['foo','bar','baz'],1)
    get_word_from_list(['foo','bar','baz'],2)
    get_word_from_list(['foo','bar','baz'],3)
    get_word_from_list(['foo','bar','baz'],4)

main()
print("doot doot")
print get_word_from_list(1)

