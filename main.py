#====Data:====
import random

weapon_damage = {
    "rusty sword": 3,
    "worn sword": 5,
    "iron sword": 10
}

#===== classes =====
class player:
    def __init__(self, name, health, Max_Health , gold, potions, weapon, inventory):
        self.name = name
        self.health = 100
        self.Max_Health = 100
        self.gold = 0
        self.potions = 0
        self.weapon = "rusty sword"
        self.inventory = []
    
    def take_damage(self, damage):
         print(f"{self.name} took {damage} damage")
         self.health -= damage
         print(f"your HP:{self.health}/{self.Max_Health}")
         if self.health <= 0:
            print("you have fallen in battle. game over :(") 
    
    def heal_player(self):
        if self.potions <= 0:
            print("you do not have any potions left -_-")

        elif self.health >= self.Max_Health:
            print("you already have the max amount of health")

        else:
            self.health = min(self.health + 3, self.Max_Health)
            self.potions -= 1
            print(f"{self.name} drank a potion and healed 3 health.")
            print(f"health is now {self.health}/{self.Max_Health}")
            print(f"you have {self.potions} potions remaining")
    
    def attack(self, damage):
        damage = weapon_damage[self.weapon]
        print(f"you attacked and dealt {damage} damage!")

class enemy:
    def __init__(self, name, damage, Max_Health, health, gold_drop):
        self.name = name
        self.damage = damage
        self.Max_Health = Max_Health
        self.health = health
        self.gold_drop = gold_drop
    
    def attack(self):
        print(f"the {self.name} attacked you and did {self.damage}")
    

    def take_damage(self):
        print(f"{self.name}HP: {self.health}/{self.Max_Health} ")
        if self.health <=0:
            print(f"you killed the {self.name}!")
            print(f"the {self.name} dropped {self.gold_drop} gold!")


#===== functions =====
def fight(current_enemy):
    while True:
        hero.take_damage(current_enemy.damage)
        current_enemy.health -= weapon_damage[hero.weapon]
        hero.attack()
        current_enemy.take_damage()
        if hero.health <= 0:
            break
            
        elif current_enemy.health <= 0:
            return "won"
        
#===== scenes: ====
def intro():
    name = input("greetings, traveller. What is your name?\n")
    return player(name)

def first_scene():
    print("=== Scene one: a fork in the road ===")
    print("You are a traveller on a journey to find treasure in an abandoned fortress. After a few days of walking you find yourself at a fork in the road." \
    " you can go left and walk along the river or turn right and enter gloomy forest. What do you do?\n")
    while True:
        Input = input("1. go left -> river\n 2. go right ->forest\n")
        if Input == "1":
            print("you decide to walk along the river.")
            return "river scene"

        elif Input == "2":
            print("you decide to go into the forest")
            return "forest scene"
        
        else:
            print("invalid input, please enter either '1' or '2'.")

#river scene 2A
def river_scene():
    print("=== Scene two: Good Karma ===")
    print("after some time walking you run into an injured merchant sitting on the bank of the river, he asks for your help. do you help him?\n")
    while True:
        Input = input("1. help him\n 2.ignore him \n")
        if Input == "1":
            print("you stitch up the merchants wounds and send him on his way. he gives you a health potion as a thank you " \
            "and tells you about a nearby cave rumoured to have a mysterious, valuable treasure deep inside.")
            hero.potions += 1
            print(hero.potions)
            return "helped"

        elif Input == "2":
            print("you continue on.")
            return "ignored"

        else:
            print("invalid input, please enter either '1' or '2'.")

#forest scene 2B
def forest_scene():
    print("=== Scene two: Furry Friends ===")
    print("after some walking you stumble into a clearing in the forest. on the ground you see a small satchel of gold. you pick it up")
    hero.gold += 10
    print(f"you have {hero.gold} gold")
    print("all of a sudden a vicious wolf emerges from the trees and starts circling you. what do you do?")
    while True:
        Input = input("1. fight / 2. run / 3. heal\n")
        if Input == "1":
            current_enemy = enemy("wolf", 20, 30, 30, 0)
            fight(current_enemy) 
            return "cave scene"
        
        elif Input == "2":
            print("You take off down the path with the wolf following close behind. after a few minutes of running " \
            "you are able to lose it however you check your pocket and realise you lost the gold during the chase.")
            hero.gold -= 10
            print(hero.gold)
            return "cave scene"
        
        elif Input == "3":
            hero.heal_player()
        
        else:
            print("invalid input please enter either '1', '2', '3'.")
    
def cave_scene():
    print("=== Scene three: The Cave === ")
    print("you stumble across an ominous looking cave. do you enter ?")
    while True:
        Choice = input("y / n\n")
    
        if Choice == "y":
            print("you decide to go in. after some walking you find a worn old sword on the ground. you pick it up.")
            hero.weapon = "worn sword"
            return "deeper"
        
        elif Choice == "n":
            print("you decide not to risk it")
            return "merchant"
        
        else:
            print("invalid input. please enter either 'y' or 'n'")
    
def deeper_cave():
    print("you notice the cave runs deeper underground through a tight passage, do you continue on?")
    while True:
        Choice = input("y / n\n")
        if Choice == "y":
            print("after you squeeze through the passage you arrive at an opening in the cave. All of a sudden a giant spider ambushes you from the ceiling. ")
            current_enemy = enemy("giant Spider", 30, 10, 10, 20)

            result = fight(current_enemy)
            if result == 'won':
                print("when the spider died it dropped a cloak of invisibility and 20 gold!")
                hero.inventory.append("invisibility cloak")
                hero.gold += 20
                print(f"{hero.name}'s gold: {hero.gold}.")
                return "merchant"


        elif Choice == "n":
            print("you decide not to risk it.")
            return "merchant"
        
        else:
            print("invalid input please enter either, 'y' or 'n'.")

