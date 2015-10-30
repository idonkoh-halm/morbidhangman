def get_word_from_list():

    '''retrieves word from a list following a player chosen number that represents a word from that list.'''
    a = ['Mario','Link','Pikachu','Donkey Kong', 'Samus', 'Fox', 'Yoshi', 'Kirby','Luigi','Captain Falcon', 'Ness', 'Jigglypuff']
    

    wordvalue=int(raw_input("Pick a number between 0 and 11."))
    for i in range (1):
            print a[wordvalue]


    '''retrieves word from list, given requested dificulty level and word to choose'''
    wordvalue=int(raw_input("Which word would you like to guess?"))
    if wordvalue==1:
        print 'test'
    if wordvalue==2:
        print 'dad'
        

    
def check_guess (word, guess):
    """Look through word for letter.
    If it is wrong, return False
    If it is right, return True
    """
    search = guess
    word.find(search)
    if guess is in word     
     print 'true'
    elif
    print false
    
    
    pass

    

def update_word():
    pass

def do_victory_thing():
    player=raw_input("What's your name?")
    print player +', you won the game.'
    

def display_lives (lives):
    print 'You have ',lives,'lives'
    if lives==1:
	print 'Ah snap dood, you only got ', lives, 'life left!'

def get_player_guess ():
<<<<<<< Updated upstream
    pass
=======
    raw_input("what is you guess?")
     
>>>>>>> Stashed changes


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
<<<<<<< Updated upstream
    for i in range (12):
        get_word_from_list()
test_get_word()
#main()



=======
    get_word_from_list(['foo','bar','baz'],1)
    get_word_from_list(['foo','bar','baz'],2)
    get_word_from_list(['foo','bar','baz'],3)
    get_word_from_list(['foo','bar','baz'],4)

def test_check_guess ():
    if check_guess('python','a')==False:
        print 'Success'
    else:
        print 'Fail'
    if check_guess('python','t')==True:
        print 'Success'
    else:
        print 'Fail'
    if check_guess('python','T')==True:
        print 'Success'
    else:
        print 'Failed with capital letter'
            


test_check_guess()
>>>>>>> Stashed changes



