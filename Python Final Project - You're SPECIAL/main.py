from BagOfDice import Die, DiceBag
from RPGCharacterCreator import CharacterGenerator

d2 = Die(2)
d4 = Die(4)
d6 = Die(6)
d10 = Die(10)
d20 = Die(20)
d50 = Die(50)
d100 = Die(100)

diceList = [d2, d4, d6, d10, d20, d50, d100]
bag = DiceBag(diceList)

generator = CharacterGenerator(bag)

generator.buildCharacter()

print(generator)
