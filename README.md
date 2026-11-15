# bind-m7

> 🇧🇷 [Português](#português) · 🇺🇸 [English](#english)

## Português

### O que você encontrará neste repositório?

Uma maneira de irritar seus oponentes no League of Legends atribuindo emotes ou maestrias às suas habilidades! A
configuração pode ser feita durante o jogo e a atribuição é múltipla (ou seja, você pode associar uma ação a uma ou mais
habilidades).

Criado em **maio de 2021** e reescrito em **novembro de 2022**, com a configuração durante a partida.

> ⚠️ Projeto de brincadeira. Scripts que enviam comandos ao jogo podem violar os termos de uso da Riot Games: use por
> sua conta e risco.

### Ferramentas

* Python 3
* [keyboard](https://github.com/boppreh/keyboard) (leitura dos atalhos)
* [pydirectinput](https://github.com/learncodebygaming/pydirectinput) (envio de teclas para o jogo)

### Como usar

Funciona no **Windows**, onde o `pydirectinput` consegue enviar teclas ao jogo.

**1. Clone e instale as dependências**

```bash
git clone https://github.com/tofolo17/bind-m7.git
cd bind-m7
pip install -r requirements.txt
```

**2. Execute** com `python main.py` ou com dois cliques no `main.bat`. Deixe o terminal aberto e entre no jogo.

**3. Configure durante a partida** (cada etapa espera até 10 segundos):

| Ação                  | Atalhos                                                                       |
|-----------------------|-------------------------------------------------------------------------------|
| Vincular              | `Ctrl+.` → `Ctrl+` habilidade (`Q`, `W`, `E`, `R`) → `Ctrl+E` (emote) ou `Ctrl+M` (maestria) |
| Desvincular           | `Ctrl+;` → `Ctrl+` habilidade                                                 |
| Desvincular todas     | `Ctrl+;` → `Ctrl+Espaço`                                                      |
| Encerrar              | `Ctrl+Enter`                                                                  |

Exemplo: `Ctrl+.`, depois `Ctrl+R`, depois `Ctrl+M` faz a maestria aparecer toda vez que você usar o ultimate. Para
vincular a tecla Espaço, use `Ctrl+.` → `Ctrl+Espaço` → ação.

O emote é enviado com a tecla `T` e a maestria com `Ctrl+6`, os atalhos padrão do jogo.

### Licença

[MIT](LICENSE)

---

## English

### What will you find in this repository?

A way to assign emotes or mastery to your skills and annoy your League of Legends opponents! You can do the setting
during the game and reach multiple assignments (you can associate an action with one or more skills).

Created in **May 2021** and rewritten in **November 2022**, adding in-game configuration.

> ⚠️ Just-for-fun project. Scripts that send inputs to the game may violate Riot Games' terms of service: use at your
> own risk.

### Tools

* Python 3
* [keyboard](https://github.com/boppreh/keyboard) (reading hotkeys)
* [pydirectinput](https://github.com/learncodebygaming/pydirectinput) (sending keys to the game)

### How to use

Works on **Windows**, where `pydirectinput` can send keys to the game.

**1. Clone and install the dependencies**

```bash
git clone https://github.com/tofolo17/bind-m7.git
cd bind-m7
pip install -r requirements.txt
```

**2. Run** `python main.py` or double-click `main.bat`. Keep the terminal open and join a game.

**3. Configure in-game** (each step waits up to 10 seconds):

| Action                | Hotkeys                                                                       |
|-----------------------|-------------------------------------------------------------------------------|
| Bind                  | `Ctrl+.` → `Ctrl+` skill (`Q`, `W`, `E`, `R`) → `Ctrl+E` (emote) or `Ctrl+M` (mastery) |
| Unbind                | `Ctrl+;` → `Ctrl+` skill                                                      |
| Unbind all            | `Ctrl+;` → `Ctrl+Space`                                                       |
| Quit                  | `Ctrl+Enter`                                                                  |

Example: `Ctrl+.`, then `Ctrl+R`, then `Ctrl+M` shows your mastery every time you use your ultimate. To bind the Space
key, use `Ctrl+.` → `Ctrl+Space` → action.

The emote is sent with the `T` key and mastery with `Ctrl+6`, the game's default shortcuts.

### License

[MIT](LICENSE)
