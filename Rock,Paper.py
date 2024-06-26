import random

def pc_selection():
    a = random.randint(1,3)
    if a == 1:
        return "Rock"
    elif a == 2:
        return "Paper"
    else:
        return "Scissors"
score_user = 0
score_pc = 0
while True:

    user_selection = input("Rock? Paper? Scissors:")
    pcselect = pc_selection()
    print("Computer:",pcselect)


    if pcselect == user_selection:
        print("Draw")
    elif pcselect =="Rock" and user_selection == "Paper":
        score_user +=1
    elif pcselect =="Paper" and user_selection == "Scissors":
        score_user +=1
    elif pcselect =="Scissors" and user_selection == "Rock":
        score_user +=1
    else:
        score_pc += 1

    print("You:", score_user, "VS Pc:", score_pc)

    if score_user == 3 or score_pc == 3:
        break

if score_pc > score_user:
    print("You lost!")
else:
    print("You won")
