import time
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
    word.find(search) ## Oops -- this line doesn't do anything - TH
    if guess in word:     
        return True
    else:
        return False
       
    pass

def is_complete(guesses, word): #from hinkle extra help
    return guesses==set(list(word))

def do_victory_thing():
    
    player=raw_input("What's your name?")
    print player +', you won the game!'

    

def display_lives (lives):
    print 'You have ',lives,'lives'
    if lives==1:
	print 'The victim seems to be grasping for his final moments of life. He prays to the gods that another petty thief never goes through this ever again. You begin to feel your incompetence run through you. Choose your letter wisely, you only have ', lives, 'guess left.'


def get_player_guess ():
    guess=raw_input("what is you guess?")
    return guess


def main ():
    guesses=set()
    lives=10
    word=get_word_from_list()
    while lives:
        display_lives(lives)
        guess = get_player_guess()
        right = check_guess(word, guess)
	if right:
            print "You got it! There is a(n)",guess
            guesses.add(guess)
            complete = is_complete(guesses, word)
            if complete:
                print 'Your word was',word

                do_victory_thing()
                
                return
        else:
            lives = lives - 1
            if lives==0:
                print 'The chair holding the victim is kicked, securing his fate. A moment passes. Silence.'
                time.sleep(5)
                print 'You monster.'
            
def test_check_guess ():
    if check_guess('python','a')==False:
        print 'Success'
    if lives==0:
        print 'The chair holding the victim is kicked, securing his fate. A moment passes. Silence.'
        time.sleep(5)
        print 'You monster.'
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
    if check_guess('python','T')==True: ## This test still fails -- TH
        print 'Success'
    else:
        print 'Failed with capital letter'
            
def test_is_complete():
    print 'true?', is_complete(set(list('Mario')), 'Mario')
    print 'false?', is_complete(set(list('Mario')), 'Luigi')
    print 'true?', is_complete(set(list('Link')), 'Link')
    print 'false?', is_complete(set(list('Link')), 'Zelda')

#get_player_guess()
#test_is_complete()
#test_check_guess() 
main()
time.sleep(60)
