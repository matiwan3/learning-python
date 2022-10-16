import time
from random import *
import pygame, sys
from pygame.locals import *
from pygame import mixer
import os

pygame.font.init()
pygame.mixer.init()

WHITE = (255,255,255)
WIDTH, HEIGHT = 800, 533

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
START_FONT = pygame.font.SysFont('04b', 100)
CHAR_WIDTH, CHAR_HEIGHT = 55, 150

pygame.display.set_caption("Przygody mateusza")
BACKGROUND_IMAGE = pygame.image.load("images/background2.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE,(WIDTH,HEIGHT))


MALE_CHARACTER_IMAGE = pygame.image.load(os.path.join("images\mati_character.png"))
MALE_CHARACTER = pygame.transform.scale(MALE_CHARACTER_IMAGE,(CHAR_WIDTH, CHAR_HEIGHT))

FEMALE_CHARACTER_IMAGE = pygame.image.load(os.path.join("images\ola_character.png"))
FEMALE_CHARACTER = pygame.transform.scale(FEMALE_CHARACTER_IMAGE,(CHAR_WIDTH, CHAR_HEIGHT))

FPS = 60
VEL = 1

mixer.music.load("sounds/pixelbit.mp3")
mixer.music.play(loops=-1)

def draw_window(type_of_char,char):
    WIN.blit(BACKGROUND,(0,0))
    WIN.blit(type_of_char, (char.x,char.y))
    pygame.display.update()
    
def char_movement(keys_pressed,char):
    if keys_pressed[pygame.K_a]: #left
        char.x -= VEL
    if keys_pressed[pygame.K_d]: #left
        char.x += VEL
    if keys_pressed[pygame.K_w]: #left
        char.y += VEL
        time.sleep(1)
        char.y -= VEL
def choose_char():
    choosing = True
    while choosing:
        character_choice = input("Male/Female: ")
        if character_choice == "Male":
            type_of_char = MALE_CHARACTER
            choosing = False

        elif character_choice == "Female":
            type_of_char = FEMALE_CHARACTER
            choosing = False

        else:
            print("Wrong choice.\n")
    return type_of_char

def START_SCREEN(text):
    draw_text = START_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
    
#main loop
def main():
    type_of_char = choose_char()
    # print(type_of_char)
            
    clock = pygame.time.Clock()
    clock.tick(FPS)
    run = True
    character = pygame.Rect(0, 300, CHAR_WIDTH,CHAR_HEIGHT)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        # Char_type = START_SCREEN("Wybierz postać")
        keys_pressed = pygame.key.get_pressed()
        char_movement(keys_pressed,character)
        draw_window(type_of_char,character)
if __name__ =="__main__":
    main()
    