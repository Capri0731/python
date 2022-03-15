from pycat.core import Window, Sprite, Scheduler,RotationMode
from pycat.core import KeyCode
from random import randint

w=Window(background_image="images/images/forest_background.jpg")

class Player(Sprite):
      def on_create(self):
          self.y=60
          self.scale=0.8
          self.image="images/images/tiger.png"
          self.score=0
          self.rotation_mode=RotationMode.RIGHT_LEFT
      def on_update(self, dt):
          if w.is_key_pressed(KeyCode.RIGHT):
              self.x+=6
              self.rotation=360
          if w.is_key_pressed(KeyCode.LEFT):
              self.x-=6
              self.rotation=180
          if w.is_key_pressed(KeyCode.SPACE):
              self.x=randint(0,1280)


class Sharp(Sprite):
    def on_create(self):
        self.y=600
        self.scale=0.2
        self.x= randint(50,1200)
        self.image="images/img/gem_shiny05.png"
    def on_update(self, dt):
        self.y-= randint(1,30)
        if self.is_touching_sprite(player):
            self.delete()
            player.score+=1
            label.text="score:"+str(player.score)
        if self.is_touching_window_edge():
            self.delete()
class Poison(Sprite):
    def on_create(self):
        self.y=600
        self.scale=0.2
        self.x= randint(50,1200)
        self.image="images/img/gem_shiny03.png"
    def on_update(self, dt):
        self.y-= randint(-15,30)
        if self.is_touching_sprite(player):
            self.delete()
            player.score-=1
            label.text="score:"+str(player.score)
        if self.is_touching_window_edge():
            self.delete()
class Iron(Sprite):
    def on_create(self):
        self.y=600
        self.scale=0.2
        self.x= randint(50,1200)
        self.image="images/img/gem_shiny04.png"
    def on_update(self, dt):
        self.y -= randint(-15,30)
        self.rotation+=10
        if self.is_touching_sprite(player):
            self.delete()
            player.score+=randint(-10,10)
            label.text="score:"+str(player.score)
        if self.is_touching_window_edge():
            self.delete()
label=w.create_label()

player=w.create_sprite(Player)

def creates():
    w.create_sprite(Sharp)
def createp():
    w.create_sprite(Poison)
def createi():
    w.create_sprite(Iron)
Scheduler.update(creates , 0.3)
Scheduler.update(createp , 0.6)
Scheduler.update(createi , 1.0)  
w.run()