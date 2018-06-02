
HPenemy = 200
HPplayer = 200
#BuffP = 1
BuffL = 1
usedL=0
usedTW=0
atck=0
dfns=0
spd=0
enemySpd=0
import random
import sys
import math
Fl = math.floor
#Your Pokemon
def Tackle(HPenemy,BuffP):
    DmgTackle = 25
    DmgTackle=DmgTackle*BuffP*atck
    DmgTackle=Fl(DmgTackle)
    #if BuffP > 1:
        #DmgTackle = DmgTackle * BuffP
    print('Your Pokemon used BodySlam!')
    input('')
    print('Enemy Pokemon has received', DmgTackle, 'damage!')
    HPenemy = HPenemy - DmgTackle
    return(HPenemy)

def TailWhip(BuffP):
    BuffP = BuffP*1.5
    print('Your Pokemon used Tail Whip!')
    input('')
    print('Enemy Pokemon\'s defense has been reduced')

    return(BuffP)

def ChargeBeam(HPenemy, BuffP):
    dmgCh = 40
    dmgCh=dmgCh*BuffP*atck
    dmgCh=Fl(dmgCh)
    miss=random.randint(1,5)
    if miss == 1:
        print('Attack missed!')
    else:
        print('Your Pokemon used Charge Beam!')
        input('')
        print('enemy Pokemon has received',dmgCh,' damage!')
        HPenemy = HPenemy - dmgCh
    return(HPenemy)

def TripleKick(HPenemy, BuffP):
    dmgTK = 13
    dmgTK=dmgTK*BuffP*atck
    dmgTK=Fl(dmgTK)
    xTK=random.randint(1,3)
    xTK1=xTK
    while xTK1 > 0:
        print('Your Pokemon used Triple Kick!')
        HPenemy=HPenemy - dmgTK
        xTK1 = xTK1-1
        print('Enemy Pokemon received',dmgTK,' damage!')
        input('')
    print('Triple Kick hit', xTK, 'times!')
    return(HPenemy)

#Enemy Pokemon
def Scratch(HPplayer, BuffL,Fl):
    dmgScratch = 25
    dmgScratch = dmgScratch*BuffL/dfns
    dmgScratch = Fl(dmgScratch)
    print('Enemy Pokemon used Slash')
    input('')
    print('Your Pokemon received',Fl(dmgScratch),' damage!')
    HPplayer = HPplayer - dmgScratch
    HPplayer = Fl(HPplayer)
    return(HPplayer)

def FurySwipes(HPplayer, BuffL,Fl):
    dmgFS = 9
    dmgFS = dmgFS*BuffL/dfns
    dmgFS = Fl(dmgFS)
    xFS = random.randint(1,5)
    xFS1 = xFS
    while xFS1 > 0:
        print('Enemy Pokemon used Fury Swipes!')
        HPplayer = HPplayer - Fl(dmgFS)
        xFS1 = xFS1 - 1
        print('Your Pokemon received',Fl(dmgFS),' damage!')
        input('')
    print('Fury Swipes hit', xFS, 'times!')
    return (HPplayer)

def Leer(BuffL):
    BuffL = BuffL*1.75
    print('Enemy Pokemon used Screech!')
    input('')
    print('Your Pokemon\'s defense has been reduced')
    return(BuffL)

def MoveSelectPl(HPenemy,BuffP,usedTW):
    print('[1] BodySlam')
    print('[2] Charge Beam')
    print('[3] Triple Kick')
    print('[4] Tail Whip')

    while True:
        try:
            Move = int(input('choose your move   '))
            break
        except ValueError:
            print('Please choose a valid number')
            input('')
    while Move > 4 or Move < 1:
        print('Please choose a valid number')
        input('')
        try:
            Move= int(input('choose your move   '))
        except ValueError:
            pass
    if Move == 1:
        HPenemy = Tackle(HPenemy, BuffP)
    elif Move == 4:
        if usedTW == 4:
            print('Enemy defense cannot be decreased any further!')
        else:
            BuffP=TailWhip(BuffP)
            usedTW = usedTW+1
    elif Move == 2:
        HPenemy = ChargeBeam(HPenemy, BuffP)
    elif Move == 3:
        HPenemy = TripleKick(HPenemy, BuffP)
    return(HPenemy,BuffP,usedTW)

