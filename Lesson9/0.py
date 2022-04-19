from pycat.core import Window, Sprite, Scheduler
from random import randint
w=Window()
class Ape(Sprite):
    def on_create(self):
        self.scale=3
        self.x=640
        self.y=300
        self.wait()
    def wait(self):
        self.image="img/ape_waiting.png"
        Scheduler.wait(1, self.beating)
    def beating(self):
        self.image="img/ape_angry1.png"
        Scheduler.wait(1, self.throw) 
    def throw(self):
        w.create_sprite(Barrel)
        self.wait()
class Barrel(Sprite):
    def on_create(self):
        self.x=ape.x
        self.y=ape.y
        self.image="img/barrel1.png"
        self.scale=3
        self.rotation=randint(0,150)
    def on_update(self, dt):
        
        self.move_forward(w.height*dt)
        if self.is_touching_window_edge():
            self.delete()



ape=w.create_sprite(Ape)

w.run()