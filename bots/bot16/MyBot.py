
# keep these three import statements
import game_API
import fileinput
import json


# your import statements here
import random

first_line = True # DO NOT REMOVE

# global variables or other functions can go here
stances = ["Rock", "Paper", "Scissors"]

def get_winning_stance(stance):
    if stance == "Rock":
        return "Paper"
    elif stance == "Paper":
        return "Scissors"
    elif stance == "Scissors":
        return "Rock"

def priority(monster):
    pos = a * monster.death_effects.health + b * monster.death_effects.speed + c * monster.death_effects.rock + d * monster.death_effects.paper + e * monster.death_effects.scissors
    neg = f * moves_to_get_there(monster) + g * moves_to_beat_monster(monster) + h * get_health_damage(monster)
    return pos - neg # formula

def moves_to_get_there(monster):
    path = game.shortest_paths(me.location, monster.location)
    moves = (7 - me.speed) * len(path[0])
    if monster.dead == False:
        return moves
    return monster.respawn_counter if monster.respawn_counter > moves else moves

def moves_to_beat_monster(monster):
    chosen_stance = get_winning_stance(monster.stance)
    if chosen_stance == "Paper":
        stat = me.paper 
    elif chosen_stance == "Scissors":
        stat = me.scissors
    elif chosen_stance == "Rock":
        stat = me.rock

    return monster.health / stat

def get_health_damage(monster):
    return moves_to_beat_monster(monster) * monster.attack
def monster_array():
    monsternodes = []
    for node in range(0,25):
        if has_monster(node):
            monsternodes.append(node)
    for mnode in monsternodes:
        specificmonster = get_monster(mnode)
        dist = len(shortest_paths(me.location, mnode)[0])


# main player script logic
# DO NOT CHANGE BELOW ----------------------------
for line in fileinput.input():
    if first_line:
        game = game_API.Game(json.loads(line))
        first_line = False
        continue
    game.update(json.loads(line))
# DO NOT CHANGE ABOVE ---------------------------
    

    # code in this block will be executed each turn of the game

    me = game.get_self()
    a = 0.102228639255
    b = 0.414917611699
    c = 0.655304983993
    d = 0.896476523605
    e = 0.142180437508
    f = 0.135441633014
    g = 0.105965763917
    h = 0.869586178071

    if me.location == me.destination: # check if we have moved this turn
        # create list of the priority level for each monster
        allmonsters = game.get_all_monsters()
        mlist = []
        for monster in allmonsters:
            mlist.append(priority(monster))

    # choose monster with max priority

        maxpriority = mlist.index(max(mlist))
        target = allmonsters[maxpriority]

    # get the set of shortest paths to that monster
        paths = game.shortest_paths(me.location, target.location)
        destination_node = paths[random.randint(0, len(paths)-1)][0]
    # choose monster with max priority
    else:
        destination_node = me.destination

    if game.has_monster(me.location):
        # if there's a monster at my location, choose the stance that damages that monster
        chosen_stance = get_winning_stance(game.get_monster(me.location).stance)
    else:
        # otherwise, pick a random stance
        chosen_stance = stances[random.randint(0, 2)]

    # submit your decision for the turn (This function should be called exactly once per turn)
    game.submit_decision(destination_node, chosen_stance)

    