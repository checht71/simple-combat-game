from classes import PlayerEntity, EnemyEntity, Potion
from tkinter import Button, Tk, Label, Toplevel
from functions import newEnemy
from time import sleep
from random import randint

global level
level = 1


Player = PlayerEntity("Player 1", 100, 100, 12, 5, 10, 10, 0, 30, 1)
Enemy1 = EnemyEntity("Enemy 1", 100, 100, 10, 1.05, 10, 5, 0, 0, 0, 10)
HealthPotionSmall = Potion("Small HP Potion", 10, 1)
ShieldPotionSmall = Potion("Small Shield Potion", 20, 1)

print(Player.__dict__)
print(Enemy1.__dict__)

root = Tk()

def PlayerHit(playerAttack):
    infoLabel.config(text="")
    if Enemy1.shield > 0:
        Enemy1.shield -= playerAttack
    enemyShieldLabel.config(text="shield: "+str(Enemy1.shield))
    if Enemy1.shield <= 0:
        print((round(playerAttack / Enemy1.defense)) + Enemy1.shield)
        Enemy1.hp -= (round(playerAttack / Enemy1.defense)) + Enemy1.shield #broken
        Enemy1.shield = 0
        
        if Enemy1.hp <= 0:
            enemyHPLabel.config(text="ENEMY DEFEATED.")
            Player.gold += Enemy1.lootdrop
            goldLabel.config(text='Gold:'+str(Player.gold))
            HealthPotionSmall.amount += Enemy1.hpdrop
            hpsLabel.config(text='HP Potions: '+str(HealthPotionSmall.amount))
            ShieldPotionSmall.amount += Enemy1.hpdrop
            shieldpsLabel.config(text='Shield Potions: '+str(ShieldPotionSmall.amount))
            Player.xp += Enemy1.xp
            Player.hp = Player.maxhp
            xpLabel.config(text="XP:"+str(Player.xp))
            global level
            level+=1
            
            newEnemy(Enemy1)
            print(Enemy1.__dict__)
    hpLabel.config(text="HP: "+ str(Player.hp)+"/"+str(Player.maxhp))
    hpsLabel.config(text='HP Potions: '+str(HealthPotionSmall.amount))
    
    enemyHPLabel.config(text=str(Enemy1.hp)+"/"+str(Enemy1.maxhp))
    enemyShieldLabel.config(text="Shield: "+str(Enemy1.shield))
    EnemyTurn()
    
def EnemyHit(enemyAttack):
    root.update_idletasks()
    root.update()
    sleep(0.2)
    if Player.shield > 0:
        Player.shield -= enemyAttack
    if Player.shield <= 0:
        Player.hp -= (round(enemyAttack / Player.defense))
        hpLabel.config(text="HP: "+ str(Player.hp)+"/"+str(Player.maxhp))
        Player.shield = 0
    
    shieldLabel.config(text="My Shield: "+str(Player.shield))

    if Player.hp <= 0:
        top= Toplevel(root)
        top.geometry("750x250")
        top.title("GAME OVER")
        Label(top, text= "GAME OVER").pack()
        Label(top, text="Level Reached: "+str(level)).pack()
        root.update()
        sleep(4)
        root.destroy()
        
def TakeHealthPotion(myPotion):
    if myPotion.amount <= 0:
        infoLabel.config(text="Not enough Potions!")
    else:
        Player.hp += myPotion.value
        if Player.hp >= Player.maxhp:
            Player.hp = Player.maxhp
        myPotion.amount -= 1
        hpLabel.config(text="HP: "+ str(Player.hp)+"/"+str(Player.maxhp))
        hpsLabel.config(text='HP Potions: '+str(HealthPotionSmall.amount))
        
def TakeShieldPotion(myPotion):
    if myPotion.amount <= 0:
        infoLabel.config(text="Not enough Potions!")
    else:
        Player.shield += myPotion.value
        myPotion.amount -= 1
        shieldLabel.config(text="My Shield: "+str(Player.shield))
        shieldpsLabel.config(text='Shield Potions: '+str(ShieldPotionSmall.amount))

def ShieldUp(myEntity):
    myEntity.shield += myEntity.shieldincrease
    shieldLabel.config(text="My Shield: "+str(Player.shield))
    enemyShieldLabel.config(text="Shield: "+str(Enemy1.shield))
    if myEntity == Player:
        EnemyTurn()
    
def EnemyTurn():
    decision=randint(1,2)
    if decision == 1:
        EnemyHit(Enemy1.attack)
    elif decision == 2:
        ShieldUp(Enemy1)
    Tk.update(root)

