# section 1

import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()
player = codesters.Sprite("Lolaaa2",0,-180)
player.set_size(0.25)
stage.set_background("doghouse3")
object_speed = -5
bones = 2

# Section 2 - Objects

def falling_objects():
    global object_speed, bones
    if bones < 10:
        x = random.randint ( -250, 250 ) 
        object = codesters.Sprite("bone",0,600)
        object.set_size(.25)
        object.go_to(x,250)
        object.set_y_speed(object_speed)
stage.event_interval(falling_objects, 2)

# Section 3 - collision 

def collision(player, object):
    global bones 

    if object.get_image_name() == "bone":
        stage.remove_sprite(object)
        bones += 1
        if bones == 0:
            player.say("you have 0 bones", 5)
        else:
            player.say(f"{bones}",0.5)

player.event_collision(collision)

# Section 4 - controlls 

# Right Key
def go_right():
    player.move_right(10)

player.event_key("right", go_right)

# Left Key
def go_left():
    player.move_left(10)

player.event_key("left", go_left)