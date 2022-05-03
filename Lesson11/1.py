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
        self.add_tag(next)
        self.index=0
    def on_left_click(self):
        self.index+=1
        if self.index==len(img):
           self.index=0
        
        w.background_image=img[self.index]

w.create_sprite(Next)
w.run()