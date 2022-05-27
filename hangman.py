import random

from words import words
import string

def get_valid_word(words):
      word = random.choice(words) #randomly chooses something from the list
      while '-' in word or ' ' in word: #as long as there is a dash or space in the word, keep choosing the word
            word = random.choice(words)
      return word.upper() #finally getting a word that does nt have a dash or space in it. .upper means uppercase

def hangman():
      word = get_valid_word(words)
      word_letters = set(word) #letters in the words already guessed
      alphabet = set(string.ascii_uppercase) #uppercase characters in English
      used_letters = set() #what the user has guessed

      #getting user input
      while len(word_letters) > 0: #if the length of letter is greater than zero keep ilietarating
            #letters used to help user keep track
            # ''.join(['a', 'b', 'cd']) --> 'a b cd' (changes the list into a string)
            print('you have used these letters: ', ' '.join(used_letters))

            #what current word is (ie W- R D) the letters they have guessed and where they appear in the word and the dash represeting the missing letter and where it goes
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print('current word: ', ' '.join(word_list))
          
            user_letter = input('Guess a letter: ').upper()
            if user_letter in alphabet - used_letters: #valid character in the alphabet that i havent used yet
                  used_letters.add(user_letter) #add valid letter to the user_letter set
                  if user_letter in word_letters: #character already in word
                  word_letters.remove(user_letter) #every time guess is correct each word decreases in size
                  print('')

            elif user_letter in used_letters:
                  print('you literally already guessed that letter')

            else:
                  print('invalid character')  #gets here when len(word_letter) == 0

      hangman()

