from pycat.core import Window, Sprite, Color
from random import randint
w=Window()
class Particle(Sprite):
    def on_create(self):
        self.rotation=randint(0,360)
        self.add_tag('particle')
        self.scale=10
        self.goto_random_position()
    def on_update(self, dt):
        self.rotation=randint(0,360)
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.delete()
class Button(Sprite):
    def on_create(self):
        self.x=300
        self.y=450
        self.scale=100
    def on_left_click(self):
        p_list=w.get_sprites_with_tag('particle')
        for p in p_list:
            p.color=Color(randint(0,255),randint(0,255),randint(0,255))

for _ in range(100):
    w.create_sprite(Particle)
w.create_sprite(Button)
w.run()