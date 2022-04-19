from pycat.core import Window, Sprite
from random import randint
w=Window()
waiting=1
beating=2
throwing=3
class Ape(Sprite):
    def on_create(self):
        self.scale=3
        self.x=640
        self.y=300
        self.time=0
        self.state=1
        self.image="img/ape_waiting.png"
    def on_update(self, dt):
        self.time+=dt
        if self.state==1:
            if self.time>1:
                self.state=2
        elif self.state==2:
            self.image="img/ape_angry1.png"
            if self.time>0.1:
                self.state=3
        elif self.state==3:
            self.image="img/ape_angry2.png"
            if self.time>0.3:
                self.state=4
                self.time=0
        elif self.state==4:
            w.create_sprite(Barrel)
            self.state=1
        
    
    
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