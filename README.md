# AIGamePlayingAgent
A board game which takes the current state of the board as the input and gives the best possible next movie for a given depth. 
Alpha beta pruning is incorporated to improve the efficiency of the program which improved the depth of search of the game agent.

Input and output formats:

Input: 

<N>
<MODE>
<YOUPLAY>
<DEPTH>
<… CELL VALUES …>
<… BOARD STATE …>
where
<N> is the board width and height, e.g., N=5 for the 5x5 board shown in the figures above. N is an integer
strictly greater than 0 and smaller than or equal to 26.
<MODE> is “MINIMAX” or “ALPHABETA” or “COMPETITION”.
<YOUPLAY> is either “X” or “O” and is the player which you will play on this turn.
<DEPTH> is the depth of your search. By convention, the root of the search tree is at depth 0. DEPTH will
always be larger than or equal to 1.
<… CELL VALUES …> contains N lines with, in each line, N positive integer numbers each separated by a single
space. These numbers represent the value of each location.
<… BOARD STATE …> contains N lines, each with N characters “X” or ”O” or “.” to represent the state of each
cell as occupied by X, occupied by O, or free.



output:

<MOVE> <MOVETYPE>
<… NEXT BOARD STATE …>
where
<MOVE> is your move. As in the figures above, we use capital letters for column and numbers for rows. An
example move is “F22” (remember that N is from 1 to 26, see above).
<MOVETYPE> is “Stake” or “Raid” and is the type of move that your <MOVE> is.
<… NEXT BOARD STATE …> a description of the new board state after you have played your move. Same
format as <… BOARD STATE …> in input.txt above.



sample input format:
5
ALPHABETA
O
5
1 1 8 1 1
1 1 8 1 1
8 8 8 8 8
1 1 8 1 1
1 1 8 1 1
..X..
..O..
X....
.....
.....

sample output:
B3 Stake
..X..
..O..
XO...
.....
.....
