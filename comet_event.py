import pygame
from  comet import  Comet

#crée une classse pour gérer cet evenement
class CometFallEvent:
    # lors du chargement -> crée un compteur
    def __init__(self,game):
      self.percent=0
      self.percent_speed=5
      self.game=game
      self.fall_mode=False
      # definir un groupe de sprite pour stocker nos cometes
      self.all_comets=pygame.sprite.Group()

    def add_percent(self):
        self.percent+=self.percent_speed/100
    def is_full_loaded(self):
        return self.percent >=100
    def reset_percent(self):
        self.percent = 0
    def meteor_fall(self):
        #boucle  pour les valeur entre un et dix
        for i in range(1,5):
            #appaitre une premiere boule de feux
            self.all_comets.add(Comet(self))
        #apparaitre 1 premiere boule de feux
        self.all_comets.add(Comet(self))
    def attempt_fall(self):
        #la jauge d'évenement est totalement charger
        if self.is_full_loaded() and len(self.game.all_monsters)==0:
            print("pluie de cometes!")
            self.meteor_fall()

            self.fall_mode=True #activer l'évenement du cycle monstre/boule de feux


    def update_bar(self, surface):

        #ajouter du pourcentage a la bar
        self.add_percent()

        #bare noir en arrière plan
        pygame.draw.rect(surface,(0,0,0),[
            0, #axe des x
            surface.get_height()-20,# exe des y
            surface.get_width(), #longueur de la fenetre
            10, # epaisseur de la barre
        ])
        #bare rouge (jauge d'event)

        pygame.draw.rect(surface, (187,11,11), [
            0,  # axe des x
            surface.get_height() -20,  # exe des y
            (surface.get_width()/100)*self.percent,  # longueur de la fenetre
            10,  # epaisseur de la barre
        ])