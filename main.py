"""Vincula emotes ou a maestria do LoL às teclas de habilidade.

Depois de configurado, cada vez que a habilidade é usada o script
também envia o comando de emote (T) ou de maestria (Ctrl+6).
"""
import time

import keyboard
import pydirectinput

# Hotkeys
ATTRIBUTE = "ctrl+."  # inicia uma atribuição
UNBIND = "ctrl+;"  # remove uma atribuição
BREAK = "ctrl+enter"  # encerra o script

# Constants
# Habilidade -> ação vinculada ('e' = emote, 'm' = maestria, '' = nada)
ATTRIBUTIONS = {
    'q': '',
    'w': '',
    'e': '',
    'r': '',
    'space': ''
}
OPTIONS = ['e', 'm']
TIMER = 10  # segundos para escolher a habilidade/ação após o atalho


# Loop principal
def main():
    while True:
        if keyboard.is_pressed(ATTRIBUTE):
            atribuir()
        if keyboard.is_pressed(UNBIND):
            desvincular()
        if keyboard.is_pressed(BREAK):
            break

        # Dispara a ação vinculada quando a habilidade é pressionada
        for key, value in ATTRIBUTIONS.items():
            if keyboard.is_pressed(key):
                if value == 'e':
                    pydirectinput.press('t')
                elif value == 'm':
                    pydirectinput.keyDown('ctrl')
                    pydirectinput.press('6')
                    pydirectinput.keyUp('ctrl')


# Atribuição
def atribuir():
    print("#" * 5, "Atribuição", "#" * 5)
    c = recebe_comando()
    print(f"Comando: {c}")
    time.sleep(0.5)  # evita ler o mesmo atalho duas vezes

    r = None
    if c:
        print("Comando recebido!")
        r = recebe_resposta()
        print(f"Resposta: {r}")
    if r:
        ATTRIBUTIONS[c] = r
        print(f"Atualizações:\n{ATTRIBUTIONS}")
    print("Saindo de atribuir()")


def recebe_algo(options):
    """Espera até TIMER segundos por Ctrl + uma das teclas em `options`."""
    ini = time.time()
    while time.time() - ini < TIMER:
        for key in options:
            if keyboard.is_pressed("ctrl+" + key):
                return key


def recebe_comando():
    return recebe_algo(ATTRIBUTIONS)


def recebe_resposta():
    return recebe_algo(OPTIONS)


# Desvínculo
def desvincular():
    print("#" * 5, "Desvínculo", "#" * 5)
    c = recebe_comando()
    print(f"Comando: {c}")
    if c is not None:
        # Ctrl+Espaço limpa todas as habilidades de uma vez
        if c == 'space':
            for key in ATTRIBUTIONS:
                ATTRIBUTIONS[key] = ''
        else:
            ATTRIBUTIONS[c] = ''
        print(f"Atualizações:\n{ATTRIBUTIONS}")
    print("Saindo de desvincular()")


if __name__ == "__main__":
    main()
