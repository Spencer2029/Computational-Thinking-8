###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("Theatre 2")


q1 = codesters.Square(100, 100, 200, 'DeepPink')
q2 = codesters.Square(-100, 100, 200, 'Gainsboro')
q3 = codesters.Square(-100, -100, 200, 'LightCoral')
q4 = codesters.Square(100, -100, 200, 'DarkGreen')

s1 = codesters.Sprite("mean girls", 100, 100)
s1.set_size(0.5)
s2 = codesters.Sprite("Taylor swift", -100, -100)
s2.set_size(0.2)
s3 = codesters.Sprite("little shop", 100, -100)
s3.set_size(0.3)
s4 = codesters.Sprite("campus 00", -100, 100)
s4.set_size(0.2)

message1 = codesters.Text("Spencer",0,220,"Goldenrod")
message2 = codesters.Text(":)",0,-220,"Goldenrod")

