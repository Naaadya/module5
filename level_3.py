import random
class Warrior:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        

    def attack(self):
        self.health -= 20
        if self.health == 0:
            return False
        return True


class Battle:
    def __init__(self,w1,w2):
        self.w1 = w1
        self.w2 = w2

    def round(self):
        a = random.randint(1,2)
        if a == 1:
            attacked = w1
            attacking = w2
        else:
            attacked = w2
            attacking = w1
        
        res = attacked.attack()
        print('Атаковал ' + attacking.name + ' у ' + attacked.name + ' осталось ' + str(attacked.health) +'% здоровья ' )
        return res

w1 = Warrior('Воин1',100)
w2 = Warrior('Воин2',100)
battle = Battle(w1,w2)

res = battle.round()
while res == True:
    res = battle.round()

print('Битва завершена')
    
