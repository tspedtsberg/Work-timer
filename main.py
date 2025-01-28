import pygame
import sys
from constants import *
from Button import Button
from rewards import *

def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    CLOCK = pygame.time.Clock()
    pygame.display.set_caption("Work timer")

    background = pygame.image.load("assets/3headeddrag.jpg")
    Red_circle = pygame.image.load("assets/backdrop.png")
    white_button = pygame.image.load("assets/button.png")
    

    Start_stop_button = Button(white_button, (SCREEN_WIDTH/4), ((SCREEN_HEIGHT/5)*4), (SCREEN_WIDTH/3), (SCREEN_HEIGHT/5), "#c97676", "#9ab034", "START", pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20))
    reset_stop_button = Button(white_button, (SCREEN_WIDTH/4+2*(SCREEN_WIDTH/4)), ((SCREEN_HEIGHT/5)*4), (SCREEN_WIDTH/3), (SCREEN_HEIGHT/5), "#c97676", "#9ab034", "RESET", pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20))
    
    FONT = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 120)
    FONT_work_counter = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 30)
    FONT_status_text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 30)
    status_text = FONT_status_text.render("Work, work, work", True, "white")

    


    Worktimer_length = 1800 #30min
    short_break_length = 300 #5min
    long_break_length = 900 #15min

    current_seconds = Worktimer_length
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    started = False
    on_break = False
    work_counter = 0



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Start_stop_button.check_for_input(pygame.mouse.get_pos()):
                    if started:
                        started = False
                    else:
                        started = True
                if started:
                    Start_stop_button.text_input = "STOP"
                    Start_stop_button.text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 30).render(
                                            Start_stop_button.text_input, True, Start_stop_button.base_color)
                    status_text = FONT_status_text.render("work work work", True, "white")
                else:
                    Start_stop_button.text_input = "START"
                    Start_stop_button.text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 30).render(
                                            Start_stop_button.text_input, True, Start_stop_button.base_color)
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_stop_button.check_for_input(pygame.mouse.get_pos()):
                    if started:
                        current_seconds = Worktimer_length
                        started = False
                        Start_stop_button.text_input = "START"
                        Start_stop_button.text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 30).render(Start_stop_button.text_input, True, Start_stop_button.base_color)
                    else:
                        current_seconds = Worktimer_length
            
            if event.type == pygame.USEREVENT and started == True:
                current_seconds -= 1

            if current_seconds == 0:
                if on_break == False:
                    if (work_counter+1) % 4 == 0:
                        current_seconds = long_break_length
                        on_break = True
                        status_text = FONT_status_text.render("looong as break", True, "white")
                        work_counter += 1
                    elif (work_counter+1) % 4 != 0:
                        current_seconds = short_break_length
                        on_break = True
                        status_text = FONT_status_text.render(f"{short_break_tasks()}", True, "white")
                        work_counter += 1
                else:
                    current_seconds = Worktimer_length
                    started = False
                    on_break = False
                    status_text = FONT_status_text.render("Back to work", True, "white")
                    Start_stop_button.text_input = "START"
                    Start_stop_button.text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 30).render(Start_stop_button.text_input, True, Start_stop_button.base_color)
                

        
        SCREEN.fill("#ba4949")
        #SCREEN.blit(background, background.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))
        
        
        if current_seconds >= 0:
            display_seconds = int(current_seconds % 60)
            display_minuttes = int(current_seconds / 60) % 60
            
        
        timer_text = FONT.render(f"{display_minuttes:02}:{display_seconds:02}", True, "white")
        work_text = FONT_work_counter.render(f"Daily streak: {work_counter}", True, "white")
        curently_text = FONT_status_text.render(f"Currently doing:", True, "white")
        SCREEN.blit(timer_text, timer_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))
        SCREEN.blit(status_text, status_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 120)))
        SCREEN.blit(work_text, work_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 200)))
        SCREEN.blit(curently_text, curently_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 150)))
        Start_stop_button.update(SCREEN)
        Start_stop_button.change_color(pygame.mouse.get_pos())
        reset_stop_button.update(SCREEN)
        reset_stop_button.change_color(pygame.mouse.get_pos())

        pygame.display.update()

        CLOCK.tick(60) # limit to 60 fps




if __name__ == "__main__":
    main()
'''
To do's:

Sounds

Add user inputs to short break and long break tasks
store the tasks in a separate file
read from the file

'''
