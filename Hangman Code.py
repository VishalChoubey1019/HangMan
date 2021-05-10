import random
import time
play = input("To Start The Game Press Enter\n")
play = 'enter'
if play == 'enter':
  print ("Hello, Time To Play Hangman!\n")
  time.sleep(1.5)
  print ("NOTE: \n1] Make sure you don't use any capital letters.\n2] There are no repeating letters in the word.\n3] The First Letter Will Be Provided To You.\n4] If The Word Has More Than 8 Letters, Last Letter Will Also Be Given.\n")
  time.sleep(5)
  print("ENJOY!\n")
  list = ['army', 'beautiful', 'hacked', 'love', 'dance', 'monkey' , 'bot', 'gun','polish','duration','zodiac','worthy','grape','me','you','husky','dog','cat','lion','tiger','beard','brush','sword','brown','grey','red','black','oxygen','water','heat','pray','gold','golf','erase','clear','clean','head','shoulder','black','blank','burst','goal','glow']

  guess = ''

  word = random.choice(list)
  turns = len(word)+3
  ans = ''
  print(f'Length of the word= {len(word)}\n')
  time.sleep(2)
  p=0
  done = [""]

  print (f'The First Letter Of The Word Is: " {word[0]} "')
  time.sleep(2)
  if len(word)>=8:
    print (f'\nThe Last Letter Of The Word Is: " {word[len(word)-2]} "\n')
    time.sleep(2)
  while turns>0 :
    #print("Guess a letter: ")
    guess = input("Guess A Letter: ")
    
    if guess in word:
      if guess in done:
        print("Letter Already Entered.")
      else:  
        count=1
        p=p+1
        
        print (f'correct\n')
        if p==len(word):
          break
        for i in word:
          
          if i==guess:
            print(f'character no. {count} unlocked.\n')    
            done.insert(count-1,guess)
            
            break
          else:
            count=count+1
    else:
      print("Wrong!\nTry again\n") 
      print(f'Number Of Tries Left {turns-1}')
      turns = turns-1    
      guess = ''
    
     
  if turns==0:
    print("\nYou Lost. ?? ?? ")
    print(f'The Word Was " {word} "')
  else:
    print(f'HURRAY! YOU FOUND THE WORD, IT WAS " {word} "\n\nYOU WON!! ?? ??\n')  
