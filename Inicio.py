# Inicio.py
from pgzero import music
from pygame import Rect
import Jogo  # <-- importa o módulo do jogo

WIDTH = 800
HEIGHT = 600

game_state = 'menu'
sound_on = True
music_started = False

# Botões
class Button:
    def __init__(self, x, y, text):
        self.pos = (x, y)
        self.text = text
        self.width = 384
        self.height = 128
        self.rect = Rect((x, y), (self.width, self.height))

    def draw(self):
        img = 'botao_hover' if self.rect.collidepoint(mouse_pos) else 'botao'
        screen.blit(img, self.pos)
        screen.draw.text(self.text, center=self.rect.center, fontsize=28, color="black")

start_btn = Button(208, 180, "Start Game")
sound_btn = Button(208, 320, "Sound: ON")
exit_btn = Button(208, 460, "Exit")

mouse_pos = (0, 0)

def draw():
    screen.clear()
    if game_state == 'menu':
        draw_menu()
    elif game_state == 'jogando':
        Jogo.draw(screen)  # delega ao jogo

def draw_menu():
    screen.fill((50, 50, 120))
    screen.draw.text("MAIN MENU", center=(WIDTH // 2, 100), fontsize=50, color="white")
    sound_btn.text = "Sound: ON" if sound_on else "Sound: OFF"
    start_btn.draw()
    sound_btn.draw()
    exit_btn.draw()

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def on_mouse_down(pos):
    global game_state, sound_on, music_started
    if game_state == 'menu':
        if start_btn.rect.collidepoint(pos):
            sounds.click.play()
            game_state = 'jogando'
            Jogo.reset()  # inicia o jogo

        elif sound_btn.rect.collidepoint(pos):
            sounds.click.play()
            sound_on = not sound_on
            if sound_on and not music_started:
                music.set_volume(1.5)
                music.play("musica")
                music_started = True
            elif not sound_on:
                music.stop()
                music_started = False

        elif exit_btn.rect.collidepoint(pos):
            sounds.click.play()
            quit()
    elif game_state == 'jogando':
        Jogo.on_mouse_down(pos)

def on_key_down(key):
    if game_state == 'jogando':
        Jogo.on_key_down(key)

def update():
    if game_state == 'jogando':
        Jogo.update()

def on_start():
    music.set_volume(1.5)
    if sound_on:
        music.play("musica")
