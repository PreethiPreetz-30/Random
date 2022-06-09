import random


def heading():
    print("***************************************************")
    print("\t \t ROCK PAPER SCISSORS")
    print("***************************************************")

"""
1=>ROCK         0=>TIE
2=>PAPER        1=>Player/Player1 wins
3=>SCISSORS     2=>Computer/Player2 wins
"""
def winner(n1,n2):
    if(n1==n2):return(0)
    elif(n1==1 and n2==2):return(2)
    

def Play1vPlay2():
    print("Player 1")
    print("Choose: \n 1.Rock \n 2.Paper \n 3.Scissors")
    player1=int(input())
    print("Player 2")
    print("Choose: \n 1.Rock \n 2.Paper \n 3.Scissors")
    player2=int(input())
    return winner(player1,player2)

def PlayvsComp():
    print("Player vs Computer")
    print("Choose: \n 1.Rock \n 2.Paper \n 3.Scissors")
    player=int(input())
    computer=random.randint(1,3)
    return winner(player,computer)
    


heading()
print("1.Player vs Computer \n2.Player 1 vs Player 2")
choice=int(input("Enter choice :"))
if choice==1:
    while(True):
        result=PlayvsComp()
        if result==1:
            print("Player wins")
            break
        elif result==2:
            print("Computer wins")
            break
        else:
            print("Tie")
else:
    while(True):
        result=Play1vPlay2()
        if result==1:
            print("Player 1 wins")
            break
        elif result==2:
            print("Player 2 wins")
            break
        else:
            print("Tie")


