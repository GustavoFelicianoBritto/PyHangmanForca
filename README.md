# 🐍 Jogo da Forca em Python  

🔍 **Descrição**  
Um simples jogo da forca em Python onde o jogador tenta adivinhar uma **palavra secreta** antes de perder todas as vidas.  

<!--⚠️ **Bug CORRIGIDO**: 
- ✅ Quando o jogador repetia a mesma letra correta várias vezes, o contador de acertos aumenta indevidamente, permitindo vencer sem completar a palavra. -->

✨**NOVIDADES**:
- Agora você possui informação na tela com suas letras já enviadas (Evitando repetir letra)
- ✅ Bug Corrigido: Quando o jogador repetia a mesma letra correta várias vezes, o contador de acertos aumenta indevidamente, permitindo vencer sem completar a palavra (agora temos um acumulador de letras enviadas)
- Agora o usuário pode escolher entre 4 dificuldades **cada dificuldade possui um tema diferente**
- Função pressionar adicionada (Agora em algumas escolhas você não precisa digitar enter, apenas pressionar a tecla)
  
---

### 🎮 **Como Jogar**  
1. O programa escolhe aleatoriamente uma palavra da lista da categoria selecionada.  
2. Você tem **5 vidas** para adivinhar as letras corretas.  
3. A cada erro, perde uma vida.  
4. Se completar a palavra antes de perder todas as vidas, vence!  

---

🛠️ **Tecnologias e Conceitos Utilizados**

📚 Bibliotecas Python
- random: Seleção aleatória de palavras das categorias
- msvcrt: Captura de teclas em sistemas Windows
- tty e termios: **Manipulação de terminal** em Linux/Mac
- sys: Controle de entrada/saída do sistema

Controle de game state:

- Sistema de vidas (5 tentativas)
- Verificação de letras repetidas
- Exibição progressiva da palavra oculta (_ _ _ _ → P _ _ _)

⚙️ Estruturas e Técnicas
- Manipulação avançada de strings e listas:
- Substituição dinâmica de underlines (_)
- Controle de letras já tentadas
- Estruturas de controle:
- while para loop principal do jogo
- for com **enumerate()** para verificação de letras
- **if/elif/else** para gestão de dificuldades
- **try/except/finally** para compatibilidade entre sistemas


💻 **Funcionalidades Principais**
- Sistema multiplataforma de captura de teclas sem necessidade de Enter
- 4 níveis de **dificuldade** com categorias distintas:

🐾 Animais (fácil)
🏙️ Estados brasileiros (intermediário)
🌎 Países em inglês (difícil)
💀 Todas categorias (extremo)


---

📌 **Observação**: 
- Projeto criado para prática de Python, com foco em lógica básica e manipulação de dados.  
