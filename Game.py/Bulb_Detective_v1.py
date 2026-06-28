import pygame
pygame.init()
import time
font = pygame.font.SysFont(None, 40)
WIDTH = 900
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bulb Detective 💡")
bulb_on = pygame.image.load("bulb.webp")
bulb_off = pygame.image.load("bulb_off.png")
bulb_on = pygame.transform.scale(bulb, (60, 60))
bulb_off = pygame.transform.scale(bulb_off, (60, 60))
BACKGROUND = (25, 25, 25)
YELLOW = (255, 255, 0)
bulb_positions = [
    (200, 200),
    (350, 200),
    (500, 200),
    (650, 200),

    (200, 350),
    (350, 350),
    (500, 350),
    (650, 350)
]
bulb_states = [True]*8
high_score = 0
restart_button = pygame.Rect(700, 20,150, 50)
start_button = pygame.Rect(350, 20, 150, 50)
start_time = time.time()
time_limit = 30
high_score = 0
game_started = False
running = True
while running:
    elapsed = int(time.time() - start_time)
    remaining = time_limit - elapsed
    if remaining < 0:
        remaining = 0 
    if remaining == 0:
        game_over = font.render("Time Over!", True, (255, 0, 0))
        screen.blit(game_over, (450, 100))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if start_button.collidepoint(mouse_x, mouse_y):
                game_started = True
            if restart_button.collidepoint(mouse_x, mouse_y):
                bulb_states = [True] * 8
            if game_started:
                for i, position in enumerate(bulb_positions):
                    x, y = position
                    distance = ((mouse_x - x)**2 + (mouse_y - y)**2)**0.5
                    if distance < 40:
                        bulb_states[i] = not bulb_states[i]
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, (0, 180, 0), start_button)
    start_text = font.render("start", True, (255, 255, 255))
    screen.blit(start_text, (390, 30))
    for i, position in enumerate(bulb_positions):
        x, y = position
        if bulb_states[i]:

            screen.blit(bulb_on,(x-30, y-30))
        else:
            screen.blit(bulb_off,(x-30, y-30))      
    score = bulb_states.count(False)
    if score == 8:
        perfect = font.render("Perfect!", True, (0, 255, 0))
        screen.blit(perfect, (450, 120))
    if score > high_score:
        high_score = score
    score_text = font.render(f"Score: {score}/8", True, (255, 255, 255))
    high_text = font.render(f"High Score: {high_score}/8", True, (0, 255, 255))
    screen.blit(high_text, (100, 100))
    screen.blit(score_text, (20, 20))
    if score == 8:
        win_text = font.render("You Win!", True, (0, 255, 0))
        screen.blit(win_text, (410, 90))
    pygame.draw.rect(screen, (0,180,0), restart_button)
    restart_text = font.render("Restart", True, (255,255,255))
    screen.blit(restart_text, (730,30))
    timer_text = font.render(f"Time: {remaining}", True, (255, 255, 255))
    screen.blit(timer_text, (700, 100))
    if remaining == 0:
        over_text = font.render("Time Up!", True, (255, 0, 0))
        screen.blit(over_text, (350, 120))
    pygame.display.update()
pygame.quit()