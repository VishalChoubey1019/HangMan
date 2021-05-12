#using another package known as random word which can be installed using ```pip install random-word```
#https://pypi.org/project/Random-Word/ check this out for more use of random word and upgrade it using verbs adjectives places options in future
from os import system, name
from random_word import RandomWords
import random
import time

#changed

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

correctletter=[]

#changed
play = input("To Start The Game Press Enter\n")
play = 'enter'
clear()
if play == 'enter':
  print ("Hello, Time To Play Hangman!\n")
  time.sleep(1.5)
  print ("NOTE: \n1] Make sure you don't use any capital letters.\n2] There are no repeating letters in the word.\n3] The First Letter Will Be Provided To You.\n4] If The Word Has More Than 8 Letters, Last Letter Will Also Be Given.\n")

  print("ENJOY!\n")

  time.sleep(5)
  
  clear()

#choosing random word
  guess = ''
  r= RandomWords()
  word=r.get_random_word(hasDictionaryDef="true")
#choosing random word

  turns = len(word)+3
  ans = ''
  print(f'Length of the word= {len(word)}\n')
  p=0
  done = []

  correct=1
#setting up variables
  for i in word:
    if(i!='-'):
      correctletter.append("-")
      done.append(i)
    else:
      correct=correct-1
#setting up variables


  print (f'The First Letter Of The Word Is: " {word[0]} "')

  correctletter[0]=word[0]
  time.sleep(0.5)

  if len(word)>=8:
    correct=correct+1
    print (f'\nThe Last Letter Of The Word Is: " {word[len(word)-1]} "\n')
    done[(len(done)-1)]="-"
    correctletter[len(word)-1]=word[len(word)-1]


  answer=""
  time.sleep(0.5)

  done[0]="-"
  

  while (turns>0) :
    if(len(word)==correct):
      break
    
    for i in correctletter:
      print(i,end =" ")
      
    print("\nTry left = ",turns)
    guess = input("\nGuess A Letter: ")
    
    if guess in word:
      if guess in done:
        print("Correct answer !")
        correct=correct+1
        correctletter[done.index(guess)]=guess
        done[(done.index(guess))]="-"
        time.sleep(0.75)
        clear()
        
        
      else: 
        time.sleep(0.5)
        clear()
        print("Letter Already Entered.")
        turns=turns-1

    else:
      time.sleep(0.25)
      clear()
      print("Wrong!\nTry again\n") 
      print(f'Number Of Tries Left {turns-1}')
      turns = turns-1    
      guess = ''
      time.sleep(1)
      clear()
    
     
  if turns==0 and (correct!=len(word)):
    print("\nYou Lost. ?? ?? ")
    print(f'The Word Was " {word} "')
  else:
    print(f'HURRAY! YOU FOUND THE WORD, IT WAS " {word} "\n\nYOU WON!! ?? ??\n') 
  answer=""
