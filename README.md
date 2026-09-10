# 🐍 Snake Game em Pygame

Um clássico jogo da cobrinha (Snake) desenvolvido em Python utilizando a biblioteca **Pygame**, apresentando um tabuleiro quadriculado, sistema de pontuação e aumento progressivo do corpo da cobra a cada maçã consumida.

---

## 🚀 Funcionalidades

* **Tabuleiro Estilizado:** Fundo quadriculado alternando entre dois tons de verde.
* **Crescimento da Cobra:** A cobra aumenta de tamanho e o placar é atualizado cada vez que uma maçã é comida.
* **Detecção de Colisões:** O jogo termina se a cobra atingir as bordas da tela ou colidir com o próprio corpo.
* **Placar em Tempo Real:** Contador visível no canto superior esquerdo mostrando o número de maçãs coletadas.

---

## 🛠️ Pré-requisitos e Instalação

Antes de executar o jogo, certifique-se de ter o Python e a biblioteca Pygame instalados em sua máquina.

1. **Clone o repositório ou baixe os arquivos:**
```bash
git clone https://github.com/vesky69/Snake-Game.git
cd snake-pygame

```


2. **Instale o Pygame:**
```bash
pip install pygame

```



---

## 🕹️ Como Jogar

Execute o script principal do jogo através do terminal:

```bash
python snake.py

```

### 🎮 Controles

Utilize as **setas direcionais** do teclado para controlar a movimentação da cobra:

* **Seta para Cima ($\uparrow$):** Move para cima
* **Seta para Baixo ($\downarrow$):** Move para baixo
* **Seta para Esquerda ($\leftarrow$):** Move para esquerda
* **Seta para Direita ($\rightarrow$):** Move para direita

---

## ⚙️ Configurações do Jogo (Personalização)

Você pode alterar facilmente alguns parâmetros no início do código-fonte para ajustar a dificuldade ou o visual:

* `width` e `height`: Dimensões da janela do jogo (padrão: `600x400`).
* `speed`: Velocidade de atualização dos quadros / velocidade da cobra (padrão: `8`).
* `snake_size`: Tamanho em pixels de cada bloco da cobra e da maçã (padrão: `10`).

---

## 📜 Licença

Este projeto é de código aberto e está disponível sob a licença [MIT](https://www.google.com/search?q=LICENSE).
