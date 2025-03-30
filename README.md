# 🐍 Jogo da Forca em Python  

🔍 **Descrição**  
Um simples jogo da forca em Python onde o jogador tenta adivinhar uma palavra secreta (dica: sempre um animal!) antes de perder todas as vidas.  

<!--⚠️ **Bug CORRIGIDO**: 
- ✅ Quando o jogador repetia a mesma letra correta várias vezes, o contador de acertos aumenta indevidamente, permitindo vencer sem completar a palavra. -->

✨**NOVIDADES**:
- Agora você possui informação na tela com suas letras já enviadas (Evitando repetir letra)
- ✅ Bug Corrigido: Quando o jogador repetia a mesma letra correta várias vezes, o contador de acertos aumenta indevidamente, permitindo vencer sem completar a palavra (agora temos um acumulador de letras enviadas)
- Agora o usuário pode escolher entre 3 dificuldades **cada dificuldade possui um tema diferente**
---

### 🎮 **Como Jogar**  
1. O programa escolhe aleatoriamente uma palavra da lista de animais.  
2. Você tem **5 vidas** para adivinhar as letras corretas.  
3. A cada erro, perde uma vida.  
4. Se completar a palavra antes de perder todas as vidas, vence!  

---

### ⚙️ **Funcionalidades**  
✔️ Palavras aleatórias de diferentes dificuldades (de "vaca" a "ornitorrinco").  
✔️ Exibição da posição das letras corretas.  
✔️ Contador de vidas restantes.  
✔️ Mensagem de vitória/derrota ao final.  

---

### 🛠️ **Tecnologias e Conceitos Utilizados**  
- **Biblioteca `random`**: Para seleção aleatória da palavra.  
- **Manipulação de strings e listas**: Substituição de underlines (`_`) pelas letras corretas.  
- **Estruturas de repetição (`while`, `for`)**: Controle do fluxo do jogo.  
- **Input do usuário**: Interação via terminal.  

---

📌 **Observação**: Projeto criado para prática de Python, com foco em lógica básica e manipulação de dados.  
