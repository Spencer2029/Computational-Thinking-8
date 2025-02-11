# section 1

import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()
player = codesters.Sprite("Lolaaa2")
player.set_size(0.25)
stage.set_background("doghouse3")
object_speed = -5
bones = 2

# Section 2 - Objects

def falling_objects():
    global object_speed, bones
    if bones < 10:
        x = random.randint ( -250, 250 ) 
        object = codesters.Sprite("bone",x,250)
        object.set_size(.25)
        object.set_y_speed(object_speed)
stage.event_interval(falling_objects, 2)
