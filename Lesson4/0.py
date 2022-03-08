
from pycat.core import Window, Sprite
from random import randint, random
from pycat.core import KeyCode, RotationMode

w=Window()
class Owl(Sprite):
    def on_create(self):
        self.image="images/owl.gif"
        self.x=600
        self.y=300
        self.scale=0.45
        self.add_tag("owl")
        self.rotation_mode=RotationMode.RIGHT_LEFT
    def on_update(self, dt):
        self.move_forward(5.5)
        if w.is_key_down(KeyCode.DOWN):
            self.rotation=-90
        if w.is_key_down(KeyCode.RIGHT):
            self.rotation=0
        if w.is_key_down(KeyCode.UP):
            self.rotation=90
        if w.is_key_down(KeyCode.LEFT):
            self.rotation=180
        

class Fireball(Sprite):
     def on_create(self):
         self.image="images/fireball.gif"
         self.x=500
         self.y=100
         self.scale=1.2
         self.add_tag("fire")
     def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("owl"):
            print("You lose!")
            w.close()
        self.x+= randint(-15,20)
        self.y+= randint(-20,25)
class Rat(Sprite):
     def on_create(self):
         self.image="images/rat.png"
         self.x=800
         self.y=550
         self.scale=0.3
         self.add_tag("rat")
     def on_update(self, dt):
         if self.is_touching_any_sprite_with_tag("owl"):
             print("You win!")
             w.close()
         self.x+= randint(-15,10)
         self.y+= randint(-15,10)


w.create_sprite(Owl)
for i in range(2):
    w.create_sprite(Fireball)
w.create_sprite(Rat)
w.run()