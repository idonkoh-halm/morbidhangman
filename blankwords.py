def setestablish():
    a=['Mario','Link','Pikachu','Donkey Kong', 'Samus', 'Fox', 'Yoshi', 'Kirby','Luigi','Captain Falcon', 'Ness', 'Jigglypuff']
    wordvalue=int(raw_input("Pick a number between 0 and 11."))
    return a[wordvalue]

#a=['Mario','Link','Pikachu','Donkey Kong', 'Samus', 'Fox', 'Yoshi', 'Kirby','Luigi','Captain Falcon', 'Ness', 'Jigglypuff']
#print a
print setestablish()

#i = "Mario"
#if "e" in i:
#    print "There is no e."
b="mario"
blank_word=b
letters = set(b)
for l in letters:
    blank_word.replace(l,"_")
    blank_word.replace(l.upper(),'_')
    print 
