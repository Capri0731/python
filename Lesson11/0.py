from pycat.core import Window, Sprite, Color, Label
w=Window()
img=["img/3.jpg", "img/6.jpg", "img/4.jpg"]

class B1(Sprite):
    def on_create(self):
        self.scale=80
        self.color=Color.PURPLE
        self.x=200
        self.y=100
        
    def on_left_click(self):
        w.background_image=img[0]   
        itd.img_2="Busstop"
class B2(Sprite):
    def on_create(self):
        self.scale=80
        self.color=Color.RED
        self.x=600
        self.y=100
        
    def on_left_click(self):
        w.background_image=img[1]
        itd.img_2="Schoolstop"
class B3(Sprite):
    def on_create(self):
        self.scale=80
        self.color=Color.BLUE
        self.x=1000
        self.y=100
        
    def on_left_click(self):
        w.background_image=img[2]
        itd.img_2="Park"
class Itd(Label):
    def on_create(self):
        self.x=640
        self.y=600
        self.img_2=""
    def on_update(self, dt: float):
        self.text=":"+str(self.img_2)
itd=w.create_label(Itd)
w.create_sprite(B1)
w.create_sprite(B2)
w.create_sprite(B3)
w.run()