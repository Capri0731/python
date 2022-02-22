from pycat.core import Window
window=Window()
animal=window.create_sprite()
animals=input("Please choose an animal.")
if animals=="elephant":
    animal.image="images/elephant.png"
if animals=="owl":
    animal.image="images/owl.gif"
if animals=="pig":
    animal.image="images/pig.png"
if animals=="rat":
    animal.image="images/rat.png"
if animals=="tiger":
    animal.image="images/tiger.png"
if animals=="rooster":
    animal.image="images/rooster.png"
sizes=input("How big do you want?(*)")
animal.scale=float(sizes)
msg=("I'm a(an)"+ animals+ ", my size is "+ str(animal.scale))
print(msg)
print(type(animal.image))
print(type(animal.rotation))
print(type(animal.x))
print(type(animal.is_visible))
animal.x=640
animal.y=320
window.run()