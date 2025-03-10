import sys
#not perfect
no_of_blocks=9
playerx=[]
playero=[]
no_of_turns=0

def check_for_winplayero():
    for i in range(len(playero)-2):
        if playero[i+1]-playero[i]==1 and playero[i+2]-playero[i+1]==1:
             print("playero wins")
             sys.exit()#to end the program if the condition is fulfill from chatgpt

def check_for_winplayerx():
    for i in range(len(playerx)-2):
        if playero[i+1]-playero[i]==1 and playero[i+2]-playero[i+1]==1:
             print("playero wins")
             sys.exit()#to end the program if the condition is fulfill from chatgpt

while no_of_turns<no_of_blocks:
    if no_of_turns%2==0:
        turn = int(input("enter block number:"))
        playero.append(turn)
        print(playero)
        check_for_winplayero()
    else:
        turn = int(input("enter block number:"))
        playerx.append(turn)
        print(playerx)
    no_of_turns += 1




