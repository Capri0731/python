from pycat.core import Color, Sprite, Window, KeyCode, Scheduler
from random import randint
window = Window()


class Player(Sprite):

    def on_create(self):
        self.color = Color.AMBER
        self.scale = 30
        self.speed = 10

    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.W):
            self.move_forward(self.speed)
            self.rotation=90
        if window.is_key_pressed(KeyCode.A):
            self.move_forward(self.speed)
            self.rotation=180
        if window.is_key_pressed(KeyCode.S):
            self.move_forward(self.speed)
            self.rotation=-90
        if window.is_key_pressed(KeyCode.D):
            self.move_forward(self.speed)
            self.rotation=0
    def on_left_click_anywhere(self):
        
        
        bullet=window.create_sprite(Playerbullet)
        bullet.point_toward_mouse_cursor()

        
        
class Playerbullet(Sprite):
    def on_create(self):
        self.scale=7
        self.color=Color.VIOLET
        self.position=player.position
        self.add_tag("pb")
    
    def on_update(self, dt):
        self.move_forward(15)
        if self.is_touching_window_edge():
            self.delete()
class Enemy(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.rotation=randint(0,360)
        self.scale=30
        self.color=Color.RED
        self.time=0
        self.shoottime=0.2
    def on_update(self, dt):
        self.time+=dt
        if self.time>self.shoottime:
            self.time=0
            bullet=window.create_sprite(Enemybullet)
            bullet.position=self.position
            bullet.point_toward_sprite(player)
        self.move_forward(7.5)
        if self.is_touching_window_edge():
            self.delete()
        self.point_toward_sprite(player)
        if self.is_touching_any_sprite_with_tag("pb"):
            self.delete()
class Enemybullet(Sprite):
    def on_create(self):
        self.scale=7
        self.color=Color.RGB(randint(0,255), randint(0,255), randint(130,255))
    def on_update(self, dt):
        self.move_forward(15)

def spawn_enemies():
    window.create_sprite(Enemy)


Scheduler.update(spawn_enemies, 2.3)

player = window.create_sprite(Player)
window.run()