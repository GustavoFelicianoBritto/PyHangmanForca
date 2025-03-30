import random

#criando função de receber tecla (windows e linux)
def input_key():
    try:
        #tentando importar windows > atribuindo em tecla o valor da tecla clicada > talvez converter para utf-8
        import msvcrt
        tecla=msvcrt.getch()
        return tecla.decode('utf-8')if isinstance(tecla, bytes) else tecla
        # retornando a tecla pressionada
    except(ImportError):
        #se tiver erro de importação, tentar o do linux
        try:
            import tty, termios, sys
            #importando sistemas e terminal
            CanalEntrada = sys.stdin.fileno()
            #obtendo canal de entrada
            old_settings = termios.tcgetattr(CanalEntrada)
            #salvando configurações no old_settings como backup
            tty.setraw(CanalEntrada)
            #ativando o modo raw do canal de entrada (sem enter)
            return sys.stdin.read(1)
            #retornando a tecla pressionada
        except():
            print("Seu terminal não suporta leitura direta")

        finally:
            termios.tcsetattr(CanalEntrada, termios.TCSADRAIN, old_settings)
            #restaurando terminal linux
            #continuar estudando sobre

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

wordListGeneral=["vaca","camelo","jabuti","ornitorrinco", "elefante","tartaruga","hipopotamo","rinoceronte","formiga",
    "arara","capivara","tucano","lagarto","cachorro","papagaio","jacare","borboleta","girafa","pinguim","morcego","tigre","zebra",
    "macaco","golfinho","baleia","sapo","rã","peixe","piranha",
    "baiacu","aguia","falcão","gaivota","pelicano","acre","alagoas","amapa","amazonas","bahia","ceara","goias","maranhao","paraiba","parana","pernambuco","piaui",
"rondonia","roraima","sergipe","tocantins","argentina", "australia", "brazil", "canada", "chile",
    "china", "colombia", "cuba", "egypt", "france",
    "germany", "greece", "india", "israel", "italy",
    "japan", "mexico", "norway", "poland", "russia"]


#Valor default para categoria
categoria = "Animais"


print(f"Escolha o nível de dificuldade:\n1 - Animais (fácil)\n2 - Estados Brasileiros (intermediário)\n3 - Países em inglês (difícil)\n"
      f"4 - Todas categorias (EXTREMO): ")
difficulty=input_key()

print("==========================\n")

if(difficulty=='1'):
    print("Opção fácil escolhida")
    activeWord = random.choice(wordListAnimais)
    categoria = "Animais"
elif(difficulty=='2'):
    print("Opção intermediária escolhida")
    activeWord = random.choice(wordListEstados)
    categoria = "Estados brasileiros"
elif(difficulty=='3'):
    print("Opção difícil escolhida")
    activeWord = random.choice(wordListCountry)
    categoria = "Países"
elif(difficulty == '4'):
    print("Opção EXTREMA escolhida")
    activeWord = random.choice(wordListGeneral)
    categoria = "Geral"
else:
    print("Opção inválida, categoria fácil escolhida")
    activeWord = random.choice(wordListAnimais)
    categoria = "Animais"



#Quantidade de letra da palavra escolhida
letterQtd = len(activeWord)
acertos=0
vidas=5
letterSend =[]


#print(f"Debug, a palavra é: {activeWord}")
print(f"\nBem vindo ao jogo da forca!!! \n"
      f"Dica: {categoria}\n")

wordGuess = ['_']*letterQtd

while acertos < letterQtd and vidas>0:

    notValid = 0

    print(f"Letras enviadas: {letterSend}")
    letter = str(input(f"{wordGuess}\n\nDigite uma letra: ").lower())

    if letter not in letterSend:
        #se a letra enviada não estiver no vetor das letras enviadas, irei colocar ela dentro e
        #darei sequencia no código

        letterSend.insert(0,letter)

        print("==========================\n")

        for indexLetter, currentLetter in enumerate(activeWord):
            if letter == currentLetter:
                print(f"Letra '{letter}' encontrada na posição {indexLetter +1}")
                #colocando a letra encontrada na posição do _ do vetor da forca
                wordGuess[indexLetter] = letter
                acertos+=1

            else:
                notValid+=1
                #a cada giro no for, adiciono +1 pra cada slot que a letra não estiver (continua abaixo)


        if notValid == letterQtd:
            vidas-=1
            print("[Opção incorreta]")
            #se o valor de notValid for igual a quantidade de letra da palavra, vou saber que n tem a letra na palavra

    else:
        #se a letra já estiver nas letras enviadas, não farei nada e indicarei que a letra ja´foi enviada
        print(f"--------------------\nLetra já enviada\n--------------------")


    print(f"Vidas restantes: {vidas}")

#final do while (acertou todas letras ou perdeu todas vidas)

if vidas <= 0:
    print(f"Você perdeu! a palavra era: {activeWord}")
else:
     print(f"Parabéns, você acertou a palavra: {activeWord} com {vidas} vidas")


print(wordGuess)
#print(ActiveWord)

print(f"\n\nPressione qualquer tecla para fechar: ")
closeKey = input_key()
