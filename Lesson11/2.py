from pycat.core import Window, Sprite, Color
w=Window()
img=["img/3.jpg", "img/6.jpg", "img/4.jpg"]
w.background_image=img[0]

class Next(Sprite):
    def on_create(self):
        self.scale=80
        self.color=Color.GREEN
        self.x=1100
        self.y=100
        self.index=0
    def on_left_click(self):
        self.index+=1
        if self.index==len(img):
           self.index=0
        
        w.background_image=img[self.index]
class Back(Sprite):
    def on_create(self):
        self.scale=80
        self.color=Color.RED
        self.x=300
        self.y=100
        
    def on_left_click(self):
        next.index-=1
        if next.index<0:
           next.index=2
        
        w.background_image=img[next.index]

next = w.create_sprite(Next)
w.create_sprite(Back)
w.run()