from time import sleep
from random import *
import pygame, sys
from pygame.locals import *
from pygame import mixer

pygame.init()

#definiowanie okna gry
width = 1280
height = 720
window = pygame.display.set_mode((width,height))
background_image = pygame.image.load("life_game/images/green_field_background.jpg")
background_image = pygame.transform.scale(background_image,(width,height))

mixer.init
mixer.music.load("life_game/sounds/tavern.mp3")
mixer.music.play()

#wyświetlanie okna gry
pygame.display.set_caption("Life game")


game = True
#main loop
while game:
    window.blit(background_image,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.display.update()
pygame.quit()    

# def get_font(size):

# def play():
#     pygame.display.set_caption("Play") #Ustawienie nagłówka

#     while True:

#         play_mouse_pos = pygame.mouse.get_pos()

#         window.fill("black")

#         play_text = get_font(45).render("This is the play screen.", True, "White")
#         play_rect = play_text.get_rect(center = (640, 260))
#         window.blit(play_text, play_rect)

#         play_back = Button(image = None, pos = (640,460),
#                             text_input= "BACK", font = get_font(75), base_color = "White", hovering_color = "Green")
#         play_back.changeColor(play_mouse_pos)
#         play_back.update(window)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if play_back.checkForInput(play_mouse_pos):
#                     main_menu()

#         pygame.display.update()
# def options():

# def main_menu():
#     pygame.display.set_caption("Menu")

#     while True:
#         window.blit(background_image,(width,height))

#         menu_mouse_pos = pygame.mouse.got_pos()

#         menu_text = get_font(100).render("MENU", True, "#b68f40")
#         menu_rect = menu_text.get_rect(center = (640, 100))

#         play_button = Button(image = pygame.image.load())

# main_menu()


    
    # print("===================================================== \n Witaj w grze biograficznej \n =====================================================")
    # choice = input("Press S to start the game \nPress H to view help \nPress Q to quit the game\n:").upper()
    # if (choice == "Q"):
    #     game = False
    # elif(choice == "H"):
    #     print("To jest gra na zasadach życia igora. Nic w tej grze nie jest spójne i logiczne :)")
    # elif(choice == "S"):
    #     print("Witaj w kreatorze swojego życia :D")
    #     sex = input("Wybierz płeć (M/K): ")
        
    #     def define_sex(km):
    #         if (sex == 'M' or sex == 'K'):
    #             return sex
    #         else:
    #             sex = input("Wybrana płeć nie istnieje! Podaj płeć jeszcze raz: ")
    #             return sex
    #     define_sex(sex)

    #     name = input("Podaj imię jakie chciałbyś nosić: ")
    #     eyes = input("Podaj jaki chcesz kolor oczu: ")
    #     hair = input("Podaj jaki chcesz kolor włosów: ")

    #     height_dad = input("Podaj wzrost taty: ")
    #     height_mom = input("Podaj wzrost mamy: ")

    #     def wzrost (height_d, height_m, s):
    #         if sex == 'M':
    #             kid_height = (height_dad + height_mom + 13) / 2
    #         elif sex == 'K':
    #             kid_height = (height_dad + height_mom - 13) / 2

    #         return kid_height

    #     wzrost(height_dad, height_mom, sex)
    #     country = input("Podaj kraj w którym chciałbyś się urodzić")
    #     iq = randint(10,200)
        
    #     print (f"Witaj {name}, twoje iq wynosi: {iq} ")
    #     game = False

