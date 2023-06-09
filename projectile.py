import pygame
#definir la classe qui va gerer le projectile de notre joeurs

class Projectile(pygame.sprite.Sprite):
    
    #definir le constructeur de cette classe 
    def __init__(self, player):
        super().__init__()
        self.velocity= 5
        self.player=player
        self.image=pygame.image.load('PygameAssets-main/projectile.png')
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect= self.image.get_rect()
        self.rect.x= player.rect.x + 120
        self.rect.y = player.rect.y +85
        self.origin_image=self.image
        self.angle=0
    def rotate(self):
        #tourner le projectile
        self.angle+=5
        self.image=pygame.transform.rotozoom(self.origin_image, self.angle, 1 )
        self.rect=self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)
    def move(self):
        self.rect.x+= self.velocity
        self.rotate()
        # verifier si le projectil entre en collision avec un monstre

        for monster in self.player.game.chek_collision(self, self.player.game.all_monsters):
            # supprimer le projectifl
            self.remove()
            #infliger des degats
            monster.damagee(self.player.attack)
        #verifier si le projectile n'est plus présent sur l'ecarn
        if self.rect.x> 1080:
            #supp le projectil (en dehors de l'ecran )
            self.remove()
            print("projectile supprimé")