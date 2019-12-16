from random import randint
import pygame
import numpy as np


class Bot:
    def __init__(self):
        self.matrix = [randint(0, 64) for i in range(64)]
        self.see = 0
        self.health = 35
        self.u = 0
        self.x = 0
        self.y = 0
        self.counts = 0

    def step(self, x):
        global b


    def next_move(self):
        global b
        self.counts += 1
        self.health -= 1
        if self.counts == 10:
            self.counts = 0
            return None
        command = self.matrix[self.u]
        if 0 <= command <= 7:
            self.step(command)
        elif 8 <= command <= 15:
            pass # step
        elif 16 <= command <= 23:
            x, y = self.x, self.y
            if command == 16:
                self.sdvig(b.board[y - 1][x - 1])
            elif command == 17:
                self.sdvig(b.board[y - 1][x])
            elif command == 18:
                self.sdvig(b.board[y - 1][x + 1])
            elif command == 19:
                self.sdvig(b.board[y][x + 1])
            elif command == 20:
                self.sdvig(b.board[y + 1][x + 1])
            elif command == 21:
                self.sdvig(b.board[y + 1][x])
            elif command == 22:
                self.sdvig(b.board[y + 1][x - 1])
            elif command == 23:
                self.sdvig(b.board[y][x - 1])
            self.next_move()
        elif 24 <= command <= 31:
            self.see = (self.see + (command - 24)) % 8
            self.sdvig(1)
            self.next_move()
        elif 32 <= command <= 63:
            self.sdvig(command)
            self.next_move()

    def sdvig(self, s):
        if str(s) == 'bot':
            self.u = (self.u + 3) % 64
        else:
            self.u = (self.u + s) % 64

    def __str__(self):
        return 'bot'


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = np.array([[5] * height for _ in range(width)])
        self.board[0] = 2
        self.board[:][0] = 2
        self.left = 0
        self.top = 0
        self.cell_size = 20

    def render(self):
        for x in range(self.height):
            for y in range(self.width):
                if str(self.board[y][x]) == 'bot':
                    pygame.draw.rect(screen, (0, 0, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size))
                    pygame.draw.rect(screen, (255, 255, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size),
                                     1)
                    f1 = pygame.font.Font(None, 36)
                    text1 = f1.render(self.board[y][x].health, 1, (255, 255, 255))
                    screen.blit(text1, (self.left + x * self.cell_size, self.top + y * self.cell_size))
                elif self.board[y][x] == 1:
                    pygame.draw.rect(screen, (255, 0, 0), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, (255, 255, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size),
                                     1)
                elif self.board[y][x] == 3:
                    pygame.draw.rect(screen, (0, 0, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, (255, 255, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size),
                                     1)
                elif self.board[y][x] == 2:
                    pygame.draw.rect(screen, (128, 128, 128), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, (255, 255, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size),
                                     1)
                elif self.board[y][x] == 4:
                    pygame.draw.rect(screen, (0, 255, 0), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, (255, 255, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size),
                                     1)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, (255, 255, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size),
                                     1)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def set_poison(self, n):
        for i in range(n):
            x = randint(0, 8)
            y = randint(0, 8)
            while self.board[y][x] != 0:
                x = randint(0, 8)
                y = randint(0, 8)
            self.board[y][x] = -1

    def set_food(self, n):
        for i in range(n):
            x = randint(0, 8)
            y = randint(0, 8)
            while self.board[y][x] != 0:
                x = randint(0, 8)
                y = randint(0, 8)
            self.board[y][x] = 5

    def get_click(self, mouse_pos):
        pass
        # cell = self.get_cell(mouse_pos)
        # if cell:
        #    self.on_click(cell[0], cell[1])

    def get_cell(self, mouse_pos):
        pass
        # x = (mouse_pos[0] - self.left) // self.cell_size
        # y = (mouse_pos[1] - self.top) // self.cell_size
        # if x < 0 or y < 0 or y >= self.width or x >= self.height:
        #    return None
        # else:
        #    return (x, y)

    def on_click(self, x, y):
        pass
        # if self.board[y][x] == 0:
        #    self.board[y][x] = 1
        # elif self.board[y][x] == 1:
        #    self.board[y][x] = 2
        # else:
        #    self.board[y][x] = 0

        # self.render()


pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
fps = 50
bots = []
b = Board(40, 20)
b.set_poison(50)
b.render()
clock = pygame.time.Clock()
running = True
for i in range(64):
    bots.append(Bot())
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in bots:
        i.next_move()
    b.render()
    pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
