from random import randint
from pycat.core import Window, Sprite

w=Window()
class Owl(Sprite):
    def on_create(self):
        self.image="images/owl.gif"
        self.x=0
        self.y=500
        
    def on_update(self,dt):
        self.x +=3
        self.scale+=0.002
        
        if self.x>=w.width:
           print("Owl is the winner")
           w.close()

class Fireball(Sprite):
    def on_create(self):
        self.image="images/fireball.gif"
        self.x=0
        self.y=200

    def on_update(self, dt):
        self.x +=4
        self.scale +=0.001
        if self.x>=w.width:
           print("Fireball is the winner")
           w.close()
    
w.create_sprite(Fireball)
w.create_sprite(Owl)

w.run()