'''
Now, open main.py and do the following.
    1. Import Die and DiceBag from BagOfDice and CharacterGenerator from RPGCharacterCreator.
    2. Create a DiceBag object with 2, 4, 6, 10, 20, 50, and 100 sided dice.
    3. Create a CharacterGenerator object; pass in your created DiceBag object.
    4. Call your CharacterGenerator's buildCharacter method.
    5. Print the object to the terminal.

Lastly, run main.py. Save a screenshot showing your code works. This step is worth the remaining 60 points not included in your class definition.
Compress this file, BagOfDice.py, main.py, and your screenshot into a ZiP folder and submit on Canvas.
'''
from BagOfDice import Die
from BagOfDice import DiceBag
from RPGCharacterCreator import CharacterGenerator

'''diceBag = [Die(2), Die(4), Die(6), Die(10), Die(20), Die(50), Die(100)]'''
dice_bag = DiceBag([Die(2),Die(4),Die(6),Die(10),Die(20),Die(50),Die(100)])

characterGenerator = CharacterGenerator(dice_bag)

characterGenerator.buildCharacter()

print(characterGenerator)


