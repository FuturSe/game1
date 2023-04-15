import pygame
from  projectile import Projectile
import animation
#crée une première classe qui va représenter le jour
class Player(animation.AnimateSprite):
    def __init__(self,game):
        super(). __init__('player')
        self.game=game
        self.health = 100
        self.max_health = 100
        self.attack = 50
        self.velocity = 5
        self.all_projectiles=pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 450
    def update_animation(self):
        self.animate()
    def damage(self , amount):
        if self.health- amount > amount:
            self.health-= amount
        else:
            #si le joeur n'a plus de point de vie
            self.game.game_over()

    def update_health_bar(self,surface):
        #definir une couleur pour notre bare de vie (vert claire )
        bar_color=(111,210,46)
        #Définir une couleur pour l'arrière plan de la jauge (gris foncé)
        back_bar_color=(60,63,60)
        #définir la position de l'arrière plan de notre jauge de vie
        back_bar_position=[self.rect.x+50, self.rect.y+20, self.max_health, 5]


    #DEFINIR LA POSITION DE NOTRE JAUGE DE VIE AINSI KE SA LARGEUR ET SON EPAISSEUR
        bar_position=[self.rect.x+50, self.rect.y+20, self.health, 6]
        # dessioner nptre barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def lunch_projectile(self):
        #crer une nouvelle instance de la class Projectile
        self.all_projectiles.add(Projectile(self))
        #demarer l'animation du lancer
        self.start_animation()
        #jouer le son
        self.game.sound_manager.play('tir')


    def move_right(self):

        #si le joeur n'est pas en collision avec un monstre
        if not self.game.chek_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity