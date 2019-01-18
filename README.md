# ChessSimulator

Goal of this is to create a computer simulation of the game chess. 
The approach I've taken is that all pieces are objects, and the board is simply a method of displaying where everything 
is, at a certain moment. 

For the computer simulation portion, it is fueled via createOptionsGrid() a method that will return a list of lists within python
which are positions in which that particular piece can go to. The createDict() method is a function where it returns a dictionary
of the optionGrid of all pieces the chess board. 

The play() is the main function and simulates a game of chess. 

Its all text based, however castling has not been implemented for rooks. 

@author Rohan Gupta 
