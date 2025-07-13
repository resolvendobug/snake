# Snake Roguelike - Projeto em Python com pgzero

Este é um jogo estilo Snake com elementos de roguelike, desenvolvido em Python utilizando a biblioteca [pgzero](https://pygame-zero.readthedocs.io/). O jogo possui inimigos móveis, menu inicial com botões funcionais, animação simples do personagem principal e música de fundo.

---

## Características principais

- **Menu inicial** com botões: Start Game, Sound ON/OFF, Exit
- **Música de fundo** e efeitos sonoros nos cliques
- **Jogabilidade estilo Snake** com corpo e cabeça animada
- **Inimigos móveis** que se deslocam dentro de áreas definidas
- Uso das bibliotecas restritas: `pgzero`, `random`, `pygame.Rect`
- Código organizado, seguindo padrões PEP8

---

## Requisitos

- Python 3.7+
- [pgzero](https://pypi.org/project/pgzero/)
- (Opcional) Editor de código como VSCode para facilitar o desenvolvimento

---

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale o pgzero:
   ```bash
   pip install pgzero
   ```

3. Certifique-se de que as imagens estão na pasta correta (`images/`), incluindo:
   - `head-1.png` e `head-2.png` (sprites da cabeça da cobra)
   - `body.png` (sprite do corpo da cobra)
   - `apple.png` (imagem da maçã)
   - `hippo.png` (imagem dos inimigos)
   - `botao.png` e `botao_hover.png` (sprites dos botões do menu)

4. Certifique-se de que os sons estão na pasta `sounds/`, incluindo:
   - `musica.mp3` (música de fundo)
   - `click.wav` (som do clique nos botões)

---

## Como jogar

1. Execute o jogo com o pgzero:
   ```bash
   pgzrun Inicio.py
   ```

2. No menu inicial:
   - Clique em **Start Game** para iniciar.
   - Clique em **Sound: ON/OFF** para ligar ou desligar a música.
   - Clique em **Exit** para fechar o jogo.

3. Controle a cobra usando as setas do teclado:
   - ↑, ↓, ←, → para mudar a direção.

4. Evite colidir com as bordas, com seu próprio corpo ou com os inimigos.

5. Coma as maçãs para crescer e continuar jogando.

6. Se perder, clique em **Play Again** para reiniciar.

---

## Estrutura do projeto

- `Inicio.py`: módulo principal com menu, controle de estados e música.
- `Jogo.py`: lógica do jogo, incluindo o controle da cobra, inimigos e interface gráfica.
- `images/`: imagens usadas no jogo (sprites da cobra, inimigos, maçã, botões).
- `sounds/`: arquivos de áudio para música e efeitos.

---

## Licença

Projeto aberto para uso educacional e pessoal. Sinta-se à vontade para contribuir e modificar conforme sua necessidade.

---

## Contato

Para dúvidas, sugestões ou contribuições, abra uma issue no repositório ou envie mensagem