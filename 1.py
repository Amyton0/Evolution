from random import randint
import pygame


class Bot:
    def __init__(self, x, y, matrix=[randint(0, 64) for _ in range(64)]):
        self.matrix = matrix
        self.see = 0
        self.health = 35
        self.u = 0
        self.x = x
        self.y = y
        self.counts = 0

    def step(self, x):
        global b
        x1, y1 = self.x, self.y
        if 0 <= x <= 7:
            napr = (self.see + x) % 8
            if napr == 0:
                if b.board[self.y + 1][self.x - 1] == 1:
                    self.y += 1
                    self.x -= 1
                    self.health = 0
                elif b.board[self.y + 1][self.x - 1] == 5:
                    self.y += 1
                    self.x -= 1
                self.sdvig(b.board[self.y + 1][self.x - 1])
            elif napr == 1:
                if b.board[self.y + 1][self.x] == 1:
                    self.y += 1
                    self.health = 0
                elif b.board[self.y + 1][self.x] == 5:
                    self.y += 1
                self.sdvig(b.board[self.y + 1][self.x])
            elif napr == 2:
                if b.board[self.y + 1][self.x + 1] == 1:
                    self.x += 1
                    self.y += 1
                    self.health = 0
                elif b.board[self.y + 1][self.x + 1] == 5:
                    self.x += 1
                    self.y += 1
                self.sdvig(b.board[self.y + 1][self.x + 1])
            elif napr == 3:
                if b.board[self.y][self.x + 1] == 1:
                    self.x += 1
                    self.health = 0
                elif b.board[self.y][self.x + 1] == 5:
                    self.x += 1
                self.sdvig(b.board[self.y][self.x + 1])
            elif napr == 4:
                if b.board[self.x + 1][self.y + 1] == 1:
                    self.x += 1
                    self.y += 1
                    self.health = 0
                elif b.board[self.x + 1][self.y + 1] == 4:
                    self.y += 1
                    self.x += 1
                    self.health += 10
                elif b.board[self.x + 1][self.y + 1] == 5:
                    self.x += 1
                    self.y += 1
                self.sdvig(b.board[self.x + 1][self.y + 1])
            elif napr == 5:
                if b.board[self.x][self.y + 1] == 1:
                    self.y += 1
                    self.health = 0
                elif b.board[self.x][self.y + 1] == 4:
                    self.y += 1
                    self.health += 10
                elif b.board[self.x][self.y + 1] == 5:
                    self.y += 1
                self.sdvig(b.board[self.x][self.y + 1])
            elif napr == 6:
                if b.board[self.y - 1][self.x - 1] == 1:
                    self.x -= 1
                    self.y -= 1
                    self.health = 0
                elif b.board[self.y - 1][self.x - 1] == 5:
                    self.x -= 1
                    self.y -= 1
                self.sdvig(b.board[self.y - 1][self.x - 1])
            elif napr == 7:
                if b.board[self.y][self.x - 1] == 1:
                    self.x -= 1
                    self.health = 0
                elif b.board[self.y][self.x - 1] == 5:
                    self.x -= 1
                self.sdvig(b.board[self.y][self.x - 1])
            b.board[x1][y1] = 5
            b.board[self.x][self.y] = self

    def next_move(self):
        global b
        self.counts += 1
        if self.counts == 10:
            self.counts = 0
            return None
        if self.health == 0:
            bots.remove(self)
            b.board[self.x][self.y] = 5
            return None
        command = self.matrix[self.u]
        x, y = self.x, self.y
        if 0 <= command <= 7:
            self.step(command)
            self.next_move()
        elif 8 <= command <= 15:
            if self.see == 0:
                if b.board[y - 1][x] == 1:
                    self.health += 10
                    b.board[y - 1][x] = 5
                    b.set_poison(1)
                elif b.board[y - 1][x] == 4:
                    self.health += 10
                    b.board[y - 1][x] = 5
                    b.set_food(1)
                self.sdvig(b.board[y - 1][x])
            elif self.see == 1:
                if b.board[y - 1][x + 1] == 1:
                    self.health += 10
                    b.board[y - 1][x + 1] = 5
                    b.set_poison(1)
                elif b.board[y - 1][x + 1] == 4:
                    self.health += 10
                    b.board[y - 1][x + 1] = 5
                    b.set_food(1)
                self.sdvig(b.board[y - 1][x + 1])
            elif self.see == 2:
                if b.board[y][x + 1] == 1:
                    self.health += 10
                    b.board[y][x + 1] = 5
                    b.set_poison(1)
                elif b.board[y][x + 1] == 4:
                    self.health += 10
                    b.board[y][x + 1] = 5
                    b.set_food(1)
                self.sdvig(b.board[y][x + 1])
            elif self.see == 3:
                if b.board[y + 1][x + 1] == 1:
                    self.health += 10
                    b.board[y + 1][x + 1] = 5
                    b.set_poison(1)
                elif b.board[y + 1][x + 1] == 4:
                    self.health += 10
                    b.board[y + 1][x + 1] = 5
                    b.set_food(1)
                self.sdvig(b.board[y + 1][x + 1])
            elif self.see == 4:
                if b.board[y + 1][x] == 1:
                    self.health += 10
                    b.board[y + 1][x] = 5
                    b.set_poison(1)
                elif b.board[y + 1][x] == 4:
                    self.health += 10
                    b.board[y + 1][x] = 5
                    b.set_food(1)
                self.sdvig(b.board[y + 1][x])
            elif self.see == 5:
                if b.board[y + 1][x - 1] == 1:
                    self.health += 10
                    b.board[y + 1][x - 1] = 5
                    b.set_poison(1)
                elif b.board[y + 1][x - 1] == 4:
                    self.health += 10
                    b.board[y + 1][x - 1] = 5
                    b.set_food(1)
                self.sdvig(b.board[y + 1][x - 1])
            elif self.see == 6:
                if b.board[y][x - 1] == 1:
                    self.health += 10
                    b.board[y][x - 1] = 5
                elif b.board[y][x - 1] == 4:
                    self.health += 10
                    b.board[y][x - 1] = 5
                    b.set_food(1)
                self.sdvig(b.board[y][x - 1])
            elif self.see == 7:
                if b.board[y - 1][x - 1] == 1:
                    b.board[y - 1][x - 1] = 4
                    b.set_poison(1)
                elif b.board[y - 1][x - 1] == 4:
                    self.health += 10
                    b.board[y - 1][x - 1] = 5
                    b.set_food(1)
                self.sdvig(b.board[y - 1][x - 1])
        elif 16 <= command <= 23:
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
            self.u = (self.u + 3) % 5
        else:
            self.u = (self.u + s) % 5

    def __str__(self):
        return 'bot'


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[5 for __ in range(height)] for _ in range(width)]
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if i == 0 or j == 0 or i == self.height - 1 or j == self.width - 1:
                    self.board[i][j] = 2
        self.left = 0
        self.top = 0
        self.cell_size = 30

    def render(self):
        for x in range(self.width):
            for y in range(self.height):
                if str(self.board[x][y]) == 'bot':
                    pygame.draw.rect(screen, (0, 0, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size))
                    pygame.draw.rect(screen, (255, 255, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size),
                                     1)
                    hp = str(self.board[x][y].health)
                    f1 = pygame.font.Font(None, 30)
                    text1 = f1.render(hp, 1, (255, 255, 255))
                    screen.blit(text1, (self.left + x * self.cell_size + self.cell_size // 8,
                                        self.top + y * self.cell_size + self.cell_size // 7))
                elif self.board[x][y] == 1:
                    pygame.draw.rect(screen, (255, 0, 0), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, (255, 255, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size),
                                     1)
                elif self.board[x][y] == 3:
                    pygame.draw.rect(screen, (0, 0, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, (255, 255, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size),
                                     1)
                elif self.board[x][y] == 2:
                    pygame.draw.rect(screen, (128, 128, 128), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, (255, 255, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size),
                                     1)
                elif self.board[x][y] == 4:
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
        for _ in range(n):
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            while self.board[x][y] != 5:
                x = randint(0, self.width - 1)
                y = randint(0, self.height - 1)
            self.board[x][y] = 1

    def set_food(self, n):
        for _ in range(n):
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            while self.board[x][y] != 5:
                x = randint(0, self.width - 1)
                y = randint(0, self.height - 1)
            self.board[x][y] = 4

    def set_bot(self, n):
        global bots
        for _ in range(n):
            x = randint(1, self.width - 2)
            y = randint(1, self.height - 2)
            while self.board[x][y] != 5:
                x = randint(1, self.width - 2)
                y = randint(1, self.height - 2)
            bo = Bot(x, y)
            bots.append(bo)
            self.board[x][y] = bo


def new_poko():
    for i in bots_reserv:
        for j in range(7):
            x = randint(1, b.width - 2)
            y = randint(1, b.height - 2)
            while b.board[x][y] != 5:
                x = randint(1, b.width - 2)
                y = randint(1, b.height - 2)
            bo = Bot(x, y, i.matrix)
            bots.append(bo)
            b.board[x][y] = bo
        m = i.matrix
        a = randint(0, 63)
        m[a] = randint(0, 63)
        bo = Bot(x, y, m)
        bots.append(bo)
        b.board[x][y] = bo


pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))
fps = 10
bots = []
bots_reserv = []
b = Board(20, 20)
b.set_poison(3)
b.set_food(3)
b.set_bot(1)
b.render()
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in bots:
        i.health -= 1
        i.next_move()
        if len(bots) <= 8:
            bots_reserv = bots[:]
            bots.clear()
            new_poko()
    clock.tick(fps)
    b.render()
    pygame.display.flip()
pygame.quit()
