from asyncio import shield
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
        if self.is_touching_any_sprite_with_tag("blue"):
            blue.x=560
        
class PlayerR(Sprite):
    def on_create(self):
        self.scale=0.11
        self.speed = 10
        self.x=1100
        self.y=320
        self.add_tag("red")
        self.image="images/PlayerRed.png"
        self.lives=151
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
        
        if self.lives<0:
            w.close()
            print("blue win~")
    def on_left_click_anywhere(self):
        bulletr=w.create_sprite(PlayerRbullet)
        bulletr.point_toward_mouse_cursor()
    
    
        
        
        
class PlayerRbullet(Sprite):
    def on_create(self):
        self.scale=7
        self.color=Color.RGB(randint(170,255), randint(0,255), randint(0,255))
        self.position=red.position
        self.add_tag("prb")
        
    def on_update(self, dt):
        self.move_forward(15)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag("twr"):
            self.delete()
            twr.lives-=2              
        if self.is_touching_any_sprite_with_tag("blue"):
            self.delete()
            blue.lives-=2
        
class Key(Sprite):
    def on_create(self):
        self.image="images/key.webp"
        self.x=1100
        self.y=550
        self.scale=0.1
        self.time=0
    def on_update(self, dt):
        self.time+=dt
        if w.is_key_down(KeyCode.ENTER):
            self.goto_random_position_in_region(min_x=700, min_y=0, max_x=1280, max_y=640)
        if self.time>6:
            self.is_visible=True
            self.time=0
        elif self.time>1:
            self.is_visible=False
        if self.is_touching_any_sprite_with_tag("blue"):
            w.close()
            print("blue win")
class PlayerB(Sprite):
    def on_create(self):
        self.scale=0.3
        self.speed = 5
        self.rotation_speed = 3.75
        self.x=200
        self.y=320
        self.lives=101
        self.time=0
        self.add_tag("blue")
        self.image="images/PlayerBlue.PNG"
        self.rotation_mode = RotationMode.ALL_AROUND
    def on_update(self, dt):
        self.time+=dt
        if w.is_key_pressed(KeyCode.W):
            self.move_forward(self.speed)
            # self.rotation=90
        if w.is_key_pressed(KeyCode.A):
            # self.move_forward(self.speed)
            # self.rotation=180
            self.rotation+=self.rotation_speed
        if w.is_key_pressed(KeyCode.S):
            self.move_forward(-self.speed)
            # self.rotation=-90
        if w.is_key_pressed(KeyCode.D):
            # self.move_forward(self.speed)
            # self.rotation=0
            self.rotation-=self.rotation_speed
        if w.is_key_pressed(KeyCode.SPACE):
            if self.time>0.1:
               bulletb=w.create_sprite(PlayerBbullet)
               bulletb.rotation=blue.rotation
               self.time=0
        
            
        if self.lives<0:
            w.close()
            print("red win")


class PlayerBbullet(Sprite):
    def on_create(self):
        self.scale=7
        self.color=Color.RGB(randint(0,255), randint(0,255), randint(110,255))
        self.position=blue.position
        self.add_tag("pbb")
    
    def on_update(self, dt):
        self.move_forward(15)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag("red"):
            self.delete()
            red.lives-=2
class Tower(Sprite):
    def on_create(self):
        self.image="images/Tower.png"
        self.scale=0.6
        self.x=175
        self.lives=301
        self.y=150
        self.add_tag("twr")
    def on_update(self, dt):
        
            
        if self.lives<=0:
            w.close()
            print("red win")
class Shield(Sprite):
    def on_create(self):
        self.is_visible=False
        self.image="images/Shield.png"
        self.goto(Tower)
        self.time=0
        self.able=True
    def on_update(self, dt):
        self.time+=dt
        if w.is_key_down(KeyCode.Q):
            self.is_visible=True
            if self.time>3:
                self.is_visible=False
                self.time=0
                self.able=False
        else:
            self.time=0



w.create_sprite(Line)
w.create_sprite(Key)
twr=w.create_sprite(Tower)
red=w.create_sprite(PlayerR)
blue=w.create_sprite(PlayerB)
w.run()