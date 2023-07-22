from ui import main_menu
import pygame

def main(window=None):
    pygame.font.init()  # <---- add this line
    s_width = 800
    s_height = 750
    if not window:
        window = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Tetris')
    main_menu(window)

if __name__ == "__main__":
    main()

