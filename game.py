from player import Player
from monster import Monster, Mummy, Alien
import pygame
from player import Player
from comet_event import  CometFallEvent
from sound import soundManager


#creer une seconde classe qui va représenter notre jeux
class Game:
    def __init__(self):
        #definir si notre jeux a commencer ou nn
        self.is_playing= False
        # generer  notre joeur
        self.all_players= pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenement de cette plui de comete
        self.comet_event=CometFallEvent(self)
        #groupe de monstre
        self.all_monsters=pygame.sprite.Group()
         #gerer le son
        self.sound_manager=soundManager()
        #mettre le  scor a zéro
        self.score=0
        self.pressed = {}

    def start(self):
        self.is_playing=True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):
        #remettre le jeux a neuf ( retirer les monstres remettre le joeur a cent de vie et le jeux en attente)
        self.all_monsters= pygame.sprite.Group()
        self.comet_event.all_comets= pygame.sprite.Group()
        self.player.health= self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing=False
        self.score=0
        #jouer le son
        self.sound_manager.play('game_over')

    def update(self,screen):

        #afficher le scor sur l'ecran
        font=pygame.font.SysFont("monospace",16)
        score_text=font.render(f"score: {self.score}",1 ,(0,0,0))
        screen.blit(score_text,(20,20))
        # appliquer l'image de mon joeur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la bare de vie du joeur
        self.player.update_health_bar(screen)
        #actualiser l'animation du joueur
        self.player.update_animation()
        #actualiser la barre d'évenement du jeux
        self.comet_event.update_bar(screen)


        # recuperer les  projectiles du joeur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperons les monstre de notre jeux
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation

        #recuperer les cometes de notre jeux
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'sensemble des images de mon groupe de projectils
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)

        #appliquer l'ensemble des image de mon groupe de cometes
        self.comet_event.all_comets.draw(screen)
        # verifier si le joeur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()



    def chek_collision(self, sprite,group):
        return  pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self,monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

