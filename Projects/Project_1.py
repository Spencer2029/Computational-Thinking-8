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

s1 = codesters.Sprite("mean girls", 55, 100)
s1.set_size(0.4)
s1 = codesters.Sprite("burn book", 150, 135)
s1.set_size(0.2)
s1 = codesters.Sprite("blue_hoodie-removebg-preview", 130, 50)
s1.set_size(0.5)
s2 = codesters.Sprite("Taylor swift", -140, -100)
s2.set_size(0.2)
s2 = codesters.Sprite("eras tour", -70, -135)
s2.set_size(0.3)
s3 = codesters.Sprite("little shop", 70, -100)
s3.set_size(0.3)
s3 = codesters.Sprite("Audrey_two", 130, -135)
s3.set_size(0.5)
s4 = codesters.Sprite("campus 00", -100, 100)
s4.set_size(0.2)
s4 = codesters.Sprite("samba", -140, 50)
s4.set_size(0.8)
s4 = codesters.Sprite("black_campus", -40, 140)
s4.set_size(0.4)

message1 = codesters.Text("Spencer",0,220,"Goldenrod")
message2 = codesters.Text(":)",0,-220,"Goldenrod")

