# HANGMAN GAME
# BY VARAD KSHIRSAGAR

import random

#------------------------------------------variables------------------------------------------#

word_list = ['watermelon','moisturiser','medicines','football']
guess_word = word_list[random.randint(0,len(word_list)-1)]
append_list = []
wrong_attempts = 0

#------------------------------------------variables------------------------------------------#

#------------------------------------------functions------------------------------------------#

def disp_init():
	for i in guess_word:
		if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
			append_list.append(i)
		else:
			append_list.append('_')
	print(' '.join(append_list))

def disp_char(c):
	flag = 0
	for i in range(0,len(guess_word)):
		if guess_word[i] == c:
			flag = 1
			append_list[i] = c

	if flag == 0:
		global wrong_attempts 
		wrong_attempts += 1
	print(' '.join(append_list))

def check_done():
	flag = 0
	for i in append_list:
		if i == '_':
			flag = 1

	if flag == 1:
		return 0
	else:
		return 1

#------------------------------------------functions------------------------------------------#

#------------------------------------------game loop------------------------------------------#

print('Welcome to hangman!You have 3 attemps.\nYour word is:')
disp_init()

flag = 0
while wrong_attempts < 3 :
	guessed_char = input('Guess:')
	disp_char(guessed_char)
	if check_done() == 1:
		flag = 1
		print('You win yay!')
		break;

if flag == 0:
	print('You lost :(')

#------------------------------------------game loop------------------------------------------#
