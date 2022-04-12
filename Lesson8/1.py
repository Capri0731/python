from pycat.core import Window, Sprite, Color, Label
w=Window()
class Stsp(Sprite):
    def on_create(self):
        self.color=Color.RED
        self.scale=75
        self.x=450
        self.y=300
    def on_left_click(self):
        label.is_active=not label.is_active
class Reset(Sprite):
    def on_create(self):
        self.color=Color.GREEN
        self.scale=75
        self.x=600
        self.y=300
    def on_left_click(self):
        label.is_active=False
        label.time=0
        label.text=str(round((label.time), 2))
class Time(Label):
    def on_create(self):
        self.text="0"
        self.time=0
        self.is_active=True
    def on_update(self, dt: float):
        if self.is_active:
           self.text=str(round((self.time), 2))
           self.time+=dt
       
     

label=w.create_label(Time)
w.create_sprite(Stsp)  
w.create_sprite(Reset)        
w.run()