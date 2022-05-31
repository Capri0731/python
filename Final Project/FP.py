from pycat.core import Window, Sprite, KeyCode, Color, RotationMode
from random import randint
w=Window()
class Line(Sprite):
    def on_create(self):
        self.time=0
        self.x=w.width/2
        self.y=w.height/2
        self.scale=1.5
        self.image="images/blocking line.png"
    def on_update(self, dt):
        self.time+=dt
        if self.time>10:
            self.delete()
        if self.is_touching_any_sprite_with_tag("red"):
            red.x=700
        
class PlayerR(Sprite):
    def on_create(self):
        self.scale=0.12
        self.speed = 10
        self.x=1000
        self.y=320
        self.add_tag("red")
        self.image="images/PlayerRed.png"

    def on_update(self, dt):
        self.rotation_mode=self.rotation_mode=RotationMode.RIGHT_LEFT
        if w.is_key_pressed(KeyCode.UP):
            self.move_forward(self.speed)
            self.rotation=90
        if w.is_key_pressed(KeyCode.LEFT):
            self.move_forward(self.speed)
            self.rotation=180
        if w.is_key_pressed(KeyCode.DOWN):
            self.move_forward(self.speed)
            self.rotation=-90
        if w.is_key_pressed(KeyCode.RIGHT):
            self.move_forward(self.speed)
            self.rotation=0
    def on_left_click_anywhere(self):
        bullet=w.create_sprite(PlayerRbullet)
        bullet.point_toward_mouse_cursor()
    
        
        
        
class PlayerRbullet(Sprite):
    def on_create(self):
        self.scale=7
        self.color=Color.RGB(randint(0,255), randint(0,255), randint(0,255))
        self.position=red.position
        self.add_tag("prb")
    
    def on_update(self, dt):
        self.move_forward(15)
        if self.is_touching_window_edge():
            self.delete()
class Key(Sprite):
    def on_create(self):
        self.image="images/key.webp"
        self.x=1100
        self.y=550
        self.scale=0.1
    def on_update(self, dt):
        if w.is_key_down(KeyCode.ENTER):
            self.goto_random_position_in_region(min_x=700, min_y=0, max_x=1280, max_y=640)



w.create_sprite(Line)
w.create_sprite(Key)
red=w.create_sprite(PlayerR)
w.run()