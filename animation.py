import random

import pygame

#definir une classe qui va s'occuper des animation
class AnimateSprite(pygame.sprite.Sprite):
    #definir les chose  a faire a la création de l'entité
    def __init__(self, sprite_name,size=(200,200)):
        super().__init__()
        self.size=size
        self.image=pygame.image.load(f'PygameAssets-main/{ sprite_name}.png')
        self.image=pygame.transform.scale(self.image,size)
        self.current_image= 0 #commencer l'animation a l'image zero
        self.images =self.animations.get(sprite_name)
        self.animation=False

    #definir une methode pour démarer l'animation
    def start_animation(self):
        self.animation= True


    #definir une méthode pour animé le sprite
    def animate(self,loop=False):
        #verifier si l'animation est active
        if self.animation:
            #passer a l'image suivante
            self.current_image+=1
             # verifier si on a attein la fin de l'animation
            if self.current_image >=len(self.images):
                #remttre l'animation au départ
                self.current_image=0
                #vérifier si l'animation n'est pas en mode boucle
                if loop is False:
                    #désactivation de l'animation
                    self.animation=False
            #modifier l'image de l'animation précedent par la suivante
            self.image=self.images[self.current_image]
            self.image = pygame.transform.scale(self.image,self.size)

    #definir une fonction pour charger les images d'un  sprite
    def load_animation_images(sprite_name):
        # charger les 24image de ce sprite dans le dossier correspondant
        images=[]
        # recuperer le chemin du dossier pour ce sprite
        path=f"PygameAssets-main/{sprite_name}/{sprite_name}"
        # boucler sur chaque image de ce dossier pour ajouter a la liste
        for num in range(1,25):
            image_path=path + str(num) + '.png'
            images.append(pygame.image.load(image_path))
        #renvoyer le contenu de la liste d'images
        return images

    #definir un dictionnaire qui va contenir  les images charger de chaque sprite
    #mummy _> [.....mummy1.png, ....mummy2.png etc ]
    #mummy _> [.....mummy1.png, ....mummy2.png etc ]

    animations={
        'mummy': load_animation_images('mummy'),
        'player':load_animation_images('player'),
        'alien': load_animation_images('alien')
    }