def MoveSelectEn(HPplayer, BuffL,usedL):
    EnM = random.randint(1,3)
    if EnM == 3:
        if usedL == 3:
            EnM=random.randint(1,2)
        else:
            BuffL=Leer(BuffL)
            usedL = usedL+1
    elif EnM == 1:
        HPplayer = Scratch(HPplayer,BuffL,Fl)
    elif EnM == 2:
        HPplayer = FurySwipes(HPplayer,BuffL,Fl)
    #elif EnM == 3:
        #BuffL=Leer(BuffL)
        #usedL = usedL+1
        #if usedL == 3:
            #EnM = random.randint(1,2)
    return(HPplayer,BuffL,usedL)

def PlayerTurn(HPenemy,BuffP,usedTW,HPplayer,Fl):
    PlScore = MoveSelectPl(HPenemy, BuffP, usedTW)
    HPenemy = PlScore[0]
    BuffP = PlScore[1]
    usedTW = int(PlScore[2])
    input('')
    if HPenemy < 1:
        HPenemy = 0
    print('Your HP:', Fl(HPplayer))
    print('Enemy HP:', Fl(HPenemy))
    input('')
    if HPenemy < 1:
        print('Enemy Pokemon defeated!')
        end = input('Enter to end')
        sys.exit()
    return(HPenemy,BuffP,usedTW,PlScore,HPplayer)

def EnemyTurn(HPplayer,BuffL,usedL,HPenemy,Fl):
    EnScore = MoveSelectEn(HPplayer, BuffL, usedL)
    HPplayer = EnScore[0]
    BuffL = EnScore[1]
    usedL = int(EnScore[2])
    input('')
    if HPplayer < 1:
        HPplayer = 0
    print('Your HP:', Fl(HPplayer))
    print('Enemy HP:', Fl(HPenemy))
    input('')
    if HPplayer < 1:
        print('Your Pokemon fainted...')
        end = input('Enter to end')
        sys.exit()
    return(HPplayer,BuffL,usedL,HPenemy,EnScore,HPenemy)

print('Use your points to strengthen your attack, defense or speed!')
print('You have 10 points.')
while True:
    try:
        atck = int(input('Attack: ').strip())
        dfns = int(input('Defense: ').strip())
        if atck + dfns > 10:
            print('the maximum amount of points is 10!')
            input('')
            atck = int(input('Attack: ').strip())
            dfns = int(input('Defense: ').strip())
        spd = int(input('Speed: ').strip())
        if atck + dfns + spd > 10:
            print('the maximum amount of points is 10!')
            atck = int(input('Attack: ').strip())
            dfns = int(input('Defense: ').strip())
            spd = int(input('Speed: ').strip())
        break
    except ValueError:
        print('Please choose a valid number')
        input('')




atck = atck/10+1
dfns = dfns/10+1

enemySpd = random.randint(1,5)

print('A wild enemy Pokemon appeared!')
print('*************************************************')
if spd == enemySpd:
    enemySpd = enemySpd-1
if spd > enemySpd:
    BuffP = 1
    while HPplayer > 0 or HPenemy > 0:
        StatsE = PlayerTurn(HPenemy, BuffP, usedTW, HPplayer,Fl)
        HPenemy = StatsE[0]
        BuffP = StatsE[1]
        usedTW = int(StatsE[2])

        StatsP = EnemyTurn(HPplayer, BuffL, usedL, HPenemy,Fl)
        HPplayer = StatsP[0]
        BuffL = StatsP[1]
        usedL = int(StatsP[2])


else:
    BuffP = 1
    while HPplayer > 0 or HPenemy > 0:
        StatsP = EnemyTurn(HPplayer, BuffL, usedL, HPenemy,Fl)
        HPplayer = StatsP[0]
        BuffL = StatsP[1]
        usedL = int(StatsP[2])

        StatsE = PlayerTurn(HPenemy, BuffP, usedTW, HPplayer,Fl)
        HPenemy = StatsE[0]
        BuffP = StatsE[1]
        usedTW = int(StatsE[2])















