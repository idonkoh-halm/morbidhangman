def get_word_from_list():
#Get word from list function made by Isaac.
    '''Retrieves word from a list following a player chosen number that represents a word from that list.'''
    a = ['Mario','Link','Pikachu','Donkey Kong', 'Samus', 'Fox', 'Yoshi', 'Kirby','Luigi','Captain Falcon', 'Ness', 'Jigglypuff']
    wordvalue=int(raw_input("Pick a number between 0 and 11."))
    #print a[wordvalue]
    return a[wordvalue]    


def check_guess (word, guess):
    """Look through word for letter.
    If it is wrong, return False
    If it is right, return True
    """
    search = guess
    word.find(search)
    if guess in word:     
        print 'true'
    else:
        print 'false'
    
    
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

    pass
    raw_input("what is you guess?")


def main ():
    lives=10
    word=get_word_from_list()
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
	if 
def test_check_guess ():
    if check_guess('python','a')==False:
        print 'Success'
    else:lives==0:
		print 'game over man, game over.'
        do_victory_thing()
            

def test_get_word ():
    for i in range (12):
        get_word_from_list()
        
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
            

print word
test_get_word()
