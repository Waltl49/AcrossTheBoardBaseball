"""
Rules/Game:
This is Across the Board Baseball, programmed.
Two players compete by rolling a set of two die.
Each die outcome corresponds with a different baseball
outcome: single, walk, SO, FO, etc. Pegs are moved
around the board, simulating the rolled outcome - the
goal is to score more runs than your oppenent.
One player starts at bat and can roll until they have
made three outs. After three outs, the half-inning ends
and the opponent gets their turn to "hit". Nine full innings
make one game, the player with more runs at the end wins.
"""

"""
Dice Roll Key:

1 and 1: Home Run
1 and 2: Double
1 and 3: OUT Fly Out
1 and 4: Walk
1 and 5: OUT Pop Out
1 and 6: Single
2 and 2: Double Play - if there's a runner on 1st (?)
2 and 3: OUT Ground Out
2 and 4: OUT Out
2 and 5: Single, runners advance 2 baseses
2 and 6: OUT Out
3 and 3: Walk
3 and 4: Single
3 and 5: OUT Ground Out
3 and 6: OUT Fly Out
4 and 4: Walk
4 and 5: OUT Pop Out
4 and 6: OUT Out
5 and 5: OUT Strikeout
5 and 6: Sac Fly
6 and 6: Triple
"""

"""
How do we approach this? In the end, I'm imagining there will be main function
that incorporates all elements. Lemme list out what I might need.
Functions:
    -Dice Roll
    -Distinct Outcomes (I don't think there's a functinal difference between Pop Out and Fly Out, for example):
       X - Single
       X - Single, Runners advance 2
       X - Double (Runners advance 2)
       X - Triple
       X - Home Run
       X - Walk
       X - Out (Out, K, Fly/Pop Out, Ground Out)
       X - Double Play (If theres a runner on base)
       X - Sacrfice Fly (Runners advance one base)
    - Outs Checker (Checks if there's three outs)
    - Innings Counter (Maybe not needed, but will essentially stop the loop. I suppose I can just loop it 9 times)

I'm not entirely sure how to define runners on. Maybe a list of [0, 0, 0] could represent bases empty, and "1" would be a any runner on

I also realize I don't need to actually program the entire game, where it would give a score at the end if all I care
about is average runs scored. I can simply simulate one team playing 27 outs and wipe the bases everytime 3 outs are
reached. I think that simplifies this problem quite a bit. 
"""

"""
Base States:

[0,0,0] = No runners on
[1,0,0] = Runner on First
[0,1,0] = Runner on Second
[0,0,1] = Runner on Third
[1,1,0] = Runner on First and Second
[1,0,1] = Runner on First and Third
[0,1,1] = Runner on Second and Third
[1,1,1] = Runner on First, Second, and Third

I also realize that I didn't actually need to have these states be anything specific, they just need to be distinct:
I could've just made runners on first and second "11", or randomly "26". As long as my logic is looking for the right
thing and gives the right outputs, nothing matters. Either way, [1,0,1] and 13 are each understandable ways to represent
runners on first and third: pick your poison. I've chosen the 0s and 1s in case I need to check if a specifc runner is on;
it could reduce the amount of coding I need to do. 
"""

import random

def diceRoll():
    """Rolls two die and outputs as a list
    I think a list would be easier to work with
    """
    
    dice = [random.randint(1, 6), random.randint(1, 6)]
    dice.sort()
    return dice

def single(bases, outs, runs):
    """player hits a single, advancing runners 1 base
    """
    if bases == [0,0,0]:
        bases = [1,0,0]

    elif bases == [1,0,0]:
        bases = [1,1,0]

    elif bases == [0,1,0]:
        bases = [1,0,1]

    elif bases == [0,0,1]:
        bases = [1,0,0]
        runs += 1

    elif bases == [1,1,0]:
        bases = [1,1,1]

    elif bases == [1,0,1]:
        bases = [1,1,0]
        runs += 1

    elif bases == [0,1,1]:
        bases = [1,0,1]
        runs += 1

    elif bases == [1,1,1]:
        bases = [1,1,1]
        runs += 1

    return bases, outs, runs

