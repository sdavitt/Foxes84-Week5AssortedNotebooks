# this file is intended to house our dice rolling functionality -> when called we want to be able to roll dice, then see the score
# if there is any external functions/modules/libraries I intend to use within this file
# i'll import them at the top
from random import randint

# greed class
    # dice -> a list of 5 integers representing our 5 dice rolls
    # score -> the score of that roll
# when the class is instantiated - the dice will be rolled and the score calculated

# option 1 for structure of roll: list of 5 numbers made using:
    # [randint(1, 6) for x in range(5)] list comprehension=
# option 2 for structure of roll: dictionary where the key is the roll (rolled a 3 or a 1 or a 2) and value is the number of occurances of that roll
    # ex: {1:4, 6:1} -> a roll of four 1s and one 6 aka [1, 1, 1, 1, 6]

class Greed:
    def __init__(self):
        self.roll = [randint(1, 6) for x in range(5)]
        self.score = self.calcScore()

    def calcScore(self):
        """
        calculate the score of a roll in the Greed Dice game
        return an integer representing the score
        """
        sroll = self.convertRoll()
        tally = 0
        for val in sroll: # scores our triplets
            # so for each number we want to check for triplets
            if sroll[val] >= 3:
                # we have a triplet, increase score
                if val != 1:
                    tally += val*100
                    sroll[val] -= 3
                else:
                    tally += 1000
                    sroll[val] -= 3
        if sroll.get(1): # scores our remaining 1s
            tally += 100*sroll[1]
        if sroll.get(5): # scores our remaining 5s
            tally += 50*sroll[5]
        return tally


    def convertRoll(self):
        """
        takes the list format of the roll and returns the dictionary format of the same roll
        """
        droll = {}
        for val in self.roll:
            if val in droll:
                droll[val] += 1
            else:
                droll[val] = 1
        return droll