import pygame
import random

#ccrer ue=ne classe pour gerer la comete

class Comet(pygame.sprite.Sprite):
    def __init__(self,comet_event):
        super().__init__()
        #definir l'image de la comete
        self.image=pygame.image.load('PygameAssets-main/comet.png')
        self.rect= self.image.get_rect()
        self.velocity=random.randint(1,4)
        self.rect.x=random.randint(20,800)
        self.rect.y=- random.randint(0,800)
        self.comet_event=comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        #jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        # verifier si le nombre de comete est de zero
        if len(self.comet_event.all_comets) == 0:
            print('evenement fini ')
            #remtre la barre a zero
            self.comet_event.reset_percent()
            # apparaitre a nouveau les deux premier monstre
            self.comet_event.game.start()


    def fall(self):
        self.rect.y+= self.velocity

    # ne tombe pas sur le sol
        if self.rect.y>=500:
            print('sol')
            # retirer la boule de feux
            self.remove()

            #si il n'y a plus de boule de feux
            if len(self.comet_event.all_comets)==0:
                print('evenement fini ')
                # remettre la jauge au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode=False

        #verifier si la boule de feux touche le joeur
        if self.comet_event.game.chek_collision(
                self, self.comet_event.game.all_players):
            print('joeur touché')
            #retirer la boule de feu
            self.remove()
            #subir 20point de déguat
            self.comet_event.game.player.damage(20)