def double(bases, outs, runs):
    """Player hits a double, advancing runners two bases
    """
    if bases == [0,0,0]:
        bases = [0,1,0]

    elif bases == [1,0,0]:
        bases = [0,1,1]

    elif bases == [0,1,0]:
        bases = [0,1,0]
        runs += 1

    elif bases == [0,0,1]:
        bases = [0,1,0]
        runs += 1

    elif bases == [1,1,0]:
        bases = [0,1,1]
        runs += 1

    elif bases == [1,0,1]:
        bases = [0,1,1]
        runs += 1

    elif bases == [0,1,1]:
        bases = [0,1,0]
        runs += 2

    elif bases == [1,1,1]:
        bases = [0,1,1]
        runs += 2

    return bases, outs, runs

def triple(bases, outs, runs):
    """Player hits a triple, advancing runners 3 bases
    """
    if bases == [0,0,0]:
        bases = [0,0,1]

    elif bases == [1,0,0]:
        bases = [0,0,1]
        runs += 1

    elif bases == [0,1,0]:
        bases = [0,0,1]
        runs += 1

    elif bases == [0,0,1]:
        bases = [0,0,1]
        runs += 1

    elif bases == [1,1,0]:
        bases = [0,0,1]
        runs += 2

    elif bases == [1,0,1]:
        bases = [0,0,1]
        runs += 2

    elif bases == [0,1,1]:
        bases = [0,0,1]
        runs += 2

    elif bases == [1,1,1]:
        bases = [0,0,1]
        runs += 3

    return bases, outs, runs

def homerun(bases, outs, runs):
    """Player hits a homerun, scoring all runners
    """
    if bases == [0,0,0]:
        bases = [0,0,0]
        runs += 1

    elif bases == [1,0,0]:
        bases = [0,0,0]
        runs += 2

    elif bases == [0,1,0]:
        bases = [0,0,0]
        runs += 2

    elif bases == [0,0,1]:
        bases = [0,0,0]
        runs += 2

    elif bases == [1,1,0]:
        bases = [0,0,0]
        runs += 3

    elif bases == [1,0,1]:
        bases = [0,0,0]
        runs += 3

    elif bases == [0,1,1]:
        bases = [0,0,0]
        runs += 3

    elif bases == [1,1,1]:
        bases = [0,0,0]
        runs += 4
    
    return bases, outs, runs

def walk(bases, outs, runs):
    """Runner is walked. Advance runner if forced
    """
    if bases == [0,0,0]:
        bases = [1,0,0]

    elif bases == [1,0,0]:
        bases = [1,1,0]

    elif bases == [0,1,0]:
        bases = [1,1,0]

    elif bases == [0,0,1]:
        bases = [1,0,1]

    elif bases == [1,1,0]:
        bases = [1,1,1]

    elif bases == [1,0,1]:
        bases = [1,1,1]

    elif bases == [0,1,1]:
        bases = [1,1,1]

    elif bases == [1,1,1]:
        bases = [1,1,1]
        runs += 1

    return bases, outs, runs

def single2(bases, outs, runs):
    """A single that advances runners two bases
    """
    if bases == [0,0,0]:
        bases = [1,0,0]

    elif bases == [1,0,0]:
        bases = [1,0,1]

    elif bases == [0,1,0]:
        bases = [1,0,0]
        runs += 1

    elif bases == [0,0,1]:
        bases = [1,0,0]
        runs += 1

    elif bases == [1,1,0]:
        bases = [1,0,1]
        runs += 1

    elif bases == [1,0,1]:
        bases = [1,0,1]
        runs += 1

    elif bases == [0,1,1]:
        bases = [1,0,0]
        runs += 2

    elif bases == [1,1,1]:
        bases = [1,0,1]
        runs += 2

    return bases, outs, runs

def out(bases, outs, runs):
    """Simply an out; includes popout, flyout,
    groundout, and strikeout
    """
    outs += 1
    return bases, outs, runs

def sacfly(bases, outs, runs):
    """a sacrifice; an out is made, but runners
    advance a base. I recognize this is not the
    most realistic baseball outcome - a sacrifice
    rarely would advance a runner from 1st to 2nd,
    but so be it. This is Across the Board baseball,
    not the World Series.
    """
    if bases == [0,0,0]:
        bases = [0,0,0]
        outs += 1

    elif bases == [1,0,0]:
        bases = [0,1,0]
        outs += 1

    elif bases == [0,1,0]:
        bases = [0,0,1]
        outs += 1

    elif bases == [0,0,1]:
        bases = [0,0,0]
        runs += 1
        outs += 1

    elif bases == [1,1,0]:
        bases = [0,1,1]
        outs += 1

    elif bases == [1,0,1]:
        bases = [0,1,0]
        runs += 1
        outs += 1

    elif bases == [0,1,1]:
        bases = [0,0,1]
        runs += 1
        outs += 1

    elif bases == [1,1,1]:
        bases = [0,1,1]
        runs += 1
        outs += 1

    return bases, outs, runs

