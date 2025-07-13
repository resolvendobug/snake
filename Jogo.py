import random
from pygame import Rect

cell_size = 20
cols = 40
rows = 30

snake = []
direction = (1, 0)
apple = (10, 10)
game_over = False
frame_count = 0
speed = 10
head_frame = 0

play_again_btn = Rect(300, 350, 200, 60)

class Enemy:
    def __init__(self, x, y, move_range, direction='random'):
        self.start_pos = (x, y)
        self.pos = [x, y]
        self.move_range = move_range
        self.axis = direction
        self.step = 1

    def move(self):
        axis_choice = random.choice(['horizontal', 'vertical']) if self.axis == 'random' else self.axis
        if axis_choice == 'horizontal':
            delta = random.choice([-1, 0, 1])
            new_x = self.pos[0] + delta
            if abs(new_x - self.start_pos[0]) <= self.move_range:
                self.pos[0] = new_x
        elif axis_choice == 'vertical':
            delta = random.choice([-1, 0, 1])
            new_y = self.pos[1] + delta
            if abs(new_y - self.start_pos[1]) <= self.move_range:
                self.pos[1] = new_y

    def draw(self, screen):
        # Desenha a imagem hippo.png na posição do inimigo
        screen.blit("hippo", (self.pos[0] * cell_size, self.pos[1] * cell_size))

    def get_position(self):
        return tuple(self.pos)

enemies = [
    Enemy(10, 15, 10),
    Enemy(25, 5, 6),
    Enemy(30, 20, 8),
    Enemy(37, 0, 8),
    Enemy(60, 25, 8),
]

def reset():
    global snake, direction, apple, game_over, frame_count, head_frame
    snake.clear()
    snake.append((5, 5))
    direction = (1, 0)
    apple = generate_apple()
    game_over = False
    frame_count = 0
    head_frame = 0
    for enemy in enemies:
        enemy.pos = list(enemy.start_pos)
        enemy.step = 1

def draw(screen):
    global head_frame
    if game_over:
        screen.fill((150, 0, 0))
        screen.draw.text("Game Over!", center=(400, 250), fontsize=60, color="white")
        screen.draw.filled_rect(play_again_btn, (255, 255, 0))
        screen.draw.text("Play Again", center=play_again_btn.center, fontsize=30, color="black")
        return

    screen.fill((0, 0, 0))

    # animação da cabeça
    head_image = f"head-{head_frame % 2 + 1}"
    hx, hy = snake[0]
    screen.blit(head_image, (hx * cell_size, hy * cell_size))

    # corpo
    for segment in snake[1:]:
        x, y = segment
        screen.blit("body", (x * cell_size, y * cell_size))

    # maçã - usando imagem apple.png
    ax, ay = apple
    screen.blit("apple", (ax * cell_size, ay * cell_size))

    for enemy in enemies:
        enemy.draw(screen)

def update():
    global frame_count, game_over, apple, head_frame
    if game_over:
        return

    frame_count += 1
    if frame_count < speed:
        return
    frame_count = 0
    head_frame += 1  # troca de sprite da cabeça

    for enemy in enemies:
        enemy.move()

    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)

    if (new_head in snake or
        new_head[0] < 0 or new_head[0] >= cols or
        new_head[1] < 0 or new_head[1] >= rows):
        game_over = True
        return

    for enemy in enemies:
        if new_head == enemy.get_position():
            game_over = True
            return

    snake.insert(0, new_head)

    if new_head == apple:
        apple = generate_apple()
    else:
        snake.pop()

def generate_apple():
    while True:
        pos = (random.randint(0, cols - 1), random.randint(0, rows - 1))
        if pos not in snake and all(pos != e.get_position() for e in enemies):
            return pos

def on_key_down(key):
    global direction
    if key.name == "UP" and direction != (0, 1):
        direction = (0, -1)
    elif key.name == "DOWN" and direction != (0, -1):
        direction = (0, 1)
    elif key.name == "LEFT" and direction != (1, 0):
        direction = (-1, 0)
    elif key.name == "RIGHT" and direction != (-1, 0):
        direction = (1, 0)

def on_mouse_down(pos):
    global game_over
    if game_over and play_again_btn.collidepoint(pos):
        reset()
