'''
Experiment_6
'''

import os
import time 

player=1
Win=1
Stop=1
Draw=-1
Running=0
Game=Running
Mark='X'
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
'''draw the board'''
def DrawBoard():
    print(" %c | %c | %c "%(board[1],board[2],board[3]))
    lines()
    print(" %c | %c | %c"%(board[4],board[5],board[6]))
    lines()
    print(" %c | %c | %c "%(board[7],board[8],board[9]))
def lines():
    print("___|___|___")

def CheckPosition(x):
    if board[x]==' ':
        return True
    else:
        return False
    
def CheckWin():
    global Game
    if board[1]==board[2] and board[2]==board[3] and board[1]!=' ':
        Game=Win
    elif board[4]==board[5] and board[5]==board[6] and board[4]!=' ':
        Game=Win
    elif board[7]==board[8] and board[8]==board[9] and board[7]!=' ':
        Game=Win
    elif board[1]==board[4] and board[4]==board[7] and board[1]!=' ':
        Game=Win
    elif board[2]==board[5] and board[5]==board[8] and board[2]!=' ':
        Game=Win
    elif board[3]==board[6] and board[6]==board[9] and board[3]!=' ':
        Game=Win
    elif board[1]==board[5] and board[5]==board[9] and board[1]!=' ':
        Game=Win
    elif board[3]==board[5] and board[5]==board[7] and board[3]!=' ':
        Game=Win
    elif board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' ':
        Game=Draw
    else:
        Game=Running

print ("Player 1[X] --- Player 2[O]\n\n\n")
print("Please wait...")
time.sleep(2)
while Game==Running:
    os.system('clear')
    DrawBoard()
    if player%2!=0:
        print("Player 1's chance")
        Mark='X'
    else:
        print("Player 2's chance")
        Mark='O'
    choice=int(input("Enter the position between[1-9]where you want to mark: "))
    if CheckPosition(choice):
        board[choice]=Mark
        player+=1
        CheckWin()
        
    os.system('clear')
    DrawBoard()
    if Game==Draw:
        print("Game Draw!")
    elif Game==Win:
        player -=1
        if player%2!=0:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")