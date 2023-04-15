import pygame
pygame.init()
from game import Game
import math
#definir une clock
clock=pygame.time.Clock()
FPS=120
# generer la fentre de notre jeux

pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080 ,720))
#importer de charger l'arrière plan du jeux
background=pygame.image.load('PygameAssets-main/bg.jpg')

#chrger notre banniere
banner=pygame.image.load('PygameAssets-main/banner.png')
banner=pygame.transform.scale(banner,(500,500))
banner_rect=banner.get_rect()
banner_rect.x=math.ceil(screen.get_width()/4)

#charger notre boutons pour lancer la partie
play_button=pygame.image.load('PygameAssets-main/button.png')
play_button=pygame.transform.scale(play_button,(400,150))
play_button_rect=play_button.get_rect()
play_button_rect.x=math.ceil(screen.get_width()/3.33)
play_button_rect.y=math.ceil(screen.get_height()/2)


#charger notre jeux
game = Game()
running = True

#boucle tant que  cette condition est vrai

while running:
    #apppliquer la fenetre  du jeux
    screen.blit(background, (0, -250))
    # vérifier si notre jeux a commencer ou nn
    if game.is_playing:
        #déclancher les instruction de la partie
        game.update(screen)
    #verifier si notre jeux n'a pas commencer
    else:
        #ajouter mon ecran de bienvenu
        screen.blit(play_button,play_button_rect    )
        screen.blit(banner,banner_rect)

    # metttee a jour ecran
    pygame.display.flip()
    # si le joeur ferme cette fenetre
    for event in pygame.event.get():
        # que l'évenement est une fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

            # detecter si un joeur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # detecter si la touche espace est enclancher pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.lunch_projectile()
                else:
                    # mettre le jeux en mode lancer
                    game.start()
                    # jouer le son
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeux en mode lancer
                game.start()
                # jouer le son
                game.sound_manager.play('click')    
    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)

#hello