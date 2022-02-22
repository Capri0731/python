from random import randint
from pycat.core import Window, Sprite
w=Window()
class Owl(Sprite):
    def on_create(self):
        self.image="images/owl.gif"
        self.name="Dr.Owl"
        self.goto_random_position()
        self.set_random_color()
        self.layer=randint(0,2)

class Fireball(Sprite):
    def on_create(self):
        self.image="images/fireball.gif"
        self.goto_random_position()
        self.set_random_color
    
for i in range(100):
    w.create_sprite(Owl)
    
for i in range(500):
    w.create_sprite(Fireball)

w.run()