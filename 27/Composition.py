#InventoryItem
class InventoryItem:
    def __init__(self, name, quantity, value):
        self.name = name
        self.quantity = quantity
        self.value = value
    def __str__(self):
        message = self.name + " x" + str(self.quantity)
        message += ", Value: " + str(self.value) + " "
        message += "(" + str(self.quantity*self.value) + ")"
        return message

#Character
class Character:
    def __init__(self, name, species):
        self.name = name
        self.species = species

#PlayerCharacter
class PlayerCharacter(Character):
    def __init__(self, name, species, inventory):
        super().__init__(name, species)
        self.level = 1
        self.inventory = inventory
    def addItem(self, name, quantity, value):
        for item in self.inventory:
            if name == item.name:
                item.quantity += quantity
                return
        newItem = InventoryItem(name, quantity, value)
        self.inventory.append(newItem)
        return
    def __str__(self):
        message = self.name + ", Lv." + str(self.level) + " " + self.species + "\n"
        for item in self.inventory:
            message += str(item) + "\n"
        return message

#Test Code
item1 = InventoryItem("Iron Arrow", 30, 5)
item2 = InventoryItem("Health Potion", 10, 35)
item3 = InventoryItem("Smoke Bomb", 5, 50)
item4 = InventoryItem("Steel Sword", 1, 220)
#print(str(item2))

newPlayer = PlayerCharacter("Grilka", "Dwarf",
                            [item1, item2, item3, item4])
newPlayer.addItem("Dwarven Bow", 1, 575)
print(str(newPlayer))