class Entity():
    
    def __init__(self, name, hp, maxhp, attack, defense, shield,
                 shieldincrease, xp):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.attack = attack
        self.defense = defense #1.10 = 10% def = 10 defense
        self.shield = shield
        self.shieldincrease = shieldincrease
        self.xp = xp
    


class PlayerEntity(Entity):
    
    def __init__(self, name, hp, maxhp, attack, defense, shield,
                 shieldincrease, gold, xp, level):
        super().__init__(name, hp, maxhp, attack, defense,
                         shield, shieldincrease, xp)
        self.gold = gold
        self.level = level
        
        def TakeDamage(self, enemyAttack):
            self.hp -= (round(enemyAttack / self.defense))
            print(self.hp)
            
            if self.hp <= 0:
                print("Game Over.")

class EnemyEntity(Entity):
    
    def __init__(self, name, hp, maxhp, attack, defense, shield,
                 shieldincrease, lootdrop, hpdrop, shielddrop, xp):
        super().__init__(name, hp, maxhp, attack, defense, shield,
                         shieldincrease, xp)
        self.lootdrop = lootdrop
        self.hpdrop = hpdrop
        self.shielddrop = shielddrop

class Potion():
    
    def __init__(self, name, value, amount):
        self.name = name
        self.value = value
        self.amount = amount


class Weapon(PlayerEntity):
    def __init__(self, name, hp, attack, defense, shield,
                 shieldincrease, gold):
        super().__init__(name, hp, attack, defense, shield,
                         shieldincrease, gold)
    


