import random

wordList=["vaca","camelo","jabuti","ornitorrinco","paralelepipedo"]

activeWord = random.choice(wordList)
letterQtd = len(activeWord)
acertos=0

print(f"Debug, a palavra é: {activeWord}")
wordGuess = ['_']*letterQtd

while acertos != letterQtd:

    letter = str(input(f"{wordGuess}\nDigite uma letra: ").lower())

    for indexLetter, currentLetter in enumerate(activeWord):
        if letter == currentLetter:
            print(f"Letra '{letter}' encontrada na posição {indexLetter}")
            wordGuess[indexLetter] = letter
            acertos+=1
        








print(wordGuess)
#print(ActiveWord)
