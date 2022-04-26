
from pycat.core import Window, Sprite, Scheduler, RotationMode, Label

from random import randint
w=Window()
score=0
class Wizard(Sprite):
    def on_create(self):
        self.scale=0.3
        self.image="img/wizard-a.png"
        self.x=640
        self.y=100
        self.wait()
    def wait(self):
        self.image="img/wizard-a.png"
        Scheduler.wait(1, self.raise_)
    def raise_(self):
        self.image="img/wizard-b.png"
        Scheduler.wait(0.15, self.put_down)
    def put_down(self):
        self.image="img/wizard-a.png"
        Scheduler.wait(0.15, self.raise_2)
    def raise_2(self):
        self.image="img/wizard-b.png"
        Scheduler.wait(0.15, self.put_down2)
    def put_down2(self):
        self.image="img/wizard-a.png"
        Scheduler.wait(0.15, self.attack)
    def attack(self):
        sn=w.create_sprite(Snow)
        self.wait()


class Snow(Sprite):
    def on_create(self):
        self.scale=0.1
        self.image="img/snowflake.png"
        self.x=640
        self.y=100
        self.point_toward_mouse_cursor()
        self.add_tag("snow")
    def on_update(self, dt):
        self.move_forward(w.height*dt)
        if self.is_touching_window_edge():
            self.delete()
        #if self.is_touching_any_sprite():
            self.delete()
class Dove(Sprite):
    def on_create(self):
        self.scale=0.3
        self.image="img/dove-a.png"
        self.x=randint(100, 1200)
        self.y=600
        self.rotation_mode=RotationMode.RIGHT_LEFT
        self.rotation=-90
        self.time=0

    def on_update(self, dt):
        self.time+=dt
        if self.time>=0.1:
            if self.image=="img/dove-b.png":
                self.time=0
                self.image="img/dove-a.png"
            elif self.image=="img/dove-a.png":
                self.time=0
                self.image="img/dove-b.png"
        
        self.move_forward(5)
        if self.is_touching_window_edge():
            self.delete() 
        elif self.is_touching_any_sprite_with_tag("snow"):
            score.change_score(-2)
            self.delete()
            
class Jellyfish(Sprite):
    def on_create(self):
        self.scale=0.3
        self.image="img/jellyfish-a.png"
        self.x=randint(100, 1200)
        self.y=600
        self.rotation_mode=RotationMode.RIGHT_LEFT
        self.rotation=-90
        self.time=0
    def on_update(self, dt):
        self.time+=dt
        if self.time>=0.1:
            if self.image=="img/jellyfish-a.png":
                self.time=0
                self.image="img/jellyfish-b.png"
            elif self.image=="img/jellyfish-b.png":
                self.time=0
                self.image="img/jellyfish-a.png"
        self.move_forward(randint(4,8))
        if self.is_touching_window_edge():
            self.delete() 
        elif self.is_touching_any_sprite_with_tag("snow"):
            score.change_score(+2)
            self.delete()

class Score(Label):
    def on_create(self):
        self.score=0
        self.text="score:"
    def change_score(self, v):
        self.score+=v
        self.text="score:"+str(self.score)
score=w.create_label(Score)
def creates():
    w.create_sprite(Dove)
Scheduler.update(creates , 1)
def create2():
    w.create_sprite(Jellyfish)
Scheduler.update(create2 , 1.5)
w.create_sprite(Wizard)
w.run()