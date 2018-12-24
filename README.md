# ChessSimulator

Goal of this is to create a computer simulation of the game chess. 
The approach I've taken is that all pieces are objects, and the board is simply a method of displaying where everything 
is, at a certain moment. 

For the computer simulation portion, it is fueled via createOptionsGrid() a method that will return a list of lists within python
which are positions in which that particular piece can go to. The createDict() method is a function where it returns a dictionary
of the optionGrid of all pieces the chess board. 

The play() is the main function and simulates a game of chess. 

Bugs to address: The board isn't displaying properly. Some pieces appear more than once, and other pieces that are still alive on the 
board are just being written off as Xs. 

Further implementation: Need to implement stalemate function for rooks. As well as a gui using tkinter for user playing chess. 

@author Rohan Gupta 
