#logic inspired from the show Alice in Borderland[S2E5](Queen of Spades Game).
#Rules: 1. All playes guess a number between 1 and 100.
#       2. Whichever player Guesses closest to the Average number multiplied by 0.8 wins the Round.
#       3. Player(s) that do not win get -1 point and move to next round.
#       4. Player(s) that hit -10 points get eliminated and remaining player(s) move to the next round.
#       5. Either one or no players end up winning the game and survive.
#
import random as r
import time as t
def arrDisplay(player,points):
    for i in player:
        print("P"+str(i),end="          ")
    print()
    for j in points: 
        print(j,end="          ")
    print()
def closest(lst, K):
      return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
def Point8GameWinnerIndex(n):
    player_guess=int(input("**Enter Guess for this Round (1-100) : "))
    guess=[player_guess]
    for i in range(0,n-1):
        guess.append(r.randint(0,80))
    avgP8=(sum(guess)/n)*0.8
    Winner=closest(guess,avgP8)
    print("Guesses:")
    for j in guess: 
        print("("+str(j)+")",end="        ")
    print(" - Round Winner : ",guess.index(Winner),"("+str(Winner)+")","[0.8*Average :",avgP8,"]")
    return (guess.index(Winner))
    ###
    #print("Guesses:")
    #for j in range(n):
        #print("Player",j+1,end="     ")                        #useless initial code
    #print()
    #for i in guess:
        #print(i,end="           ")
    #print()
    #print("Winner : Player",guess.index(Winner)+1,"(",Winner,")")
    ###
def MainLogic(death: int,PlArr: list,points: list):
    x=1
    while(len(PlArr)>1):
        while(min(points)>death):
            print("\nRound",x)
            winner=Point8GameWinnerIndex(len(PlArr))
            for i in range(len(points)):
                if i!=winner:
                    points[i]=points[i]-1
            arrDisplay(PlArr,points)
            # t.sleep(2) 
            x+=1
        print("Eliminated Player(s) at Round",x-1,":")
        elim=[i2 for i2 in PlArr if points[PlArr.index(i2)]==(death)]
        print(elim)
        if 0 in elim:
            print("---- You Died ----")
            break
        PlArr=[i1 for i1 in PlArr if i1 not in elim]
        points=[l for l in points if l!=death]
        print("Survivor(s): continuing to Round",x," : ",PlArr,"\n ")
        if len(PlArr)>1:
            t.sleep(3) 
    if len(PlArr)<=1:
        print("Winner of the Point 8 Game : ",PlArr)

n=5 #number of players
death=-10 #point at which player is eliminated
print("\n\n\nDeath Point :",death) 
print("Starting Game...")
t.sleep(1)
PlArr=[u for u in range(n)] #Player Number array
points=[0 for _ in range(n)] #Player points Array
MainLogic(death,PlArr,points) #calling main game function