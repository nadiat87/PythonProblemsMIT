# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 13:57:09 2017

@author: Nai
"""

# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

#===PART-1=====================================================================
#==============================================================================
#===PART-1A====================================================================
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    found=False
    for char in secret_word:
        if char in letters_guessed:
            found = True
        else:
            found = False
    return found

##== TEST
#secret_word = 'apple'   
#letters_guessed = ['a', 'i', 'k', 'p', 'r', 's']
#letters_guessed = ['a', 'l', 'k', 'p', 'e', 's']
#print(is_word_guessed(secret_word, letters_guessed) )

#===PART-1B====================================================================
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    ans=''
    for char in secret_word:
        if char in letters_guessed:  
            ans+=str(char)+' '
        else:
            ans+= '_'+' '
    return ans

##== TEST
#secret_word = 'apple'   
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_guessed_word(secret_word, letters_guessed) )

#===PART-1C====================================================================
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet=string.ascii_lowercase
    ans=''
    for char in alphabet:
        if char not in letters_guessed:
            ans+=char
    return ans

##== TEST    
#print(string.ascii_lowercase)
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_available_letters(letters_guessed))
#==============================================================================

#===OTHER_FUNCTIONS===#

### Which warning message to display
def get_warning_message(n):
    if (n <0):
        ans='You have no warnings left so you lose one guess: '
    else:
        ans='You have '+str(n)+' warnings left: '
    return ans
        
### Count unique letters in secret_word
def count_unique_letters(word):
    i=0
    for i in range(len(word)):
        char_i = word[i]
        if (char_i not in word[:i]) and (char_i not in word[i+1:]):
            i+=1
    return i                      
        

#==============================================================================

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print(' Welcome to the game Hangman!')
    print(' I am thinking of a word that is ',str(len(secret_word)),' letters long.')
    print(' ------------')
    
    num_guesses = 6
    num_warnings = 3
    print(' You have ',str(num_warnings),' warnings left.')
    letters_guessed=''
    
    while num_guesses>0 and (is_word_guessed(secret_word, letters_guessed) == False):
        
        print(' You have ',str(num_guesses),' guesses left.')
        print(' Available letters: ',str(get_available_letters(letters_guessed)))
        char_found = False
        warning = False
        char_guess=[]
        char_guess=str.lower(input(' Please guess a letter: '))
        char_guess=char_guess.replace(' ','')
        char_guess=char_guess[0]

        if (str.isalpha(char_guess) == True):
            
            if (char_guess not in letters_guessed):
                
                letters_guessed+=char_guess
                for char in char_guess:
                    if char in secret_word:
                        char_found = True
                        print(' Good guess: ',get_guessed_word(secret_word, letters_guessed))
                    elif (char not in secret_word) and (char in 'aeiou'):
                        num_guesses-=2
                        print(' Oops! That letter is not in my word: ',get_guessed_word(secret_word, letters_guessed))
                    else:
                        num_guesses-=1
                        print(' Oops! That letter is not in my word: ',get_guessed_word(secret_word, letters_guessed))
            else:   
                num_warnings-=1
                warning = True
                print(' Oops! You have already guessed that letter.',get_warning_message(num_warnings),get_guessed_word(secret_word, letters_guessed))
                    
        else:
            num_warnings-=1
            warning = True
            print(' Oops! That is not a valid letter.',get_warning_message(num_warnings),get_guessed_word(secret_word, letters_guessed))

        if num_warnings <0:
               num_guesses-=1
               num_warnings = 3
                   
        print('-------------')  

        if '_' not in str(get_guessed_word(secret_word, letters_guessed)):
            break
           
        if num_guesses==0:
            print(' Sorry, you ran out of guesses. The word was:',str(secret_word))
            break
        
    if (is_word_guessed(secret_word, letters_guessed) == True):        
        total_score = num_guesses * count_unique_letters(secret_word)
        print(' Congratulations, you won! ')
        print(' Your total score for this game is:',str(total_score))
            
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

#secret_word='apple'

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word=my_word.replace(' ','')
    other_word=other_word.replace(' ','')
    match=False
    i=0
    if len(my_word)==len(other_word):
        while i<len(my_word):
            if (my_word[i:i+1] in other_word[i:i+1]):
                match=True
            elif (my_word[i:i+1] not in other_word[i:i+1]) and (my_word[i]=='_'):
                match=True
            else:
                return False
            i+=1
    return match

#my_word='a p _ _ e '
#other_word='apple'
#print(match_with_gaps(my_word,other_word))

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word=my_word.replace(' ','')
    result=[]
    j=0
    while j<len(wordlist):
        if (len(my_word)== len(wordlist[j])):
            if (match_with_gaps(my_word,wordlist[j])==True): 
                result.append(wordlist[j])
        j+=1
    if len(result)==0:
        result = ' No matches found '
    return result
#  
#my_word='a wwwww __ e '              
#print(show_possible_matches(my_word))             
                


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print(' Welcome to the game Hangman!')
    print(' I am thinking of a word that is ',str(len(secret_word)),' letters long.')
    print(' ------------')
    
    num_guesses = 6
    num_warnings = 3
    print(' You have ',str(num_warnings),' warnings left.')
    letters_guessed=''
    word_guessed=False
    
    while num_guesses>0 and (word_guessed == False):
        
        print(' You have ',str(num_guesses),' guesses left.')
        print(' Available letters: ',str(get_available_letters(letters_guessed)))
        char_found = False
        warning = False
        char_guess=''
        char_guess=str.lower(input(' Please guess a letter: '))
        char_guess=char_guess.replace(' ','')
        char_guess=char_guess[0]

        if (str.isalpha(char_guess) == True):     
            
            if (char_guess not in letters_guessed):                
                letters_guessed+=char_guess
                
                if char_guess in secret_word:
                    char_found = True
                    print(' Good guess: ',get_guessed_word(secret_word, letters_guessed))

                elif (char_guess not in secret_word) and (char_guess in 'aeiou'):
                    num_guesses-=2
                    print(' Oops! That letter is not in my word: ',get_guessed_word(secret_word, letters_guessed))
                else:
                    num_guesses-=1
                    print(' Oops! That letter is not in my word: ',get_guessed_word(secret_word, letters_guessed))
                    
            else:   
                num_warnings-=1
                warning = True
                print(' Oops! You have already guessed that letter.',get_warning_message(num_warnings),get_guessed_word(secret_word, letters_guessed))
        
        elif '*' in char_guess:
            print(str(show_possible_matches(get_guessed_word(secret_word, letters_guessed))))
            
        else:
            num_warnings-=1
            warning = True
            print(' Oops! That is not a valid letter.',get_warning_message(num_warnings),get_guessed_word(secret_word, letters_guessed))

        if num_warnings <0:
            num_guesses-=1
            num_warnings = 3

        if ('_' not in get_guessed_word(secret_word, letters_guessed)):
            word_guessed=True
        else:
            word_guessed=False
            
                   
        print('-------------')  

        
    if (word_guessed == True):        
        total_score = num_guesses * count_unique_letters(secret_word)
        print(' Congratulations, you won! ')
        print(' Your total score for this game is:',str(total_score))

    elif num_guesses==0:
        print(' Sorry, you ran out of guesses. The word was:',str(secret_word))

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    secret_word='apple'
    #secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)