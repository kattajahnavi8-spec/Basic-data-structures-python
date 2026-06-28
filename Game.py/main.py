from random import random
import pygame
pygame.init()
WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bulb Detective 💡")
BACKGROUND = (25, 25, 25)
bulb_on = pygame.image.load("bulb_on.webp")
bulb_off = pygame.image.load("bulb_off.png")
bulb_on = pygame.transform.scale(bulb_on, (60, 60))
bulb_off = pygame.transform.scale(bulb_off, (60, 60))
bulb_positions = []
def create_bulbs(rows, cols):
    positions = []
    start_x = 180
    start_y = 340
    gap_x = 120
    gap_y = 100
    for r in range(rows):
        for c in range(cols):
            positions.append(
                (start_x + c * gap_x,start_y + r * gap_y))
    return positions
bulb_positions = create_bulbs(2, 4)   
bulb_states = [True] * len(bulb_positions)
font = pygame.font.SysFont(None, 40)
GREEN = (0, 180, 0)
WHITE = (255, 255, 255)
start_button = pygame.Rect(450, 20, 140, 45)
restart_button = pygame.Rect(620, 20, 160, 45)
game_started = False
import time
time_limit = 30
remaining = time_limit
start_time = 0
import random
score = 0
high_score = 0
conditions = [
    "Turn ON all bulbs",
    "Turn OFF all bulbs",
    "Make exactly 5 bulbs ON",
    "Make more ON bulbs than OFF bulbs"
]
current_condition = random.choice(conditions)
easy_button = pygame.Rect(180, 320, 120, 60)
medium_button = pygame.Rect(370, 320, 140, 60)
hard_button = pygame.Rect(580, 320, 120, 60)
difficulty = "Easy"
game_state = "menu"
running = True
def check_condition():
    on_count = bulb_states.count(True)
    off_count = bulb_states.count(False)
    if current_condition == "Turn ON all bulbs":
        return on_count == 8
    elif current_condition == "Turn OFF all bulbs":
        return off_count == 8
    elif current_condition == "Make exactly 5 bulbs ON":
        return on_count == 5
    elif current_condition == "Make more ON bulbs than OFF bulbs":
        return on_count > off_count
    return False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if easy_button.collidepoint(mouse_x, mouse_y):
                difficulty = "Easy"
                time_limit = 30
                bulb_positions = create_bulbs(2, 4)
                bulb_states = [True] * len(bulb_positions)
                game_state = "info"
                
            elif medium_button.collidepoint(mouse_x, mouse_y):
                difficulty = "Medium"
                time_limit = 20
                bulb_positions = create_bulbs(3, 4)
                bulb_states = [True] * len(bulb_positions)
                game_state = "info"
                
            elif hard_button.collidepoint(mouse_x, mouse_y):
                difficulty = "Hard"
                time_limit = 10
                bulb_positions = create_bulbs(4, 4)
                bulb_states = [True] * len(bulb_positions)
                game_state = "info"
                
            elif game_state == "info" and start_button.collidepoint(mouse_x, mouse_y):
                game_started = True
                game_state = "game"
                start_time = time.time()
                current_condition = random.choice(conditions)
            elif game_state == "info" and restart_button.collidepoint(mouse_x, mouse_y):
                bulb_states = [True] * 8
                game_started = False
                current_condition = random.choice(conditions)
            elif game_started:
                for i, (x, y) in enumerate(bulb_positions):
                    distance = ((mouse_x - x) ** 2 + (mouse_y - y) ** 2) ** 0.5
                    if distance < 40:
                        bulb_states[i] = not bulb_states[i]
                        if check_condition():
                            game_started = False
                            game_state = "win"
    screen.fill(BACKGROUND)
    if game_state == "menu":
        title_font = pygame.font.SysFont(None, 70)
        sub_font = pygame.font.SysFont(None, 45)
        title = title_font.render("💡 BULB DETECTIVE", True, WHITE)
        screen.blit(title, (180, 120))
        subtitle = sub_font.render("Select Difficulty", True, WHITE)
        screen.blit(subtitle, (280, 220))
    if game_started:
        elapsed = int(time.time() - start_time)
        remaining = max(0, time_limit - elapsed)
        if remaining == 0:
            game_started = False
    score = bulb_states.count(False)
    if score > high_score:
        high_score = score
    if game_state == "info":
        pygame.draw.rect(screen, GREEN, start_button)
        start_text = font.render("Start", True, WHITE)
        screen.blit(start_text, start_text.get_rect(center = start_button.center))
        title = font.render(f"LEVEL : {difficulty}", True, WHITE)
        screen.blit(title, (300,180))
        if difficulty == "Easy":
            screen.blit(font.render("> 8 Bulbs", True, WHITE), (300,240))
            screen.blit(font.render("> 30 Seconds", True, WHITE), (300,280))
            screen.blit(font.render("> 4 Conditions", True, WHITE), (300,320))
        elif difficulty == "Medium":
            screen.blit(font.render("> 12 Bulbs", True, WHITE), (300,240))
            screen.blit(font.render("> 20 Seconds", True, WHITE), (300,280))
            screen.blit(font.render("> 5 Conditions", True, WHITE), (300,320))
        else:
            screen.blit(font.render("> 16 Bulbs", True, WHITE), (300,240))
            screen.blit(font.render("> 10 Seconds", True, WHITE), (300,280))
            screen.blit(font.render("> 6 Conditions", True, WHITE), (300,320))
            info = font.render("Press START to Begin", True, (0,255,0))
            screen.blit(info, (250,400))
    elif game_state == "game":   
        pygame.draw.rect(screen, GREEN, restart_button)
        restart_text = font.render("Restart", True, WHITE)
        screen.blit(restart_text, (650, 30))
    elif game_state == "game":
        for i, (x, y) in enumerate(bulb_positions):
            if bulb_states[i]:
                screen.blit(bulb_on, (x-30, y-30))
            else:
                screen.blit(bulb_off, (x-30, y-30))
    timer_text = font.render(f"Time : {remaining}", True, WHITE)
    score_text = font.render(f"Score : {score}/{len(bulb_states)}",True,WHITE)
    high_text = font.render(f"High Score : {high_score}/{len(bulb_states)}",True,WHITE)
    small_font = pygame.font.SysFont(None, 32)
    condition_text = small_font.render(current_condition, True, WHITE)
    if game_state == "win" and check_condition() and remaining > 0:
        win_text = font.render("🎉 YOU WIN! 🎉", True, (0, 255, 0))
        screen.blit(win_text, (250, 620))
    if game_state == "game" and remaining == 0:
        over_text = font.render("TIME UP!", True, (255, 0, 0))
        screen.blit(over_text, (300, 620)) 
    if game_state == "menu":      
        pygame.draw.rect(screen, (0,180,0), easy_button)
        pygame.draw.rect(screen, (255,165,0), medium_button)
        pygame.draw.rect(screen, (200,0,0), hard_button)
        easy_text = font.render("Easy", True, WHITE)
        medium_text = font.render("Medium", True, WHITE)
        hard_text = font.render("Hard", True, WHITE)
        screen.blit(easy_text, easy_text.get_rect(center=easy_button.center))
        screen.blit(medium_text, medium_text.get_rect(center=medium_button.center))
        screen.blit(hard_text, hard_text.get_rect(center=hard_button.center))
    level_text = font.render(f"Level : {difficulty}", True, WHITE)
    if game_started:
        screen.blit(score_text, (20, 90))
        screen.blit(high_text, (20,140))
        screen.blit(condition_text, (20, 220))
        screen.blit(timer_text, (700, 90))
    pygame.display.update()
pygame.quit()