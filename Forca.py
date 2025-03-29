import random


#Lista de palavras Animais, estados, objetos

wordListAnimais =["vaca","camelo","jabuti","ornitorrinco", "elefante","tartaruga","hipopotamo","rinoceronte","formiga",
    "arara","capivara","tucano","lagarto","cachorro","papagaio","jacare","borboleta","girafa","pinguim","morcego","tigre","zebra",
    "macaco","golfinho","baleia","sapo","rã","peixe","piranha",
    "baiacu","aguia","falcão","gaivota","pelicano"]

wordListEstados =["acre","alagoas","amapa","amazonas","bahia","ceara","goias","maranhao","paraiba","parana","pernambuco","piaui",
"rondonia","roraima","sergipe","tocantins"]

wordListCountry = ["argentina", "australia", "brazil", "canada", "chile",
    "china", "colombia", "cuba", "egypt", "france",
    "germany", "greece", "india", "israel", "italy",
    "japan", "mexico", "norway", "poland", "russia"]

categoria = "Animais"


difficulty = int(input(f"Escolha o nível de dificuldade:\n1 - Animais (fácil)\n2 - Estados Brasileiros (intermediário)\n3 - Países em inglês (difícil): "))

if(difficulty==1):
    print("Opção fácil escolhida")
    activeWord = random.choice(wordListAnimais)
    categoria = "Animais"
elif(difficulty==2):
    print("Opção intermediária escolhida")
    activeWord = random.choice(wordListEstados)
    categoria = "Estados brasileiros"
elif(difficulty==3):
    print("Opção difícil escolhida")
    activeWord = random.choice(wordListCountry)
    categoria = "Países"
else:
    print("Opção inválida, categoria fácil escolhida")
    activeWord = random.choice(wordListAnimais)
    categoria = "Animais"



#Quantidade de letra da palavra escolhida
letterQtd = len(activeWord)
acertos=0
vidas=5


#print(f"Debug, a palavra é: {activeWord}")
print(f"Bem vindo ao jogo da forca!!! \n"
      f"Dica: {categoria}\n")

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

tecla=input(f"\n\nPressione enter para fechar: ")