def merchant_scene():
    print("=== Scene three: the wandering merchant ===")
    print("after exiting the cave, you come across a travelling merchant. he asks if you want to browse his wares.")
    while True:
        Choice = input("shop / leave\n")
        if Choice == "shop":
            item = input("what would you like buy?\n 1.iron sword: 20 gold\n2.health potion: 10 gold")
            if item == "1":
                if hero.gold >= 20:
                    hero.gold -= 20
                    print("you bought an iron sword!")
                    hero.weapon = "iron sword"
                
                elif hero.gold < 20:
                    print("you do not have enough gold -_-")
                
            if item == "2":
                if hero.gold >= 10:
                    hero.gold -= 10
                    print("you bought a potion!")
                    hero.potions += 1
                    print(f"you now have {hero.potions} potions.")
                
                elif hero.gold < 10:
                    print("you do not have enough gold -_-")
            
        
        elif Choice == "leave":
            print("you continue on.")
            return "guard scene"
        
        else:
            print("invalid input, please enter either 'shop' or 'leave'.")
    
def guard_scene():
    current_enemy = enemy("guard",12, 30, 30, 0)
    Percent_Chance_NoCloak = 50
    Percent_Chance_Cloak = 20
    thresh1 = Percent_Chance_NoCloak / 100
    thresh2 = Percent_Chance_Cloak / 100
    print("=== Scene four: gates of greystone ===")
    print("after another long day of walking, you finally arrive at the fortress. there is a bandit guard stationed at the entrance. " \
    "what do you do?")
    while True:
        Choice = input(" 1. fight him / 2. sneak past / 3. bribe him\n")
        if Choice == "1":
            result = fight(current_enemy)
            if result == 'won':
                return "treasure"
        
        elif Choice == "2":
            if "invisibility cloak" in hero.inventory:
                if random.random() > thresh2:
                    print("you snuck past the guard with ease thanks to the invisibility cloak!")
                    return "treasure"
                
                else: 
                    print("you put the cloak on but you accidently made noise and the guard found you! now you have no choice but to fight!")
                    result = fight(current_enemy)
                    if result == 'won':
                        return "treasure"
            
            elif "invisibility cloak" not in hero.inventory:
                print("you spot a gap in the fence and try to slip through...")
                if random.random() > thresh1:
                    print("It worked! you made it into the fortress!")
                    return "treasure"
                
                else:
                    print("it didn't work -_- the guard caught you and now you have no choice but to fight!")
                    result = fight(current_enemy)
                    if result == 'won':
                        return "treasure"

        elif Choice == "3":
            if hero.gold >=15:
                print("you gave the guard 15 gold and he agreed to let you through and turn a blind eye.")
                hero.gold -= 15
                print(f"you have {hero.gold} remaining.")
                return "treasure"
            
            elif hero.gold <15:
                print("you do not have enough gold to bribe the guard.")
        
        else:
            print("invalid input, please try again")

def final_scene():
    current_enemy = enemy("leader", 18, 50, 50, 0)
    print("=== Scene five: the bandits keep ===")
    print("shortly after, you find your way into the treasure room. however when you get there you spot the bandit leader halfway through moving the treasure already.")
    print("what do you do?")
    while True:
        Choice = input("1. fight him / 2. attempt to negotiate with him")
        if Choice == "1":
            print("you decide to challenge the bandit leader.")
            result = fight(current_enemy)
            if result == "won":
                return "good ending"
            
            else:
                return "bad ending"
        
        elif Choice == "2":
            print("you attempt to negotiate with the bandit leader.")
            print("you approach him and try to strike a deal for the remaining part of the treasure that he hasn't taken yet")
            if hero.weapon == "iron sword":
                print("the bandit notices the weapon in your sheath and gets intimidated. he decides to let you have the treasure he hasn't taken as opposed to risking a fight with you.")
                return "neutral ending"

            else:
                print("it didn't work, the leader saw no reason to share his winnings with you. instead he attacks!")
                result = fight(current_enemy)
                if result == "won":
                    return "good ending"
                
                else: 
                    return "bad ending"
        
        else:
           print ("invalid input please try again")

# === endings: ===
def good_ending():
    print("=== Ending: fortune favours the bold ===")
    print("you were able to best the leader of the bandits in a fight to the death and leave the fortress with the entirety of the treasure. congrats!!")
    print("The END.")             

def neutral_ending():
    print("=== Ending: honour amongst thieves ===")
    print("the bandit delivered on his end of the deal and let you leave the fortress with half of the gold.")
    print("The END.")

def bad_ending():
    print("=== Ending: a warrior falls ===")
    print("you fell in combat against the leader of the bandit and he killed you.")
    print("The END.")


hero = intro()

scene = first_scene()

while True:
    if scene == "river scene":
        scene = river_scene()

    elif scene == "forest scene":
        scene = forest_scene()

    elif scene == "helped" or scene == "ignored" or scene == "cave scene":
        scene = cave_scene()

    elif scene == "deeper":
        scene = deeper_cave()

    elif scene == "merchant":
        scene = merchant_scene()

    elif scene == "guard scene":
        scene = guard_scene()

    elif scene == "treasure":
        scene = final_scene()

    elif scene == "good ending":
        good_ending()
        break

    elif scene == "neutral ending":
        neutral_ending()
        break

    elif scene == "bad ending":
        bad_ending()
        break


    
        

