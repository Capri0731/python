from pycat.core import Window, Sprite, Color
from random import randint
w=Window()
class Firework(Sprite):
    
            
    def on_create(self):
        self.scale=10
        self.rotation=randint(75,105)
        
        self.position=w.mouse_position
        self.timer=0
    def on_update(self, dt):
        self.timer+=dt
        if self.timer>2:
            pass
        elif self.timer>0.5:
            self.move_forward(5)
        
        self.y-=2

class Explode(Sprite):
    def on_left_click_anywhere(self):
        for _ in range(5):
            
            w.create_sprite(Firework)
      

        

w.create_sprite(Explode)
w.run()