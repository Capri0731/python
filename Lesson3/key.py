from random import randint
from pycat.core import Window, Sprite
from pycat.core import KeyCode

w=Window()
class Owl(Sprite):
    def on_create(self):
        self.image="images/owl.gif"
        self.x=0
        self.y=500
        
    def on_update(self,dt):
        self.set_random_color()
        if w.is_key_down(KeyCode.RIGHT):
           self.x +=1.7
        if w.is_key_pressed(KeyCode.BACKSPACE  ):
           self.x +=1.1 
        
        if self.x>=w.width:
           print("Owl is the winner")
           w.close()

class Fireball(Sprite):
    def on_create(self):
        self.image="images/fireball.gif"
        self.x=0
        self.y=200

    def on_update(self, dt):
        self.set_random_color()
        if w.is_key_down(KeyCode.SPACE):
           self.x+=3 
        if w.is_key_pressed(KeyCode._1):
           self.x+=1 
        
        if self.x>=w.width:
           print("Fireball is the winner")
           w.close()
    
w.create_sprite(Fireball)
w.create_sprite(Owl)

w.run()