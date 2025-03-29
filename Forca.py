import random

wordList=["vaca","camelo","jabuti","ornitorrinco","paralelepipedo","elefante","tartaruga","hipopotamo","rinoceronte","formiga",
    "arara","capivara","tucano","lagarto","cachorro","papagaio","jacare","borboleta","girafa","pinguim","morcego","tigre","zebra",
    "macaco","golfinho","baleia","sapo","rã","peixe","piranha",
    "baiacu","aguia","falcão","gaivota","pelicano"]

activeWord = random.choice(wordList)
letterQtd = len(activeWord)
acertos=0
vidas=5


#print(f"Debug, a palavra é: {activeWord}")
print(f"Bem vindo ao jogo da forca!!! \n"
      f"Dica: Animal\n")

wordGuess = ['_']*letterQtd

while acertos < letterQtd and vidas>0:

    notValid = 0

    letter = str(input(f"{wordGuess}\nDigite uma letra: ").lower())

    for indexLetter, currentLetter in enumerate(activeWord):
        if letter == currentLetter:
            print(f"Letra '{letter}' encontrada na posição {indexLetter +1}")
            wordGuess[indexLetter] = letter
            acertos+=1

        else:
            notValid+=1

    if notValid == letterQtd:
        vidas-=1
        print("Opção incorreta")


    print(f"Vidas restantes: {vidas}")

if vidas <= 0:
    print(f"Você perdeu! a palavra era: {activeWord}")
else:
     print(f"Parabéns, você acertou a palavra: {activeWord} com {vidas} vidas")


print(wordGuess)
#print(ActiveWord)

print("Aperte qualquer tecla para fechar")
