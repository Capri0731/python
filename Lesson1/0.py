from pycat.core import Window
window=Window()
owl=window.create_sprite()
owl.image="images/owl.png"
owl.x=640
owl.y=320
mouse=window.create_sprite()
mouse.image="images/rat.png"
mouse.x=300
mouse.y=240
height=input ("How tall are you?(cm)")
print ("I,m", height, "cm high." )


window.run()

