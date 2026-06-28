import pygame
import random
import time

pygame.init()

# ---------------- SCREEN ----------------
WIDTH, HEIGHT = 1000, 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bulb Detective 💡")

# ---------------- COLORS ----------------
WHITE = (255,255,255)
BLACK = (0,0,0)
BG = (25,25,25)

GREEN = (0,180,0)
ORANGE = (255,165,0)
RED = (200,0,0)

# ---------------- FONTS ----------------
title_font = pygame.font.SysFont(None,70)
font = pygame.font.SysFont(None,40)
small_font = pygame.font.SysFont(None,30)

# ---------------- IMAGES ----------------
bulb_on = pygame.image.load("bulb_on.webp")
bulb_off = pygame.image.load("bulb_off.png")

bulb_on = pygame.transform.scale(bulb_on,(60,60))
bulb_off = pygame.transform.scale(bulb_off,(60,60))

# ---------------- STATES ----------------
MENU = "menu"
INFO = "info"
GAME = "game"
WIN = "win"
TIMEUP = "timeup"

game_state = MENU

# ---------------- GAME DATA ----------------
difficulty = ""
time_limit = 30
remaining = 30

bulb_positions = []
bulb_states = []

score = 0
high_score = 0

start_time = 0
current_condition = ""

# ---------------- BUTTONS ----------------
easy_button = pygame.Rect(200,400,180,60)
medium_button = pygame.Rect(420,400,180,60)
hard_button = pygame.Rect(640,400,180,60)

start_button = pygame.Rect(400,600,200,60)
restart_button = pygame.Rect(800,30,160,50)

# ---------------- BULBS ----------------
def create_bulbs(rows, cols):
    positions = []
    start_x = 250
    start_y = 220
    gap_x = 120
    gap_y = 100

    for r in range(rows):
        for c in range(cols):
            positions.append((start_x + c*gap_x, start_y + r*gap_y))

    return positions

# ---------------- CONDITIONS ----------------
conditions = [
    "Turn ON all bulbs",
    "Turn OFF all bulbs",
    "Make exactly half ON",
    "More ON than OFF"
]

# ---------------- LOAD LEVEL ----------------
def load_level():
    global bulb_positions, bulb_states, current_condition

    if difficulty == "Easy":
        bulb_positions = create_bulbs(2,4)
        time_limit = 30

    elif difficulty == "Medium":
        bulb_positions = create_bulbs(3,4)
        time_limit = 20

    else:
        bulb_positions = create_bulbs(4,4)
        time_limit = 10

    bulb_states = [True]*len(bulb_positions)
    current_condition = random.choice(conditions)

# ---------------- CHECK WIN ----------------
def check_condition():
    on = bulb_states.count(True)
    off = bulb_states.count(False)

    if current_condition == "Turn ON all bulbs":
        return on == len(bulb_states)

    if current_condition == "Turn OFF all bulbs":
        return off == len(bulb_states)

    if current_condition == "Make exactly half ON":
        return on == len(bulb_states)//2

    if current_condition == "More ON than OFF":
        return on > off

    return False

# ---------------- MAIN LOOP ----------------
running = True
while running:

    screen.fill(BG)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            # -------- MENU --------
            if game_state == MENU:

                if easy_button.collidepoint(mouse_x, mouse_y):
                    difficulty = "Easy"
                    load_level()
                    game_state = INFO

                if medium_button.collidepoint(mouse_x, mouse_y):
                    difficulty = "Medium"
                    load_level()
                    game_state = INFO

                if hard_button.collidepoint(mouse_x, mouse_y):
                    difficulty = "Hard"
                    load_level()
                    game_state = INFO

            # -------- INFO --------
            elif game_state == INFO:

                if start_button.collidepoint(mouse_x, mouse_y):
                    game_state = GAME
                    start_time = time.time()

            # -------- GAME --------
            elif game_state == GAME:

                if restart_button.collidepoint(mouse_x, mouse_y):
                    load_level()
                    start_time = time.time()

                for i,(x,y) in enumerate(bulb_positions):
                    dist = ((mouse_x-x)**2 + (mouse_y-y)**2)**0.5

                    if dist < 40:
                        bulb_states[i] = not bulb_states[i]

                        if check_condition():
                            game_state = WIN

    # ---------------- TIMER ----------------
    if game_state == GAME:
        elapsed = int(time.time() - start_time)
        remaining = max(0, time_limit - elapsed)

        if remaining == 0:
            game_state = TIMEUP

    # ---------------- MENU SCREEN ----------------
    if game_state == MENU:

        screen.blit(title_font.render("💡 BULB DETECTIVE",True,WHITE),(250,100))
        screen.blit(font.render("Select Difficulty",True,WHITE),(360,200))

        pygame.draw.rect(screen,GREEN,easy_button)
        pygame.draw.rect(screen,ORANGE,medium_button)
        pygame.draw.rect(screen,RED,hard_button)

        screen.blit(font.render("Easy",True,WHITE),easy_button.move(55,15))
        screen.blit(font.render("Medium",True,WHITE),medium_button.move(30,15))
        screen.blit(font.render("Hard",True,WHITE),hard_button.move(50,15))

    # ---------------- INFO SCREEN ----------------
    if game_state == INFO:

        screen.blit(title_font.render(f"LEVEL : {difficulty}",True,WHITE),(320,120))
        screen.blit(font.render(f"{len(bulb_positions)} Bulbs",True,WHITE),(380,220))
        screen.blit(font.render(f"{time_limit} Seconds",True,WHITE),(380,270))
        screen.blit(font.render("4 Conditions",True,WHITE),(380,320))

        pygame.draw.rect(screen,GREEN,start_button)
        screen.blit(font.render("START",True,WHITE),start_button.move(60,15))

    # ---------------- GAME SCREEN ----------------
    if game_state == GAME:

        # bulbs
        for i,(x,y) in enumerate(bulb_positions):
            if bulb_states[i]:
                screen.blit(bulb_on,(x,y))
            else:
                screen.blit(bulb_off,(x,y))

        # UI
        score = bulb_states.count(False)

        screen.blit(font.render(f"Score: {score}",True,WHITE),(20,20))
        screen.blit(font.render(f"Time: {remaining}",True,WHITE),(20,70))
        screen.blit(font.render(current_condition,True,WHITE),(20,120))

        pygame.draw.rect(screen,GREEN,restart_button)
        screen.blit(font.render("Restart",True,WHITE),restart_button.move(20,10))

    # ---------------- WIN SCREEN ----------------
    if game_state == WIN:
        screen.blit(title_font.render("🎉 YOU WIN!",True,GREEN),(320,300))

    # ---------------- TIMEUP SCREEN ----------------
    if game_state == TIMEUP:
        screen.blit(title_font.render("TIME UP!",True,RED),(350,300))

    pygame.display.update()

pygame.quit()