def XPShopPurchase(Player, xpwin, kind):
    xpRequired = Player.level * 10 + 30
    
    if Player.xp >= xpRequired:
        if kind == 0:
            Player.attack += Player.attack + 1
        elif kind == 1:
            Player.hp += round(Player.hp * 0.1)
            Player.maxhp += round(Player.maxhp * 0.1)
        Player.xp -= xpRequired
        Player.level += 1
        xpwin.destroy()
        XPShop(Player)
        Tk.update(root)
    else:
        noxpwin = Toplevel(xpwin)
        noxpwin.geometry("800x300")
        noxpwin.title("XP Shop")
        nxpl = Label(noxpwin, text="Not enough XP to Level Up!").pack()
        nxpb = Button(noxpwin, text="Close",
                    command=noxpwin.destroy).pack()


def XPShop(Player):
    xpwin = Toplevel(root)
    xpwin.geometry("700x800")
    xpwin.title("XP Shop")
    levelLabel = Label(xpwin, text="Level:"+str(Player.level))
    levelLabel.pack()
    xpLabel = Label(xpwin, text="XP: "+str(Player.xp))
    xpLabel.pack()
    costLabel = Label(xpwin, text="XP Cost to Level Up: "+
                      str(Player.level*10 + 30)).pack()
    buyHPBttn = Button(xpwin, text="HP (+1)",
                command=lambda:XPShopPurchase(Player, xpwin, 1)).pack()
    buyAttackBttn = Button(xpwin, text="+Attack",
                command=lambda:XPShopPurchase(Player, xpwin, 0)).pack()
    closeBttn = Button(xpwin, text="Close", command=xpwin.destroy).pack(pady=100)

def GoldShop(Player):
    goldwin = Toplevel(root)
    goldwin.geometry("700x800")
    goldwin.title("Gold Shop")
    goldLabel = Label(xpwin, text="XP: "+str(Player.gold))
    goldLabel.pack()
    costLabel = Label(xpwin, text="XP Cost to Level Up: "+
                      str(Player.level*10 + 30)).pack()
    buyHPBttn = Button(xpwin, text="Buy HP Potion (+10 HP) 50 Gold",
                command=lambda:GoldShopPurchase(Player, xpwin, 1)).pack()
    buyShieldBttn = Button(xpwin, text="Buy Shield Potion (+10 Shield) 60 Gold",
                command=lambda:GoldShopPurchase(Player, xpwin, 0)).pack()
    closeBttn = Button(xpwin, text="Close", command=xpwin.destroy).pack(pady=100)

#Window features
root.option_add( "*font", "lucida 36 bold italic" )
root.title("Simple Combat Game")
root.geometry("800x900")

hpLabel = Label(root, text="HP: "+ str(Player.hp)+"/"+str(Player.maxhp))
hpLabel.pack()
shieldLabel = Label(root, text="My Shield: "+str(Player.shield))
shieldLabel.pack()
defenseLabel = Label(root, text="Def: "+ str(Player.defense)).pack()
goldLabel = Label(root, text='Gold:'+str(Player.gold))
goldLabel.pack()
xpLabel = Label(root, text="XP:"+str(Player.xp))
xpLabel.pack()
hpsLabel = Label(root, text='HP Potions: '+str(HealthPotionSmall.amount))
hpsLabel.pack()
shieldpsLabel = Label(root, text='Shield Potions: '+str(ShieldPotionSmall.amount))
shieldpsLabel.pack()


enemyHPLabel = Label(root, text=str(Enemy1.hp)+"/"+str(Enemy1.maxhp))
enemyHPLabel.pack()
enemyShieldLabel = Label(root, text="Shield: "+str(Enemy1.shield))
enemyShieldLabel.pack()
infoLabel = Label(root, text='')
infoLabel.pack()

attackBttn = Button(root, text="Attack (+"+str(Player.attack)
                    +")", command=lambda: PlayerHit(Player.attack)).pack()
shieldUpBttn = Button(root, text="Shield Up (+20)",
                      command=lambda:TakeShieldPotion(ShieldPotionSmall))
shieldUpBttn.pack()

hpsBttn = Button(root, text="Drink HP Potion", 
                    command=lambda:TakeHealthPotion(HealthPotionSmall))
hpsBttn.pack()
xpShopBttn=Button(root, text="Level Up", 
                  command=lambda: XPShop(Player))
xpShopBttn.pack()
inventoryBttn=Button(root, text="Open Inventory")
inventoryBttn.pack()
root.mainloop()
