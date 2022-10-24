import random
import time

class Warrior:
    def __init__(self,name,health,armor,endurance):
        self.name = name
        self.health = health
        self.armor = armor
        self.endurance = endurance
        self.minDamage = 10
        self.maxDamage = 30

    def decrement(value, decrement, border = 0):
        if value - decrement < border:
            return border
        return value - decrement

    #защита
    def protect(self):
        if self.armor > 0:
            self.armor = Warrior.decrement(self.armor, random.randint(0,10))
        else:
            self.health = Warrior.decrement(self.health, random.randint(self.minDamage,self.maxDamage))
        self.print()
        if self.health <= 10:
            return False
        return True

    def print(self):
        print(self.name + ': armor=' + str(self.armor) + ', health=' + str(self.health) +',endurance=' + str(self.endurance))
    #атака
    def attack(self, underAttack=False):
        self.endurance = Warrior.decrement(self.endurance, 10)
        if self.endurance <= 0:
            self.minDamage = 0
            self.maxDamage = 10
            
        if underAttack == True:
            self.health = Warrior.decrement(self.health, random.randint(self.minDamage,self.maxDamage), 10)
            self.print()
            if self.health <= 10:
                return False
        else:
            self.print()
        return True


class Battle:
    def __init__(self,w1,w2):
        self.w1 = w1
        self.w2 = w2
        self.counter = 0

    def step(self):
        self.counter +=1
        state = random.randint(1,4)
        if state == 1: # w1 атакует, w2 атакует
            print("step #"+str(self.counter) + ": " + self.w1.name + " attack, " + self.w2.name + " attack")
            res = self.w1.attack(True)
            if res == False:
                Battle.printWinner(self.w2)
                return False
            res = self.w2.attack(True)
            if res == False:
                Battle.printWinner(self.w1)
                return False

        elif state == 2: # w1 атакует, w2 защищается
            print("step #"+str(self.counter) + ": " + self.w1.name + " attack, " + self.w2.name + " protect")
            res = self.w1.attack()
            if res == False:
                Battle.printWinner(self.w2)
                return False
            res = self.w2.protect()
            if res == False:
                Battle.printWinner(self.w1)
                return False

        elif state == 3: # w1 защищается, w2 атакует
            print("step #"+str(self.counter) + ": " + self.w1.name + " protect, " + self.w2.name + " attack")
            res = self.w1.protect()
            if res == False:
                Battle.printWinner(self.w2)
                return False
            res = self.w2.attack()
            if res == False:
                Battle.printWinner(self.w1)
                return False

        else: # state == 4: w1 защищается, w2 защищается
            print("step #"+str(self.counter) + ": " + self.w1.name + " protect, " + self.w2.name + " protect")
            return True
    
    def printWinner(w):
        print(w.name + ' is a winner!!!\r\nBattle is over!!!')


w1 = Warrior("Warrior1",100,100,100)
w2 = Warrior("Warrior2",100,100,100)
battle = Battle(w1,w2)

while True:
    time.sleep(1)
    res = battle.step()
    if res == False:
        break


    
