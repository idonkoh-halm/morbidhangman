def get_word_from_list():
    '''retrieves word from list, given requested dificulty level and word to choose'''
    wordvalue=int(raw_input("Which word would you like to guess?"))
    if wordvalue==1:
        print 'test'
    if wordvalue==2:
        print 'dad'

def check_guess(guess):
    '''
    pass
    '''

def update_word():
    pass

def do_victory_thing():
    player=raw_input("What's your name?")
    print player +', you won the game.'
    

def display_lives (lives):
    print 'You have ',lives,'lives'
    if lives==1:
		print 'Ah snap dood, you only got ', lives, 'life left!'

def get_player_guess (): pass


def main ():
    lives=10
    while lives:
        display_lives(lives)
        guess = get_player_guess()
        right = check_guess(guess)
	if right: 
            victory = true
            if victory:
                do_victory_thing()
                return
        else:
            lives = lives - 1
	if lives==0:
		print 'game over man, game over.'
        do_victory_thing()
        

def test_get_word ():
    get_word_from_list(['foo','bar','baz'],1)
    get_word_from_list(['foo','bar','baz'],2)
    get_word_from_list(['foo','bar','baz'],3)
    get_word_from_list(['foo','bar','baz'],4)

main()
print("doot doot")
get_word_from_list()


