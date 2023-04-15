import pygame
import random
import animation


# crer une classe qui va gerer la notion de monstre dans notre jeux
class Monster(animation.AnimateSprite):
    def __init__(self, game, name,size,offset=0):
        super().__init__(name,size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 490-offset
        self.velocity = random.randint(1, 3)
        self.start_animation()
        self.loot_amount=10

    def set_speed(self,speed):
        self.default_speed=speed
        self.velocity = random.randint(1,3)

    def set_loot_amount(self,amount):
        self.loot_amount=amount

    def damagee(self, amount):
        # infliger les dégats
        self.health -= amount

        # érifier si son nouveau nombre de point de vie est inférieur ou égale a zero
        if self.health <= 0:
            # réaparaitre comme un new monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, self.default_speed)
            # ajouter le nombre de points
            self.game.score+=self.loot_amount
            # SI LA BARRE D'evenement est charger à son maximuù
            if self.game.comet_event.is_full_loaded():
                # retirer du jeux
                self.game.all_monsters.remove(self)
                # appel de la méthode pour essayer de déclancher la pluie de comete
                self.game.comet_event.attempt_fall()


    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # definir une couleur pour notre bare de vie (vert claire )
        bar_color = (111, 210, 46)
        # Définir une couleur pour l'arrière plan de la jauge (gris foncé)
        back_bar_color = (60, 63, 60)
        # définir la position de l'arrière plan de notre jauge de vie
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        # DEFINIR LA POSITION DE NOTRE JAUGE DE VIE AINSI KE SA LARGEUR ET SON EPAISSEUR
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 6]
        # dessioner nptre barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):
        # le deplacement ne se fait que si il n'y a pas de collision avec un groupe joueur
        if not self.game.chek_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collig=ssion avec le joeur
        else:
            # ingliger des dégarq
            self.game.player.damage(self.attack)


# definir une class pour la mummy
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy",(130,130))
        self.set_speed(1)
        self.set_loot_amount(20)

#definir une class pour l'alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien",(300,300),offset=130)
        self.health=250
        self.max_health=250
        self.attack=0.8
        self.set_speed(2)
        self.set_loot_amount(80)
