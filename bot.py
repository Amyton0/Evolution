from random import randint
import pygame
import sys

WIDTH = 1200
HEIGHT = 600
FOOD = 120
POISON = 60
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + 80))
screen.fill((255, 255, 255))
fps = 7
bots = []
bots_reserv = []
running = True
running_loc = True

clock = pygame.time.Clock()
random_location = ''


class Bot:
    def __init__(self, x, y, matrix=[randint(0, 64) for _ in range(64)]):  # создаём матрицу команд бота
        self.matrix = matrix
        self.see = 0
        self.health = 35
        self.u = 0
        self.x = x
        self.y = y
        self.counts = 0

    def step(self, x):  # бот шагает
        global b
        if self in bots:
            x1, y1 = self.x, self.y
            if 0 <= x <= 7:
                napr = (self.see + x) % 8
                if napr == 0:
                    self.sdvig(b.board[self.x - 1][self.y - 1])
                    if b.board[self.x - 1][self.y - 1] == 1:
                        self.y -= 1
                        self.x -= 1
                        self.health = 0
                    elif b.board[self.x - 1][self.y - 1] == 5:
                        self.y -= 1
                        self.x -= 1
                    elif b.board[self.x - 1][self.y - 1] == 4:
                        self.y -= 1
                        self.x -= 1
                        self.health += 10
                elif napr == 1:
                    self.sdvig(b.board[self.x - 1][self.y])
                    if b.board[self.x - 1][self.y] == 1:
                        self.x -= 1
                        self.health = 0
                    elif b.board[self.x - 1][self.y] == 5:
                        self.x -= 1
                    elif b.board[self.x - 1][self.y] == 4:
                        self.x -= 1
                        self.health += 10
                elif napr == 2:
                    self.sdvig(b.board[self.x - 1][self.y + 1])
                    if b.board[self.x - 1][self.y + 1] == 1:
                        self.x -= 1
                        self.y += 1
                        self.health = 0
                    elif b.board[self.x - 1][self.y + 1] == 5:
                        self.x -= 1
                        self.y += 1
                    elif b.board[self.x - 1][self.y + 1] == 4:
                        self.y += 1
                        self.x -= 1
                        self.health += 10
                elif napr == 3:
                    self.sdvig(b.board[self.x][self.y + 1])
                    if b.board[self.x][self.y + 1] == 1:
                        self.y += 1
                        self.health = 0
                    elif b.board[self.x][self.y + 1] == 5:
                        self.y += 1
                    elif b.board[self.x][self.y + 1] == 4:
                        self.y += 1
                        self.health += 10
                elif napr == 4:
                    self.sdvig(b.board[self.x + 1][self.y + 1])
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
                elif napr == 5:
                    self.sdvig(b.board[self.x + 1][self.y])
                    if b.board[self.x + 1][self.y] == 1:
                        self.x += 1
                        self.health = 0
                    elif b.board[self.x + 1][self.y] == 4:
                        self.x += 1
                        self.health += 10
                    elif b.board[self.x + 1][self.y] == 5:
                        self.x += 1
                elif napr == 6:
                    self.sdvig(b.board[self.x + 1][self.y - 1])
                    if b.board[self.x + 1][self.y - 1] == 1:
                        self.x += 1
                        self.y -= 1
                        self.health = 0
                    elif b.board[self.x + 1][self.y - 1] == 5:
                        self.x += 1
                        self.y -= 1
                    elif b.board[self.x + 1][self.y - 1] == 4:
                        self.x += 1
                        self.y -= 1
                        self.health += 10
                elif napr == 7:
                    self.sdvig(b.board[self.x][self.y - 1])
                    if b.board[self.x][self.y - 1] == 1:
                        self.y -= 1
                        self.health = 0
                    elif b.board[self.x][self.y - 1] == 5:
                        self.y -= 1
                    elif b.board[self.x][self.y - 1] == 4:
                        self.y -= 1
                        self.health += 10
                b.board[x1][y1] = 5
                b.board[self.x][self.y] = self

    def next_move(self):  # определяется следующий ход бота
        global b
        self.counts += 1
        if self.counts == 10:
            self.counts = 0
            return None
        command = self.matrix[self.u]
        x, y = self.x, self.y
        if b.board[x][y] == 1:
            self.health = 0
        if b.board[x][y] == 4:
            self.health += 10
        if 0 <= command <= 7:
            self.step(command)
            self.next_move()
        elif 8 <= command <= 15:
            if self.see == 0:
                if b.board[x - 1][y] == 1:
                    b.board[x - 1][y] = 4
                elif b.board[x - 1][y] == 4:
                    self.health += 10
                    b.board[x - 1][y] = 5
                self.sdvig(b.board[x - 1][y])
            elif self.see == 1:
                if b.board[x - 1][y + 1] == 1:
                    self.health += 10
                    b.board[x - 1][y + 1] = 5
                elif b.board[x - 1][y + 1] == 4:
                    self.health += 10
                    b.board[x - 1][y + 1] = 5
                self.sdvig(b.board[x - 1][y + 1])
            elif self.see == 2:
                if b.board[x][y + 1] == 1:
                    self.health += 10
                    b.board[x][y + 1] = 5
                elif b.board[x][y + 1] == 4:
                    self.health += 10
                    b.board[x][y + 1] = 5
                self.sdvig(b.board[x][y + 1])
            elif self.see == 3:
                if b.board[x + 1][y + 1] == 1:
                    self.health += 10
                    b.board[x + 1][y + 1] = 5
                elif b.board[x + 1][y + 1] == 4:
                    self.health += 10
                    b.board[x + 1][y + 1] = 5
                self.sdvig(b.board[x + 1][y + 1])
            elif self.see == 4:
                if b.board[x + 1][y] == 1:
                    self.health += 10
                    b.board[x + 1][y] = 5
                elif b.board[x + 1][y] == 4:
                    self.health += 10
                    b.board[x + 1][y] = 5
                self.sdvig(b.board[x + 1][y])
            elif self.see == 5:
                if b.board[x + 1][y - 1] == 1:
                    self.health += 10
                    b.board[x + 1][y - 1] = 5
                elif b.board[x + 1][y - 1] == 4:
                    self.health += 10
                    b.board[x + 1][y - 1] = 5
                self.sdvig(b.board[x + 1][y - 1])
            elif self.see == 6:
                if b.board[x][y - 1] == 1:
                    self.health += 10
                    b.board[x][y - 1] = 5
                elif b.board[x][y - 1] == 4:
                    self.health += 10
                    b.board[x][y - 1] = 5
                self.sdvig(b.board[x][y - 1])
            elif self.see == 7:
                if b.board[x - 1][y - 1] == 1:
                    self.health += 10
                    b.board[x - 1][y - 1] = 5
                elif b.board[x - 1][y - 1] == 4:
                    self.health += 10
                    b.board[x - 1][y - 1] = 5
                self.sdvig(b.board[x - 1][y - 1])
        elif 16 <= command <= 23:
            if command == 16:
                self.sdvig(b.board[x - 1][y - 1])
            elif command == 17:
                self.sdvig(b.board[x - 1][y])
            elif command == 18:
                self.sdvig(b.board[x - 1][y + 1])
            elif command == 19:
                self.sdvig(b.board[x][y + 1])
            elif command == 20:
                self.sdvig(b.board[x + 1][y + 1])
            elif command == 21:
                self.sdvig(b.board[x + 1][y])
            elif command == 22:
                self.sdvig(b.board[x + 1][y - 1])
            elif command == 23:
                self.sdvig(b.board[x][y - 1])
            self.next_move()
        elif 24 <= command <= 31:
            self.see = (self.see + (command - 24)) % 8
            self.sdvig(1)
            self.next_move()
        elif 32 <= command <= 63:
            self.sdvig(command)
            self.next_move()

    def sdvig(self, s):  # сдвиг в матрице
        if str(s) == 'bot':
            self.u = (self.u + 3) % 64
        else:
            self.u = (self.u + s) % 64

    def __str__(self):
        return 'bot'


class Board:
    def __init__(self, width, height):  # создание поля
        self.width = width
        self.height = height
        self.board = [[5 for __ in range(height)] for _ in range(width)]
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if i == 0 or j == 0 or j == self.height - 1 or i == self.width - 1:
                    self.board[i][j] = 2
        self.left = 0
        self.top = 0
        self.cell_size = 30
        self.cell = ''

    def render(self):  # рисование поля
        for x in range(self.width):
            for y in range(self.height):
                if str(self.board[x][y]) == 'bot':
                    if self.board[x][y] in bots:
                        pygame.draw.rect(screen, (0, 0, 255), (
                            self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size))
                        pygame.draw.rect(screen, (150, 150, 150), (
                            self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size),
                                         1)
                        hp = str(self.board[x][y].health)
                        f1 = pygame.font.Font(None, 30)
                        text1 = f1.render(hp, 1, (255, 255, 255))
                        screen.blit(text1, (self.left + x * self.cell_size + self.cell_size // 8,
                                            self.top + y * self.cell_size + self.cell_size // 7))
                    else:
                        self.board[x][y] = 5
                elif self.board[x][y] == 1:
                    pygame.draw.rect(screen, (255, 0, 0), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, (150, 150, 150), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size),
                                     1)
                elif self.board[x][y] == 3:
                    pygame.draw.rect(screen, (0, 0, 255), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, (150, 150, 150), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size),
                                     1)
                elif self.board[x][y] == 2:
                    pygame.draw.rect(screen, (128, 128, 128), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, (150, 150, 150), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size),
                                     1)
                elif self.board[x][y] == 4:
                    pygame.draw.rect(screen, (0, 255, 0), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, (150, 150, 150), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size),
                                     1)
                else:
                    pygame.draw.rect(screen, (0, 0, 0), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size))
                    pygame.draw.rect(screen, (150, 150, 150), (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                        self.cell_size),
                                     1)
        if self.cell and self.cell[0] != 0 and self.cell[1] != self.height - 1 and self.cell[1] != 0 and \
                self.cell[0] != self.width - 1 and running_loc:
            pygame.draw.rect(screen, (255, 215, 0), (
                self.cell[0] * self.cell_size - 1, self.cell[1] * self.cell_size - 1, self.cell_size + 1,
                self.cell_size + 1), 2)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def set_poison(self, n):  # расставляем n единиц яда
        for _ in range(n):
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            while self.board[x][y] != 5:
                x = randint(0, self.width - 1)
                y = randint(0, self.height - 1)
            self.board[x][y] = 1

    def set_food(self, n):  # расставляем n единиц еды
        for _ in range(n):
            x = randint(0, self.width - 1)
            y = randint(0, self.height - 1)
            while self.board[x][y] != 5:
                x = randint(0, self.width - 1)
                y = randint(0, self.height - 1)
            self.board[x][y] = 4

    def set_bot(self, n):  # расставляем n ботов
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

    def get_cell(self, mouse_pos):  # отпределяется, на какую клетку поля нажали
        for i in range(self.height):
            for j in range(self.width):
                if self.left + self.cell_size * j <= mouse_pos[0] <= self.left + self.cell_size * (j + 1) and \
                        self.top + self.cell_size * i <= mouse_pos[1] <= self.top + self.cell_size * (i + 1):
                    return (j, i)

    def on_click(self, cell_coords):
        if cell_coords:
            self.cell = cell_coords

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
        screen.fill((0, 0, 0))
        self.render()
        pygame.display.flip()

    def key_press(self, key):  # ставим еду/яд/бота в пользовательской расстановке
        if self.cell:
            if key == pygame.K_p:
                if b.board[self.cell[0]][self.cell[1]] == 1:
                    b.board[self.cell[0]][self.cell[1]] = 5
                else:
                    b.board[self.cell[0]][self.cell[1]] = 1
            if key == pygame.K_w:
                if b.board[self.cell[0]][self.cell[1]] == 2:
                    b.board[self.cell[0]][self.cell[1]] = 5
                else:
                    b.board[self.cell[0]][self.cell[1]] = 2
            if key == pygame.K_f:
                if b.board[self.cell[0]][self.cell[1]] == 4:
                    b.board[self.cell[0]][self.cell[1]] = 5
                else:
                    b.board[self.cell[0]][self.cell[1]] = 4
            pygame.display.flip()
            b.render()