def doubleplay(bases, outs, runs):
    """This just makes two outs if there's anyone on base.
    Again, not the most realistic mechanic, but so be it.
    """
    if bases == [0,0,0]:
        outs +=1

    elif bases == [1,0,0]:
        bases = [0,0,0]
        outs += 2

    elif bases == [0,1,0]:
        bases = [0,0,0]
        outs += 2

    elif bases == [0,0,1]:
        bases = [0,0,0]
        outs += 2

    elif bases == [1,1,0]:
        bases = [0,1,0]
        outs += 2

    elif bases == [1,0,1]:
        bases = [0,1,0]
        outs += 2

    elif bases == [0,1,1]:
        bases = [0,0,1]
        outs += 2

    elif bases == [1,1,1]:
        bases = [0,1,1]
        outs += 2

    return bases, outs, runs

def outsCheck(bases, outs, runs):
    """Checks to see if three (or more, in the event of a DP)
    have been reached, and resets the bases to 0 if that
    condition is met.
    """
    if outs >= 3:
        bases = [0,0,0]
        outs = 0

def play():
    """Plays the game!
    """
    runs = 0

    for x in range(10):
        bases = [0,0,0]
        outs = 0

        while outs < 3:
            dice = diceRoll()

            if dice == [1, 1]:
                bases, outs, runs = homerun(bases, outs, runs)
                
            elif dice == [1, 2]:
                bases, outs, runs = double(bases, outs, runs)

            elif dice == [1, 3]:
                bases, outs, runs = out(bases, outs, runs)
                
            elif dice == [1, 4]:
                bases, outs, runs = walk(bases, outs, runs)

            elif dice == [1, 5]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [1, 6]:
                bases, outs, runs = single(bases, outs, runs)

            elif dice == [2, 2]:
                bases, outs, runs = doubleplay(bases, outs, runs)

            elif dice == [2, 3]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [2, 4]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [2, 5]:
                bases, outs, runs = single2(bases, outs, runs)

            elif dice == [2, 6]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [3,3]:
                bases, outs, runs = walk(bases, outs, runs)

            elif dice == [3,4]:
                bases, outs, runs = single(bases, outs, runs)

            elif dice == [3,5]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [3,6]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [4,4]:
                bases, outs, runs = walk(bases, outs, runs)

            elif dice == [4,5]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [4,6]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [5,5]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [5,6]:
                bases, outs, runs = sacfly(bases, outs, runs)

            elif dice == [6,6]:
                bases, outs, runs = triple(bases, outs, runs)

            # print(bases, outs, runs)

    return runs


def averageRuns(n):
    """find the average runs each sim
    """
    total = 0
    for x in range(n+1):
        total += play()

    average = total/n

    return average

# In [221]: averageRuns(1000000)
# Out[221]: 7.607069

# In [28]: averageRuns(10000000)
# Out[28]: 7.6016799

#NEW DOUBLE PLAY#

# In [8]: averageRuns(1000000)
# Out[8]: 7.570015

# In [10]: averageRuns(10000000)
# Out[10]: 7.5689275


def play2():
    """Plays the game!
    """
    runs = 0

    for x in range(10):
        bases = [0,0,0]
        outs = 0

        while outs < 3:
            dice = diceRoll()

            if dice == [1, 1]:
                bases, outs, runs = homerun(bases, outs, runs)
                
            elif dice == [1, 2]:
                bases, outs, runs = triple(bases, outs, runs)

            elif dice == [1, 3]:
                bases, outs, runs = double(bases, outs, runs)
                
            elif dice == [1, 4]:
                bases, outs, runs = single(bases, outs, runs)

            elif dice == [1, 5]:
                bases, outs, runs = walk(bases, outs, runs)

            elif dice == [1, 6]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [2, 2]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [2, 3]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [2, 4]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [2, 5]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [2, 6]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [3,3]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [3,4]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [3,5]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [3,6]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [4,4]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [4,5]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [4,6]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [5,5]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [5,6]:
                bases, outs, runs = out(bases, outs, runs)

            elif dice == [6,6]:
                bases, outs, runs = out(bases, outs, runs)

            # print(bases, outs, runs)

    return runs

def averageRuns2(n):
    """find the average runs each sim
    """
    total = 0
    for x in range(n+1):
        total += play2()

    average = total/n

    return average