from pycat.extensions import Turtle
from pycat.core import Window, Color
w=Window()
t=w.create_sprite(Turtle)

t.x=(w.width/2)
t.y=300


def draw(step, sides, colar):
    t.pen_color=colar
    for _ in range(sides):
        t.rotation+=360/sides
        t.move_forward(step)

for _ in range(36):
    draw(20, 36, Color(153, 153, 255))
    t.rotation+=15
    t.move_forward(10)

w.run()