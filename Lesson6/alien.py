from pycat.core import Window, Sprite, Scheduler,RotationMode,Player
from pycat.core import KeyCode
from random import randint
space_sound=Player("images/Space Ambience.wav")
hit_sound=Player("images/hit.wav")
die_sound=Player("images/die.wav")
score_sound=Player("images/point.wav")
w=Window(background_image="images/underwater_04.png")
class Ufo(Sprite):
     def on_create(self):
         space_sound.play()
         self.image="images/saucer.png"
         self.x=200
         self.y=560
         self.scale=0.2
         self.rotation_mode=RotationMode.RIGHT_LEFT
         self.score=0
     def on_update(self, dt):
         self.move_forward(20)
         if self.is_touching_window_edge():
             self.rotation+=180
class Alien(Sprite):
    def on_create(self):
        self.is_moving_up=False
        self.x=100
        self.y=50
        self.scale=0.5
        self.rotation_mode=RotationMode.RIGHT_LEFT
        i=str(randint(1,5))
        self.image="images/"+i+".png"
    def on_update(self, dt):
        
        
        if self.is_moving_up:
            self.y+=10
            self.scale*=0.99
            if self.is_touching_sprite(ufo):
                ufo.score+=1
                label.text="Your score is:"+str(ufo.score)
                self.delete()
                score_sound.play()
            if self.y>630:
                self.delete()
                die_sound.play()
                
        else:
            self.move_forward(15)
            if self.is_touching_window_edge():
                hit_sound.play()
                self.rotation+=180

        


    def on_left_click(self):
        self.is_moving_up=True
        

label=w.create_label()        
def creates():
    w.create_sprite(Alien)
Scheduler.update(creates , 1.5)

ufo=w.create_sprite(Ufo)
w.run()