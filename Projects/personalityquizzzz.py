# begining of quiz

nice_points = 0
naughty_points = 0

# middle of quiz

answer = input(" are you nice A) nice, or B) naughty?\n")
if answer == "A":
    nice_points += 1
elif answer == "B":
    naughty_points += 1
answer = input(" do you like A) dogs, or B) cats?\n")
if answer == "A":
    nice_points += 1
elif answer == "B":
    naughty_points += 1



answer = input(" do you wear socks with sandals A) no, or B) yes?\n")
if answer == "A":
    nice_points += 1
elif answer == "B":
    naughty_points += 1
answer = input(" do you like the color dark red A) yes, or B) no?\n")
if answer == "A":
    nice_points += 1
elif answer == "B":
    naughty_points += 1
answer = input(" do you like dark green like forest green A) yes, or B) no?\n")
if answer == "A":
    nice_points += 1
elif answer == "B":
    naughty_points += 1
answer = input(" do you like peppermint A) yes, or B) no?\n")
if answer == "A":
    nice_points += 1
elif answer == "B":
    naughty_points += 1
answer = input(" do you kick puppies A) no, or B) yes?\n")
if answer == "A":
    nice_points += 1
elif answer == "B":
    naughty_points += 1

    answer = input(" do you find yourself acting like an animal? A) no what ew?, or B) yes all the time!\n")
if answer == "A":
    nice_points += 1
elif answer == "B":
    naughty_points += 1

answer = input(" do you like cookies A) yup, or B) no?\n")
if answer == "A":
    nice_points += 1
elif answer == "B":
    naughty_points += 1

# end of quiz

if nice_points > naughty_points:
    print("you are nice")
elif naughty_points > nice_points:
    print("you are naughty")
elif nice_points == naughty_points:
    print("i cant tell... go away")