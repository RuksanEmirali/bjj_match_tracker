import random 
intro = """
*********************************************************
BRAZILIAN JIU JITSU - MATCH TRACKER
*********************************************************
It's competition time! This match will be refereed ussing
IBJJF rules...

Submission - If a competitor holds a submission so that 
            their opponent taps, the competitor will 
            automatically win

Points - For each favourable position held for 3 seconds, 
        a competition will recieve a given number of points:
        Mount = 4 points 
        Guard pass = 3 points 
        Take down, sweep and knee on belly = 2 points
        - If time run out and neither competitor has been 
        submitted, the player with the most points will win

Penalty - On first offence, the offender will recieve a 
        verbal warning. 
        - On second offence, the opponent will recieve 
        an advantage
        - On third offence, the opponent will recieve 
        two points
        - After three offences, the offender will be 
        disqualified and their oppenent wins.

Advantage - If a commetitor attempts but does not fully 
        complete a move, they will recieve an advantage.
        - Advantages will be considered if time ends and
        there is a points tie. The commetitor with more 
        advantages will win
        - If there is a points and advantage tie, the 
        referee will decide the winner. 

*********************************************************
"""
stars = """
*********************************************************
"""
scores = {"points_1" : 0 , 
          "points_2" : 0 , 
          "adv_1" : 0 , 
          "adv_2" : 0 , 
          "sub_1" : 0 , 
          "sub_2" : 0 ,
          "pen_1" : 0 ,
          "pen_2" : 0}

print(intro)

competitor_1 = input("Competitor 1: ")
competitor_2 = input("Competitor 2: ")

points_pen_adv = """
Enter:
P for points
PEN for penalty
A for advantage 
S for submission
END if the time has ended
"""

pos_log = """
Enter move:
M for mount
G for guard pass 
T for take down
S for sweep 
K for knee on belly 
"""

which_comptitor = f"""
Select player:
1 for {competitor_1}
2 for {competitor_2} 
"""


while True:
    print(stars)
    print(f"""
The current scores are...
{competitor_1} : {scores["points_1"]}
{competitor_2} : {scores["points_2"]} 
""")
    category = input(points_pen_adv)
    if category.upper() == "END":
        break
    else:
        comp = input(which_comptitor)
        if category.upper() == "P":
            while True:
                position = input(pos_log)
                if position.upper() == "M":
                    if comp == "1":
                        scores["points_1"] += 4
                        break
                    elif comp == "2":
                        scores["points_2"] += 4
                        break
                elif position.upper() == "G":
                    if comp == "1":
                        scores["points_1"] += 3
                        break
                    elif comp == "2":
                        scores["points_2"] += 3
                        break
                elif position.upper() == "T" or "S" or "K":
                    if comp == "1":
                        scores["points_1"] += 2
                        break
                    elif comp == "2":
                        scores["points_2"] += 2
                        break
                    break
                else:
                    print("Invalid move, try again")
        elif category.upper() == "PEN":
            if comp == "1":
                    scores["pen_1"] += 1
                    scores["points_2"] += 1  
            elif comp == "2":
                    scores["pen_2"] += 1
                    scores["points_1"] += 1
            if scores["pen_1"] == 3 or scores["pen_2"] == 3:
                break
        elif category.upper() == "A":
            if comp == "1":
                scores["adv_1"] += 1
            elif comp == "1":
                scores["adv_2"] += 1
        elif category.upper() == "S":
            if comp == "1":
                scores["sub_1"] += 1
            elif comp == "1":
                scores["sub_2"] += 1
            break
        else:
            print("Invalid input, try again")


if scores["pen_1"] == 3:
    winner = competitor_2
    win_cat = "penalty"
elif scores["pen_2"] == 3:
    winner = competitor_2
    win_cat = "penalty"
elif scores["sub_1"] == 1 :
    winner = competitor_1
    win_cat = "submission"
elif scores["sub_2"] == 1 :
    winner = competitor_2
    win_cat = "submission"
elif scores["points_1"] > scores["points_2"] :
    winner = competitor_1
    win_cat = "points"
elif scores["points_2"] > scores["points_1"] :
    winner = competitor_2
    win_cat = "points"
elif scores["points_1"] == scores["points_2"] :
    if scores["adv_1"] > scores["adv_2"]:
        winner = competitor_1
        win_cat = "advantage"
    elif scores["adv_2"] > scores["adv_1"]:
        winner = competitor_2
        win_cat = "advantage"
    else:
        rand = random.randint(1,2)
        if rand == 1:
            winner = competitor_1
        else:
            winner = competitor_2
        win_cat = "referee decision"

print(stars*2)    
print(f"{winner} wins by {win_cat}!")
print(stars*2)
