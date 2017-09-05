################################################
# Title - Pendu
# Date - 04/09/17
################################################

import os

############Function############################

def hidden_word(word, proposal):
	w = ''
	for lettre in word:
		if lettre in proposal:
			w = w + lettre
		else:
			w = w + '-'
	return w

############Body################################

num_error = 0
max_error = 10
lowercase = "abcdefghijklmnopqrstuvwxyz"
proposal = []

print"Bienvenue sur ce pendu a deux joueurs"
print"Un joueur doit selectionner a sa discretion un mot, le second doit le deviner"
print"Vous avez 10 essais"

word = raw_input("Veuillez entrer le mot a deviner: ")
word = str.lower(word)
os.system('clear')

while num_error != 10 and hidden_word(word,proposal) != word:
	lettre = raw_input("Veuillez renseigner une lettre :")
	if lettre not in lowercase or len(lettre) != 1:
		print"Veuillez renseigner une seule lettre minuscule:"
	elif lettre in proposal:
		num_error = num_error + 1
		max_error = max_error - 1
		print"lettre deja proposee. Try again. Il vous reste %d essais" % max_error
		print"Reponse courante :", hidden_word(word,proposal)
	elif lettre in word:
		print"La lettre est dans le mot."
		proposal.append(lettre)
		print"Reponse courante :", hidden_word(word,proposal)
	elif lettre not in word:
		proposal.append(lettre)
		num_error = num_error + 1
		max_error = max_error - 1
		print"Erreur. Il vous reste %d essais" % max_error
		print"Reponse courante :", hidden_word(word,proposal)

if hidden_word(word,proposal) == word:
		print"Vous avez gagne ! Le mot etait ", word
else:
	print"Vous avez perdu. Le mot etait", word


