from pycat.core import Window, Sprite
from random import randint
w=Window()
class Particle(Sprite):
    def on_create(self):
        self.rotation=randint(0,360)
        self.scale=10
        self.goto_random_position()
    def on_update(self, dt):
        #self.rotation=randint(0,360)
        self.move_forward(10)
        if self.is_touching_window_edge():
            #self.delete()
            if self.rotation>360:
                self.rotation=360-self.rotation
            else:
                self.rotation=180-self.rotation

            
for _ in range(100):
    w.create_sprite(Particle)
w.run()