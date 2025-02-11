#section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("park")
s1 = codesters.Sprite ("cat2",0,-200)
s1.set_size(0.5)



# section 2: define controls 
def move_up (sprite):
    sprite.move_up(10)

def move_down(sprite):
    sprite.move_down(10)

def move_left(sprite):
    sprite.move_left(10)

def move_right(sprite):
    sprite.move_right(10)


# section 3: define hide and show
def hide (sprite):
    sprite.hide()


# section 4: bind controls to specific keys
s1.event_key("up", move_up)
s1.event_key ("down", move_down)
s1.event_key ("left", move_left)
s1.event_key ("right", move_right)

#section 5: reminder message
print("game has started. Open the screen using PORTS to play")