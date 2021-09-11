#Yatzee
import random

class Game:
    score = 0
    upperScore = 0
    slots = {
        'Three_of_a_Kind' : True,
        'Four_of_a_Kind' : True,
        'YATZEE' : True,
        'Small_Str8' : True,
        'Large_Str8' : True,
        'Full_House' : True,
        'Chance' : True,
        'Ones' : True,
        'Twos' : True,
        'Threes' : True,
        'Fours' : True,
       'Fives' : True,
        'Sixes' : True,
        }
        
    gameRounds = 0

    def YatzeeRoll():
        yeet = []
        #handles all the Yatzee cases
        for g in Game.slots:
            if(Game.slots[g]): yeet.append(g)
        if("YATZEE" in yeet): yeet.remove("YATZEE")
        print("Your options of scoring are:\n")
        for l in yeet:
            print(l + "    (" + str(yeet.index(l)+1) + ")")
        if(len(yeet)>0): 
            choice = input("\nInput which choice you would like in the form of it's order in the list: ")
            choice = ''.join(filter(lambda x: x.isdigit(), choice))
            choice = int(list(choice)[0])
            Game.score+=50
            print("You chose " + str(yeet[choice-1]))
            if(yeet[choice-1] == "Ones"):
                Game.slots["Ones"] = False
                Game.score+=(1*5)
                Game.upperScore+=(1*5)
            if(yeet[choice-1] == "Twos"):
                Game.slots["Twos"] = False
                Game.score+=(2*5)
                Game.upperScore+=(2*5)
            if(yeet[choice-1] == "Threes"):
                Game.slots["Threes"] = False
                Game.score+=(3*5)
                Game.upperScore+=(3*5)
            if(yeet[choice-1] == "Fours"):
                Game.slots["Fours"] = False
                Game.score+=(4*5)
                Game.upperScore+=(4*5)
            if(yeet[choice-1] == "Fives"):
                Game.slots["Fives"] = False
                Game.score+=(5*5)
                Game.upperScore+=(5*5)
            if(yeet[choice-1] == "Sixes"):
                Game.slots["Sixes"] = False
                Game.score+=(6*5)
                Game.upperScore+=(6*5)
            if(yeet[choice-1] == "Three_of_a_Kind"):
                Game.slots["Three_of_a_Kind"] = False
                sumy = 0
                for g in rolls:
                    sumy+=g
                Game.score+=sumy
            if(yeet[choice-1] == "Four_of_a_Kind"):
                Game.slots["Four_of_a_Kind"] = False
                sumy = 0
                for g in rolls:
                    sumy+=g
                Game.score+=sumy
            if(yeet[choice-1] == "Small_Str8"):
                Game.slots["Small_Str8"] = False
                Game.score+=30
            if(yeet[choice-1] == "Large_Str8"):
                Game.slots["Large_Str8"] = False
                Game.score+=40
            if(yeet[choice-1] == "Full_House"):
                Game.slots["Full_House"] = False
                Game.score+=25
        
    def DieRoll(num):
        #rolls a number of die
        Li = []
        for g in range(num):
            Li.append(random.randint(1,6))
        return Li
    
    def ScoreRound(rolls):
        #Hold each Round case scoring
        options = []
        for g in Game.slots:
            if(Game.slots[g]): options.append(str(g))     
        UserOptions = Game.GetSuggestions(rolls)
        print("\n\nYour rolls are : (Now sorted for your convience)\n" + str(rolls) + "\n")
        print("I would recommend one of these:\n") 
        for l in UserOptions:
            print(l + "     (" + str(options.index(l)+1) + ")")

        print("\n\nChoose one from a option below: ")
        for l in options:
            print(l + "     (" + str(options.index(l)+1) + ")")
        choice = input("\nInput which choice you would like in the form of it's order in the list: ")
        choice = ''.join(filter(lambda x: x.isdigit(), choice))
        choice = int(choice) 
        print("You chose " + str(options[choice-1]))

        #Checks user choice and determines point values
        if(options[choice-1] == "Three_of_a_Kind"):
            Game.slots["Three_of_a_Kind"] = False
            sumy = 0
            for g in rolls:
                sumy+=g
            if("Three_of_a_Kind" in UserOptions):Game.score+=sumy
        if(options[choice-1] == "Four_of_a_Kind"):
            Game.slots["Four_of_a_Kind"] = False
            sumy = 0
            for g in rolls:
                sumy+=g
            if("Four_of_a_Kind" in UserOptions): Game.score+=sumy
        if(options[choice-1] == "YATZEE"):
            if("YATZEE" in UserOptions): Game.YatzeeRoll()
            Game.slots["YATZEE"] = False
        if(options[choice-1] == "Small_Str8"):
            Game.slots["Small_Str8"] = False
            if("Small_Str8" in UserOptions):Game.score+=30
        if(options[choice-1] == "Large_Str8"):
            Game.slots["Large_Str8"] = False
            if("Large_Str8" in UserOptions): Game.score+=40
        if(options[choice-1] == "Full_House"):
            Game.slots["Full_House"] = False
            if("Full_House" in UserOptions): Game.score+=25
        if(options[choice-1] == "Ones"):
            Game.slots["Ones"] = False
            Game.score += (1*rolls.count(1))
            Game.upperScore += (1*rolls.count(1))
        if(options[choice-1] == "Twos"):
            Game.slots["Twos"] = False
            Game.score += (2*rolls.count(2))
            Game.upperScore += (1*rolls.count(2))
        if(options[choice-1] == "Threes"):
            Game.slots["Threes"] = False
            Game.score += (3*rolls.count(3))
            Game.upperScore += (1*rolls.count(3))
        if(options[choice-1] == "Fours"):
            Game.slots["Fours"] = False
            Game.score += (4*rolls.count(4))
            Game.upperScore += (1*rolls.count(4))
        if(options[choice-1] == "Fives"):
            Game.slots["Fives"] = False
            Game.score += (5*rolls.count(5))
            Game.upperScore += (1*rolls.count(5))
        if(options[choice-1] == "Sixes"):
            Game.slots["Sixes"] = False
            Game.score += (6*rolls.count(6))
            Game.upperScore += (1*rolls.count(6))
        if(options[choice-1] == "Chance"):
            Game.slots["Chance"] = False
            sumy = 0
            for g in rolls:
                sumy+=g
            Game.score+=sumy
        
        Game.gameRounds+=1
        print("Score: " + str(Game.score))
        if(Game.gameRounds < 13):
            Game.Round()
        else:
            if(Game.upperScore>=63): score+=35
            print("\n\nOk, You completed a game with a score of: " + str(Game.score))

        
    def Round():
        # holds basic start of the round
        rolls = Game.DieRoll(5)
        rerolls = 0
        print("Your rolls are : " + str(rolls))
        while(1==1): 
            us = input("Would you like to reroll any dice or score the current dice? (R/S) ")
            if((us == 'r' or us == 'R')):
                if(rerolls<3):
                    select = input("Select which dice you want rerolled:  ")
                    select = ''.join(filter(lambda x: x.isdigit(), select))
                    select = list(select)
                    for g in select:
                        if(int(g)<6 and int(g)>0):
                            rolls[int(g)-1] = Game.DieRoll(1)[0]
                    rerolls+=1
                    print("Your rolls are : " + str(rolls))
                else:
                    print("Whoops, You've run out of rerolls")
                    return(Game.ScoreRound(rolls))
                
            if(us == 's' or us == 'S'):
                return(Game.ScoreRound(rolls))


    def GetSuggestions(rolls):
        # determines which scoring options yield point for user to use
        UserOptions = []
        for g in rolls:
            if((rolls.count(g) == 5) and Game.slots["YATZEE"]):
                UserOptions.append("YATZEE")
            if((rolls.count(g) >= 4) and Game.slots["Four_of_a_Kind"]):
                UserOptions.append("Four_of_a_Kind")
            if((rolls.count(g) >= 3) and Game.slots["Three_of_a_Kind"]):
                UserOptions.append("Three_of_a_Kind")
                
        if(Game.slots["Ones"] and 1 in rolls):   UserOptions.append("Ones")
        if(Game.slots["Twos"] and 2 in rolls):   UserOptions.append("Twos")
        if(Game.slots["Threes"] and 3 in rolls):   UserOptions.append("Threes")
        if(Game.slots["Fours"] and 4 in rolls):   UserOptions.append("Fours")
        if(Game.slots["Fives"] and 5 in rolls):   UserOptions.append("Fives")
        if(Game.slots["Sixes"] and 6 in rolls):   UserOptions.append("Sixes")
            
        if (Game.slots["Small_Str8"]):
            rolls.sort()
            temp = rolls[:len(rolls)-1]
            tempy = rolls[1:len(rolls)]
            if ((sorted(temp) == list(range(min(temp), max(temp)+1))) or (sorted(tempy) == list(range(min(tempy), max(tempy)+1)))):
                UserOptions.append("Small_Str8")
                
        if (Game.slots["Large_Str8"]):
            rolls.sort()
            if (sorted(rolls) == list(range(min(rolls), max(rolls)+1))):
                UserOptions.append("Large_Str8")    

        if (Game.slots["Full_House"]):
            for g in rolls:
                if(rolls.count(g) == 3 and len(set(rolls)) == 2):
                    UserOptions.append("Full_House")
                    break

                
        if(Game.slots["Chance"]): UserOptions.append("Chance")
        return set(UserOptions)
    
Game.Round()
