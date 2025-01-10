# beginning
# g of quiz

good_points = 0
bad_points = 0

# middle

answer = input(" are you good A) good, or B) bad?\n")
if answer == "A":
    good_points += 1
elif answer == "B":
    bad_points += 1
answer = input(" do you like A) dogs, or B) cats?\n")
if answer == "A":
    good_points += 1
elif answer == "B":
    bad_points += 1



answer = input(" do you wear socks with sandals A) no, or B) yes?\n")
if answer == "A":
    good_points += 1
elif answer == "B":
    bad_points += 1
answer = input(" do you like the color dark red A) yes, or B) no?\n")
if answer == "A":
    good_points += 1
elif answer == "B":
    bad_points += 1
answer = input(" do you like dark green like forest green A) yes, or B) no?\n")
if answer == "A":
    good_points += 1
elif answer == "B":
    bad_points += 1
answer = input(" do you like peppermint A) yes, or B) no?\n")
if answer == "A":
    good_points += 1
elif answer == "B":
    bad_points += 1
answer = input(" do you kick puppies A) no, or B) yes?\n")
if answer == "A":
    good_points += 1
elif answer == "B":
    bad_points += 1

answer = input(" do you know that Honey is bee barf A) yes, or B) no?\n")
if answer == "A":
    good_points += 1
elif answer == "B":
    bad_points += 1

    answer = input(" do you find yourself acting like an animal? A) no what ew?, or B) yes all the time!\n")
if answer == "A":
    good_points += 1
elif answer == "B":
    bad_points += 1

answer = input(" do you find yourself wearing fluffy tails and cat ears A) no, or B) yesB?\n")
if answer == "A":
    good_points += 1
elif answer == "B":
    bad_points += 1

answer = input(" do you like cookies A) yup, or B) no?\n")
if answer == "A":
    good_points += 1
elif answer == "B":
    bad_points += 1

answer = input(" do you prefer to go without shoes? A) yup, or B) no?\n")
if answer == "A":
    good_points += 1
elif answer == "B":
    bad_points += 1

answer = input(" are you alergic to peanut butter A) no, or B) yes?\n")
if answer == "A":
    good_points += 1
elif answer == "B":
    bad_points += 100

# end

if good_points > bad_points:
    print("you are good")
elif bad_points > good_points:
    print("you are bad")
elif good_points == bad_points:
    print("i cant tell... go away")