def new_poko():  # боты клонируются и мутируют
    global bots_reserv, bots
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
        x = randint(1, b.width - 2)
        y = randint(1, b.height - 2)
        while b.board[x][y] != 5:
            x = randint(1, b.width - 2)
            y = randint(1, b.height - 2)
        bo = Bot(x, y, m)
        bots.append(bo)
        b.board[x][y] = bo


def start_screen():  # начальный экран (с правилами игры)
    intro_text = ["", "", "ЭВОЛЮЦИЯ", "", "", "", "Боты перемещаются в зависимости от команд в их матрицах, едят " +
                  "еду, яд, ", "клонируются, мутируют. На каждом боте написано, сколько у него здоровья. ",
                  "Расставлять еду и яд можно случайным образом, а можно самостоятельно. ", "Изначально стены " +
                  "только по краям, но можно их поставить и в других местах", "При пользовательской расстановке " +
                  "чтобы поставить еду - жмите f, яд - p, а стену - w. ",
                  "Чтобы убрать элемент, нажмите на ту же кнопку второй раз.",
                  "После расстановки еды и яда нужно нажать Enter"]

    screen.fill((173, 255, 47))
    font = pygame.font.Font(None, 40)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(fps)
    pygame.display.flip()


def game():  # сама игра
    global running_loc, random_location, running, POISON, FOOD, fps, bots, bots_reserv, b
    q = False

    while running_loc:  # кнопки меню и пользовательская расстановка
        while not str(random_location):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    running_loc = False
                    random_location = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if (WIDTH + 80) // 2 - 160 <= event.pos[0] <= (WIDTH + 80) // 2 + 160 and \
                                HEIGHT // 2 - 150 <= event.pos[1] <= HEIGHT // 2 - 30:
                            random_location = True
                        if (WIDTH + 80) // 2 - 160 <= event.pos[0] <= (WIDTH + 80) // 2 + 160 and \
                                HEIGHT // 2 + 55 <= event.pos[1] <= HEIGHT // 2 + 175:
                            random_location = False

            screen.fill((127, 255, 212))
            pygame.draw.rect(screen, (70, 130, 180), ((WIDTH + 80) // 2 - 160, HEIGHT // 2 - 150, 320, 120), 0)
            pygame.draw.rect(screen, (70, 130, 180), ((WIDTH + 80) // 2 - 160, HEIGHT // 2 + 55, 320, 120), 0)
            font = pygame.font.Font(None, 50)
            text = font.render("Случайная", 1, (255, 255, 255))
            text_ = font.render("расстановка", 1, (255, 255, 255))
            text_x = (WIDTH + 80) // 2 - text.get_width() // 2
            text_y = HEIGHT // 2 - 150 + text.get_height() // 2
            text__x = (WIDTH + 80) // 2 - text.get_width() // 2 - 10
            text__y = HEIGHT // 2 + text.get_height() - 120
            text1 = font.render("Пользовательская", 1, (255, 255, 255))
            text1_ = font.render("расстановка", 1, (255, 255, 255))
            text1_x = (WIDTH + 80) // 2 - text.get_width() // 2 - 65
            text1_y = HEIGHT // 2 + 55 + text.get_height() // 2
            text1__x = (WIDTH + 80) // 2 - text.get_width() // 2 - 10
            text1__y = HEIGHT // 2 + 90 + text.get_height()
            screen.blit(text, (text_x, text_y))
            screen.blit(text_, (text__x, text__y))
            screen.blit(text1, (text1_x, text1_y))
            screen.blit(text1_, (text1__x, text1__y))
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                running_loc = False
                q = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if WIDTH // 2 - 160 <= event.pos[0] <= WIDTH // 2 + 160 and \
                            HEIGHT + 15 <= event.pos[1] <= HEIGHT + 65:
                        fps = 7
                        bots = []
                        bots_reserv = []
                        running = True
                        running_loc = True
                        random_location = ''
                        b = Board(40, 20)
                        FOOD = 120
                        POISON = 60
                        game()
                    b.get_click(event.pos)
            if event.type == pygame.KEYDOWN:
                b.key_press(event.key)
                if event.key == pygame.K_RETURN:
                    running_loc = False
        screen.fill((200, 200, 200))
        pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 2 - 160, HEIGHT + 15, 320, 50), 1)
        font = pygame.font.Font(None, 50)
        text = font.render("В меню", 1, (0, 0, 0))
        text_x = WIDTH // 2 - 70
        text_y = HEIGHT + 25
        screen.blit(text, (text_x, text_y))
        b.render()
        pygame.display.flip()
        if random_location:
            running_loc = False

    if not q:
        b.set_bot(64)
    if random_location:
        b.set_poison(POISON)
        b.set_food(FOOD)
    else:
        POISON = 0
        FOOD = 0
        for i in b.board:
            POISON += i.count(1)
            FOOD += i.count(4)
    b.render()
    pygame.display.flip()

    while running:  # цикл игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if WIDTH // 2 - 160 <= event.pos[0] <= WIDTH // 2 + 160 and \
                            HEIGHT + 15 <= event.pos[1] <= HEIGHT + 65:
                        fps = 7
                        bots = []
                        bots_reserv = []
                        running = True
                        running_loc = True
                        random_location = ''
                        b = Board(40, 20)
                        FOOD = 120
                        POISON = 60
                        game()
                if event.button == 4:
                    fps += 1
                if event.button == 5:
                    if fps != 0:
                        fps -= 1

        screen.fill((200, 200, 200))
        pygame.draw.rect(screen, (0, 0, 0), (WIDTH // 2 - 160, HEIGHT + 15, 320, 50), 1)
        font = pygame.font.Font(None, 50)
        text = font.render("В меню", 1, (0, 0, 0))
        text_x = WIDTH // 2 - 70
        text_y = HEIGHT + 25
        screen.blit(text, (text_x, text_y))
        poison_ = 0
        food_ = 0
        for i in b.board:
            poison_ += i.count(1)
            food_ += i.count(4)
        if poison_ < POISON:
            b.set_poison(POISON - poison_)
        if food_ < FOOD:
            b.set_food(FOOD - food_)
        for i in bots:
            i.health -= 1
            if i.health < 1:
                b.board[i.x][i.y] = 5
                bots.remove(i)
            i.next_move()
            if 5 in b.board[0] or 5 in b.board[-1]:
                running = False
            if len(bots) <= 8:
                bots_reserv = bots[:]
                for i in bots:
                    b.board[i.x][i.y] = 5
                bots.clear()
                new_poko()
        clock.tick(fps)

        b.render()
        pygame.display.flip()


b = Board(40, 20)

start_screen()
game()
pygame.quit()
