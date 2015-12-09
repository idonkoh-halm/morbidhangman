import time
import random
def get_word_from_list():
#Get word from list function made by Isaac.
    '''Retrieves word from a list following a player chosen number that represents a word from that list.'''
    a = ['formulation','guilty','hoofs','gun', 'finch', 'wonder', 'villain', 'amber','jazz','blooper', 'dizzy', 'germ', 'clod', 'rib', 'rambunctious','aggressive','askew','banjo','blitz', 'daiquiri','jazzy','zombie','difficult','jinx','rhythm','vat']
    wordvalue=int(raw_input("Pick a number between 0 and 25."))
    #print a[wordvalue]
    return a[wordvalue]



def check_guess (word, guess):
    """Look through word for letter.
    If it is wrong, return False
    If it is right, return True
    """
    if guess in word:     
        return True
    else:
        return False
       
    

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
    guess=raw_input("Guess a Letter!")
    return guess

def blankwords(word,guess):
    blank_word=word
    letters = set(word)
    goodguessed=guess
    for l in letters:
        if l not in goodguessed:
            blank_word = blank_word.replace(l,"_")
            blank_word = blank_word.replace(l.upper(),'_')
    print blank_word    
    return blank_word
        
        
def main ():
    response_list = ['Oops Looks like you got the wrong answer. Time to bring out the malfested!','Uh oh! That is not it! Do not worry traveler, it is only the guilty who need to worry now',]
    response_list_dark = ['Yes! Yes! Well, you got the answer wrong, but now we will be closer to ending the heretic!','*You begin to study the face of the prisoner. Looks as if he has not eaten in weeks. Dirt and some gashes of blood of the stoning are prevealent over his malnourished body.']
    response_list_darker = ['*The crowd begins to chant: The Greater Good.','The prisoner seems to have stopped struggling from before. As he passes each guard, stray rocks and glass are thrown at him.','*Out of the blood thirsty village, a small pocket of people look on with horror. A woman, maybe the his wife, covers the eyes of a newborn infant. The woman looks about 20.' ]
    response_list_yetdarker = ['The Greater Good.','The Greater Good.', 'The Greater Good.', 'The Greater Good.', 'The Greater Good.', 'The Greater Good.','The Greater Good.','He does not look like he is having a good time.']
    random.shuffle(response_list)
    random.shuffle(response_list_dark)
    random.shuffle(response_list_darker)
    random.shuffle(response_list_yetdarker)
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
            blankwords(word,guesses)
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
            elif lives==9:
                print response_list.pop()
            elif lives==6:
                print response_list_dark.pop()
            elif lives==5:
                print response_list_darker.pop()
            elif lives==4:
                print response_list_yetdarker.pop()
            elif lives==3:
                print response_list_yetdarker.pop()
            elif lives==2:
                print response_list_yetdarker.pop()
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
            
 
print "Welcome to hangman! Pick a number 1 through 25"
time.sleep(5)
print "..."
time.sleep(5)
print "Not yet. Sorry about that."
time.sleep(4)
print "I'll explain the rules first."
time.sleep(2)
print "When you're guessing, no capital letters are allowed, and there are no spaces. You cannot guess the whole word at once."
time.sleep(3)
print "One letter at a time please."
time.sleep(4)
print "Trust me."
time.sleep(3)
print "ok, now you can start. Have fun!"
main()
time.sleep(6)
print "Hey can you do me a favor?"
time.sleep(7)
print "Can you press that squiggly button and K at the same time? It would really help me out. I'll wait." 
time.sleep(8)
print "Thanks."
time.sleep(4)
print "Also, thank you for playing my game. This was written by Isaac Donkoh-Halm and Devin Cook."
time.sleep(5)
print "Good night!"
time.sleep(9)
print ";)"
