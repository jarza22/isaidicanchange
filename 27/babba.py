import random

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class DiceBag:
    def __init__(self):
        self.dice_list = []

    def add_die(self, sides):
        self.dice_list.append(Die(sides))

    def singleRoll(self, sides):
        for die in self.dice_list:
            if die.sides == sides:
                return die.roll()
        return -1

    def multiRoll(self, sides, rolls):
        total = 0
        for die in self.dice_list:
            if die.sides == sides:
                for _ in range(rolls):
                    total += die.roll()
                return total
        return -1

# Test code
dice_bag = DiceBag()
dice_bag.add_die(4)
dice_bag.add_die(6)
dice_bag.add_die(10)
dice_bag.add_die(20)
dice_bag.add_die(50)
dice_bag.add_die(100)

# Testing singleRoll and multiRoll
print("Single Rolls:")
for sides in [4, 6, 10, 20, 50, 100]:
    result = dice_bag.singleRoll(sides)
    print(f"Single roll of {sides}-sided die: {result}")

print("\nMulti Rolls:")
for sides in [4, 6, 10, 20, 50, 100]:
    result = dice_bag.multiRoll(sides, 3)  # Rolling 3 times
    print(f"Sum of 3 rolls of {sides}-sided die: {result}")
