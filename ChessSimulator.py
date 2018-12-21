#ChessSimulator

#There is a bug in python 2.7, the type of your class objects 
#will always be instance not the class itself. 
#This will work in 3.6.5. 

class Pawn:
    def __init__(self, color, position, num, beginning):
        self.color=color; #gonna be a string 'white' or 'black'
        self.position=position; #list in the format [row, col]
        self.num=num; #pawn number, there are 8 of them. 
        self.beginning=beginning; #this is a variable to see if the pawn hasn't
#moved yet because if it hasn't then it can move 2 spaces. If it has it can
#only move one.

    def move(self,x):
        if(self.beginning==True): 
            if(x in range(0,8) and canMove(board,self,x)): 
                self.position=x; 
            else: 
                return "Illegal Move" 
        else: 
            if(x in range(0,8) and canMove(board,self,x)): 
                self.position=x; 
            else: 
                return "Illegal Move" 
    
    #method to identify what type the object is because python27 is being retarded... 
    def identify(self): 
        return "Pawn"  
    #method to identify the specific pawn
    def ID(self):
        return "Pawn {}".format(self.num)
    
    #adding repr and str methods
    def __repr__(self):
        return "Pawn {}, {}, {}, {}".format(self.color, self.position, self.num, self.beginning)
    def __str__(self):
        return "Pawn {}, {}".format(self.color, self.num)
        
#################################################################################
class Rook: 
    def __init__(self, color, position, num): 
        self.color=color; 
        self.position=position; 
        self.num=num; 
    
    #move method (can move any number of steps till the length of the board 
#either in any direction horizontally or vertically) 
    #x is gonna be a position [x,y]
    def move(self,x): 
        if(x[0] in range(0,8) and x[1] in range(0,8) and canMove(board,self,x)==True): 
            self.position=x
        else: 
            return "Illegal Move" 
    
    #method to identify the type of this object; will return the string "Rook" because python27 is being retarded. 
    def identify(self): 
        return "Rook" 

    def ID(self):
        return "Rook {}".format(self.num)
    
    #repr and str methods 
    def __repr__(): 
        return "Rook {}, {}, {}".format(self.color, self.position, self.num)
    
    def __str__(): 
        return "Rook {}, {}".format(self.color, self.num); 
        
######################################################################
class Bishop: 
    def __init__(self,color,position,num): 
        self.color=color; 
        self.position=position; 
        self.num=num; 
    
    #now these things can move diagonally (same x down or up, left or right); these snickerdoodles can ONLY move diagonally. 
    def move(self,x): 
        if(x[0] in range(0,8) and x[1] in range(0,8) and canMove(board,self,x)==True): 
            self.position=x
        else: 
            return "Illegal Move" 
    
    #method to identify what object it is 
    def identify(self): 
        return "Bishop"

    def ID(self):
        return "Bishop {}".format(self.num)
    
    #repr and str methods 
    def __repr__(): 
        return "Bishop {}, {}, {}".format(self.color,self.position,self.num)
    def __str__(): 
        return "Bishop {}, {}".format(self.color,self.num)

############################################################################
class Knight: 
    def __init__(self,color,position,num): 
        self.color=color
        self.position=position
        self.num=num
    
    def move(self,x): 
        if(x[0] in range(0,8) and x[1] in range(0,8) and canMove(board,self,x)==True): 
            self.position=x; 
        else: 
            return "Illegal Move"
    
    def identify(self): 
        return "Knight"

    def ID(self):
        return "Knight {}".format(self.num)
    
    #repr and str methods 
    def __repr__(): 
        return "Knight {}, {}, {}".format(self.color,self.position,self.num) 
    def __str__(): 
        return "Knight {}, {}".format(self.color, self.num) 
        
##########################################################################################
class Queen: 
    def __init__(self,color,position,num): 
        self.color=color
        self.position=position
        self.num=num; 
        
    def move(self,x): 
        if(x[0] in range(0,8) and x[1] in range(0,8) and canMove(board,self,x)==True): 
            self.position=x
        else: 
            return "Illegal Move" 
    
    def identify(self): 
        return "Queen" 

    def ID(self):
        return "Queen {}".format(self.num);
    
    #repr and str methods 
    def __repr__(): 
        return "Queen {}, {}".format(self.color,self.position) 
    def __str__(): 
        return "Queen {}".format(self.color) 

#########################################################################
class King: 
    def __init__(self,color,position,num): 
        self.color=color
        self.position=position
        self.num=num
        
    def move(self,x): 
        if(x[0] in range(0,8) and x[1] in range(0,8) and canMove(board,self,x)==True): 
            self.position=x
        else: 
            return "Illegal Move" 
    
    def identify(self): 
        return "King" 

    def ID(self):
        return "King {}".format(self.num)
    
    #str and repr methods 
    def __repr__(): 
        return "King {}, {}".format(self.color,self.position)
    def __str__(): 
        return "King {}".format(self.color)
        
##############################################################
#Creates an 8x8 board, as a nested list, with "X"s in all of them. 
def createBoard():
    board=[]
    for i in range(8):
        a=["X" for j in range(8)]
        board.append(a)
    return board

###################################################################################
#Creating all the pieces... 

#Black pieces 

#Pawns 
p1=Pawn('black',[1,0],1,True)
p2=Pawn('black',[1,1],2,True) 
p3=Pawn('black',[1,2],3,True) 
p4=Pawn('black',[1,3],4,True) 
p5=Pawn('black',[1,4],5,True)
p6=Pawn('black',[1,5],6,True) 
p7=Pawn('black',[1,6],7,True)
p8=Pawn('black',[1,7],8,True)

#Rooks 
r1=Rook('black',[0,0],1)
r2=Rook('black',[0,7],2) 

#Knights 
k1=Knight('black',[0,1],1)
k2=Knight('black',[0,6],2)

#Bishops 
b1=Bishop('black',[0,2],1)
b2=Bishop('black',[0,5],2) 

#King 
K1=King('black',[0,3],1)

#Queen 
q1=Queen('black',[0,4],1)

#White pieces 

#Pawns
p9=Pawn('white',[6,0],9,True)
p10=Pawn('white',[6,1],10,True)
p11=Pawn('white',[6,2],11,True)
p12=Pawn('white',[6,3],12,True)
p13=Pawn('white',[6,4],13,True)
p14=Pawn('white',[6,5],14,True)
p15=Pawn('white',[6,6],15,True)
p16=Pawn('white',[6,7],16,True) 

#Rooks 
r3=Rook('white',[7,0],3)
r4=Rook('white',[7,7],4)

#Knights 
k3=Knight('white',[7,1],3)
k4=Knight('white',[7,6],4) 

#Bishops 
b3=Bishop('white',[7,2],3)
b4=Bishop('white',[7,5],4) 

#King
K2=King('white',[7,4],2)

#Queen
q2=Queen('white',[7,3],2)

#########################################################################################
#Function setupBoard() 
#This will modify the board to have representations of all the little pieces on the board
#when the game starts. 
def setupBoard(board): 
    # test in python 3 to make sure you can make a lsit of objects and is rep correctly. 
    '''Method to set up the board to make sure the canMOve method can work'''
    #pawns 
    board[p1.position[0]][p1.position[1]]=p1.ID();
    board[p2.position[0]][p2.position[1]]=p2.ID();
    board[p3.position[0]][p3.position[1]]=p3.ID();
    board[p4.position[0]][p4.position[1]]=p4.ID();
    board[p5.position[0]][p5.position[1]]=p5.ID();
    board[p6.position[0]][p6.position[1]]=p6.ID();
    board[p7.position[0]][p7.position[1]]=p7.ID();
    board[p8.position[0]][p8.position[1]]=p8.ID();
    board[p9.position[0]][p9.position[1]]=p9.ID();
    board[p10.position[0]][p10.position[1]]=p10.ID();
    board[p11.position[0]][p11.position[1]]=p11.ID();
    board[p12.position[0]][p12.position[1]]=p12.ID();
    board[p13.position[0]][p13.position[1]]=p13.ID();
    board[p14.position[0]][p14.position[1]]=p14.ID();
    board[p15.position[0]][p15.position[1]]=p15.ID();
    board[p16.position[0]][p16.position[1]]=p16.ID();

    #rooks 1-4
    board[r1.position[0]][r1.position[1]]=r1.ID();
    board[r2.position[0]][r2.position[1]]=r2.ID();
    board[r3.position[0]][r3.position[1]]=r3.ID();
    board[r4.position[0]][r4.position[1]]=r4.ID();

    #bishops
    board[b1.position[0]][b1.position[1]]=b1.ID();
    board[b2.position[0]][b2.position[1]]=b2.ID();
    board[b3.position[0]][b3.position[1]]=b3.ID();
    board[b4.position[0]][b4.position[1]]=b4.ID();

    #knights
    board[k1.position[0]][k1.position[1]]=k1.ID();
    board[k2.position[0]][k2.position[1]]=k2.ID();
    board[k3.position[0]][k3.position[1]]=k3.ID();
    board[k4.position[0]][k4.position[1]]=k4.ID();

    #queens
    board[q1.position[0]][q1.position[1]]=q1.ID();
    board[q2.position[0]][q2.position[1]]=q2.ID();

    #kings
    board[K1.position[0]][K1.position[1]]=K1.ID();
    board[K2.position[0]][K2.position[1]]=K2.ID(); 
    
###########################################################################################################################################################################################################
#Creates the a grid of all the positions a piece can move to.
#One bug, is that for pawns self.beginning is always true because there is nothing to 
#take care of the case when it is false. 
def createOptionsGrid(board, obj):
    '''The whole goal is to create a list of lists of positions of which each
piece can move to. .identify() method is used to identify the type of object and the various
if statements are used to plot which pieces can move where. BUT this function should
also recognize that if a piece is in the way of a person's movement that pieces other than
than knights, then all those options up to the piece blocking should be removed.
To give an example of this if there is a piece blocking the pawn that is of the same color
that is right in front of it (ie, pawn is at [0,0] and there is a white piece at [1,0]) then
that pawn has no moves. But because of that funciton will be taken upon in another function'''
    options=[]
    #For Pawns
    if(obj.identify()=="Pawn"):
        #print("here") 
        #if beginning is True, then they can move a max of two steps.
        if(obj.beginning==True):
            #print("here")
            #need to add here if pawns are numbers 9-16 then they move backwards.
            if(9<=obj.num<=16):
                #moving backwards for pawns 9-16
                for i in range(1,3):
                    if(canMove(board,obj,[obj.position[0]-i,obj.position[1]])):
                        if(checkOptions(obj,[obj.position[0]-i,obj.position[1]])):
                            options.append([obj.position[0]-i,obj.position[1]])
                return options
            else:
                for i in range(1,3):
                    if( canMove(board,obj,[obj.position[0]+i,obj.position[1]])):
                        if(checkOptions(obj,[obj.position[0]+i,obj.position[1]])):
                            options.append([obj.position[0]+i, obj.position[1]])
                return options
            #code can be simplified in one line: return([obj.position[0]+i,obj.position[1] for i in range(3) if obj.position[0]+i<len(board) and canMove(board,obj,position)])
        else:
            if(9<=obj.num<=16):
                for i in range(1,2):
                    if(canMove(board,obj,[obj.position[0]-i,obj.position[1]])):
                        if(checkOptions(obj,[obj.position[0]-i,obj.position[1]])):
                            options.append([obj.position[0]-i,obj.position[1]])
            else: 
                for i in range(1,2):
                    if(obj.position[0]+i<len(board)):
                        options.append([obj.position[0]+i,obj.position[1]])
            #can be simplified in one line: return ([obj.position[0]+i for i in range(2) if obj.position[0]+i<len(board)])
            return options
    #Rooks 
    if(obj.identify()=="Rook"): 
        #rooks can move any direction from their position up to the length of the direction in a vertical or horizontal fashion. 
        #vertical - increasing 
        for i in range(1,len(board)):
            if(0<=obj.position[0]<len(board) and obj.position[0]+i in range(len(board)) and obj.position[1] in range(len(board))): 
                if(canMove(board,obj,[obj.position[0]+i,obj.position[1]])):
                    if(checkOptions(obj,[obj.position[0]+i,obj.position[1]])):
                    #print("here"); #debugging
                        options.append([obj.position[0]+i,obj.position[1]])
                    else:
                        break
                else:
                    break
            else:
                break
        #vertical - decreasing
        for i in range(1,len(board)):
            if(0<=obj.position[0]<len(board) and obj.position[0]-i in range(len(board))):
                if(canMove(board,obj,[obj.position[0]-i,obj.position[1]])):
                    if(checkOptions(obj,[obj.position[0]-i,obj.position[1]])):
                        options.append([obj.position[0]-i,obj.position[1]])
                    else:
                        break
                else:
                    break
            else:
                break
        #print(options)
        #horizontal - increasing 
        for i in range(1,len(board)):
            if(0<=obj.position[0]<len(board) and 0<=obj.position[1]+i<len(board)):
                if(canMove(board,obj,[obj.position[0],obj.position[1]+i])):
                    if(checkOptions(obj,[obj.position[0],obj.position[1]+i])):
                    #print("here") #debugging 
                        options.append([obj.position[0],obj.position[1]+i])
                    else:
                        break
                else:
                    break
            else:
                break
        #horizontal - decreasing
        for i in range(1,len(board)):
            if(obj.position[0] in range(len(board)) and obj.position[1]-i in range(len(board))):
                if(canMove(board,obj,[obj.position[0],obj.position[1]-i])):
                    if(checkOptions(obj,[obj.position[0],obj.position[1]-i])):
                        options.append([obj.position[0],obj.position[1]-i])
                    else:
                        break
                else:
                    break
            else:
                break
                        
                        
        return options 
        #this code in one line: return([[obj.position[0]+i,obj.position[1]] for i in range(len(board))] + [[obj.position[0],obj.position[1]] for i in range(len(board))])
        
    #Bishops
    if(obj.identify()=="Bishop"): 
        #increasing in both directions 
        for i in range(1,len(board)):
            if(obj.position[0]+i in range(len(board)) and obj.position[1]+i in range(len(board))): 
                if(canMove(board,obj,[obj.position[0]+i,obj.position[1]+i])):
                    if(checkOptions(obj,[obj.position[0]+i,obj.position[1]+i])):
                        options.append([obj.position[0]+i,obj.position[1]+i])
                    else:
                        break
                else:
                    break
            else:
                break 
        #increasing in rows and decreasing in cols. 
        for i in range(1,len(board)):
            if(obj.position[0]+i in range(len(board)) and obj.position[1]-i in range(len(board))): 
                if(canMove(board,obj,[obj.position[0]+i,obj.position[1]-i])):
                    if(checkOptions(obj,[obj.position[0]+i,obj.position[1]-i])):
                        options.append([obj.position[0]+i,obj.position[1]-i])
                    else:
                        break
                else:
                    break
            else:
                break 
        #decreasing in rows and increasing in cols 
        for i in range(1,len(board)):
            if(obj.position[0]-i in range(len(board)) and obj.position[1]+i in range(len(board))): 
                if(canMove(board,obj,[obj.position[0]-i,obj.position[1]+i])):
                    if(checkOptions(obj,[obj.position[0]-i,obj.position[1]+i])):
                        options.append([obj.position[0]-i,obj.position[1]+i])
                    else:
                        break
                else:
                    break
            else:
                break
        #decreasing in rows and decreasing in cols 
        for i in range(1,len(board)):
            if(obj.position[0]-i in range(len(board)) and obj.position[1]-i in range(len(board))):
                if(canMove(board,obj,[obj.position[0]-i,obj.position[1]-i])):
                    if(checkOptions(obj,[obj.position[0]-i,obj.position[1]-i])):
                        options.append([obj.position[0]-i,obj.position[1]-i])
                    else:
                        break
                else:
                    break
            else:
                break
            
        return options 
        
        #this code in one line: return([[obj.position[0]+i,obj.position[1]+i] for i in range(len(board))]+[[obj.position[0]+i,obj.position[1]-i] for i in range(len(board))]+[[obj.position[0]-i,obj.position[1]+i] for i in range(len(board))]+[[obj.position[0]-i,obj.position[1]-i] for i in range(len(board))])
    
    #Knights 
    if(obj.identify()=="Knight"): 
        '''The knight can move 2 in any direction (up, down, left or right), then one on the opposite axis, if it moves in the row then it goes +/- 1 via the cols; Those are the options from its positions. 
        NOTE: It can't move up to 2, it moves 2 in any direction and then +/- 1, those are the options''' 
         
        if(obj.position[0]+2 in range(len(board)) and obj.position[1]+1 in range(len(board))):
            if(canMove(board,obj,[obj.position[0]+2,obj.position[1]+1])):
                if(checkOptions(obj,[obj.position[0]+2,obj.position[1]+1])):
                    options.extend([[obj.position[0]+2,obj.position[1]+1]])
                            
        if(obj.position[0]+2 in range(len(board)) and obj.position[1]-1 in range(len(board))):  
            if(canMove(board,obj,[obj.position[0]+2,obj.position[1]-1])):
                if(checkOptions(obj,[obj.position[0]+2,obj.position[1]-1])
                   ):
                    options.extend([[obj.position[0]+2,obj.position[1]-1]])
                
                         
        if(obj.position[0]-2 in range(len(board)) and obj.position[1]+1):
            if(canMove(board,obj,[obj.position[0]-2,obj.position[1]+1])):
                if(checkOptions(obj,[obj.position[0]-2,obj.position[1]+1])
                   ):
                    options.extend([[obj.position[0]-2,obj.position[1]+1]])
                
                            
        if(obj.position[0]-2 in range(len(board)) and obj.position[1]-1 in range(len(board))):    
            if(canMove(board,obj,[obj.position[0]-2,obj.position[1]-1])):
                if(checkOptions(obj,[obj.position[0]-2,obj.position[1]-1])
                   ):
                    options.extend([[obj.position[0]-2,obj.position[1]-1]])
                
                
                  
        if(obj.position[0]+1 in range(len(board)) and obj.position[1]+2 in range(len(board))):
            if(canMove(board,obj,[obj.position[0]+1,obj.position[1]+2])):
                if(checkOptions(obj,[obj.position[0]+1,obj.position[1]+2])
                   ):
                    options.extend([[obj.position[0]+1,obj.position[1]+2]])
                
                
                   
        if(obj.position[0]-1 in range(len(board)) and obj.position[1]+2 in range(len(board))):   
            if(canMove(board,obj,[obj.position[0]-1,obj.position[1]+2])):
                if(checkOptions(obj,[obj.position[0]-1,obj.position[1]+2])
                   ):
                    options.extend([[obj.position[0]-1,obj.position[1]+2]])
                

              
        if(obj.position[0]+1 in range(len(board)) and obj.position[1]-2 in range(len(board))):
            if(canMove(board,obj,[obj.position[0]+1,obj.position[1]-2])):
                if(checkOptions(obj,[obj.position[0]+1,obj.position[1]-2])
                   ):
                    options.extend([[obj.position[0]+1,obj.position[1]-2]])
                
                
               
        if(obj.position[0]-1 in range(len(board)) and obj.position[1]-2 in range(len(board))):   
            if(canMove(board,obj,[obj.position[0]-1,obj.position[1]-2])):
                if(checkOptions(obj,[obj.position[0]-1,obj.position[1]-2])):
                    options.extend([[obj.position[0]-1,obj.position[1]-2]])
                
               
        
        return options; 
        #hardcoding is bad form, but your runtime is O(1) so can't complain... 
        
    #Queens 
    if(obj.identify()=='Queen'): 
        '''Queens can move literally in any direction any number of steps so they're like a combo of bishops and rooks.''' 
        #moving diagonally... 
        for i in range(1,len(board)):
            if(obj.position[0]+i in range(len(board)) and obj.position[1]+i in range(len(board))):
                if(canMove(board,obj,[obj.position[0]+i,obj.position[1]+i])):
                    if(checkOptions(obj,[obj.position[0]+i,obj.position[1]+i])):
                        options.append([obj.position[0]+i,obj.position[1]+i])
                    else:
                        break
                else:
                    break
            else:
                break
                        
        #increasing in rows and decreasing in cols. 
        for i in range(1,len(board)):
            if(obj.position[0]+i in range(len(board)) and obj.position[1]-i in range(len(board))):
                if(canMove(board,obj,[obj.position[0]+i,obj.position[1]-i])):
                    if(checkOptions(obj,[obj.position[0]+i,obj.position[1]-i])):
                        options.append([obj.position[0]+i,obj.position[1]-i])
                    else:
                        break
                else:
                    break
            else:
                break
                        
        #decreasing in rows and increasing in cols 
        for i in range(1,len(board)):
            if(obj.position[0]-i in range(len(board)) and obj.position[1]+i in range(len(board))):
                if(canMove(board,obj,[obj.position[0]-i,obj.position[1]+i])):
                    if(checkOptions(obj,[obj.position[0]-i,obj.position[1]+i])):
                        options.append([obj.position[0]-i,obj.position[1]+i])
                    else:
                        break
                else:
                    break
            else:
                break
        #decreasing in rows and decreasing in cols 
        for i in range(1,len(board)):
            if(obj.position[0]-i in range(len(board)) and obj.position[1]-i in range(len(board))):
                if(canMove(board,obj,[obj.position[0]-i,obj.position[1]-i])):
                    if(checkOptions(obj,[obj.position[0]-i,obj.position[1]-i])):
                        options.append([obj.position[0]-i,obj.position[1]-i])
                    else:
                        break
                else:
                    break
            else:
                break
                        
        #moving horizontally&&vertically 
        #horizontal 
        for i in range(1,len(board)):
            if(obj.position[0]+i in range(len(board)) and obj.position[1] in range(len(board))):
                if(canMove(board,obj,[obj.position[0]+i,obj.position[1]])):
                    if(checkOptions(obj,[obj.position[0]+i,obj.position[1]])):
                        options.append([obj.position[0]+i,obj.position[1]])
                    else:
                        break
                else:
                    break
            else:
                break
                        
        #vertical 
        for i in range(1,len(board)):
            if(obj.position[0] in range(len(board)) and obj.position[1]+i in range(len(board))):
                if(canMove(board,obj,[obj.position[0],obj.position[1]+i])):
                    if(checkOptions(obj,[obj.position[0],obj.position[1]+i])):
                        options.append([obj.position[0],obj.position[1]+i])
                    else:
                        break
                else:
                    break
            else:
                break
        return options 
        #can be put in one line, with just one long ass concatenation --- w/ three if statements might be a bit tricky.
    
    #Kings 
    if(obj.identify()=="King"): 
        '''Kings can move one step in any direction so basically queens but just to 1''' 
        if(obj.position[0]+1 in range(len(board))):
            if(canMove(board,obj,[obj.position[0]+1,obj.position[1]])):
                if(checkOptions(obj,[obj.position[0]+1,obj.position[1]])):
                    options.append([obj.position[0]+1,obj.position[1]])
        
        if(obj.position[1]+1 in range(len(board))):
            if(canMove(board,obj,[obj.position[0],obj.position[1]+1])):
                if(checkOptions(obj,[obj.position[0],obj.position[1]+1])):
                    options.append([obj.position[0],obj.position[1]+1])
                    
        if(obj.position[0]-1 in range(len(board))):
            if(canMove(board,obj,[obj.position[0]-1,obj.position[1]])):
                if(checkOptions(obj,[obj.position[0]-1,obj.position[1]])):
                    options.append([obj.position[0]-1,obj.position[1]])
                    
        if(obj.position[1]-1 in range(len(board))): 
            if(canMove(board,obj,[obj.position[0],obj.position[1]-1])):
                if(checkOptions(obj,[obj.position[0],obj.position[1]-1])):
                    options.append([obj.position[0],obj.position[1]-1])
                    
        if(obj.position[0]+1 in range(len(board)) and obj.position[1]+1 in range(len(board))):
            if(canMove(board,obj,[obj.position[0]+1,obj.position[1]+1])):
                if(checkOptions(obj,[obj.position[0]+1,obj.position[1]+1])):
                    options.append([obj.position[0]+1,obj.position[1]+1])
                    
        if(obj.position[0]+1 in range(len(board)) and obj.position[1]-1 in range(len(board))):
            if(canMove(board,obj,[obj.position[0]+1,obj.position[1]-1])):
                if(checkOptions(obj,[obj.position[0]+1,obj.position[1]-1])):
                    options.append([obj.position[0]+1,obj.position[1]-1])
            
        if(obj.position[0]-1 in range(len(board)) and obj.position[1]+1 in range(len(board))):
            if(canMove(board,obj,[obj.position[0]-1,obj.position[1]+1])):
                if(checkOptions(obj,[obj.position[0]-1,obj.position[1]+1])):
                    options.append([obj.position[0]-1,obj.position[1]+1])
                    
        if(obj.position[0]-1 in range(len(board)) and obj.position[1]-1 in range(len(board))):
            if(canMove(board,obj,[obj.position[0]-1,obj.position[1]-1])):
                if(checkOptions(obj,[obj.position[0]-1,obj.position[1]-1])):
                    options.append([obj.position[0]-1,obj.position[1]-1])
        return options; 
        
###########################################################################################################
#Checking to see if there is a piece at the given location; returns true if that piece can move there.
def canMove(board, obj, position):
    if(board[position[0]][position[1]]=="X" and 0<=position[0]<len(board) and 0<=position[1]<len(board)):
        return True
    else:
        return False

#####################################################################
#Need to create a function called playable that cycles through all the pieces
#options grid so to speak and makes a dictionary and then in that dicitonary
#returns what pieces can move.
def createDict():
    a=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,r1,r2,r3,r4,k1,k2,k3,k4,b1,b2,b3,b4,q1,q2,K1,K2]
    d=dict()
    for element in a:
        try:
           d[element.ID()]=createOptionsGrid(board,element)
        except:
            print(element.ID())
    return d 
#####################################################################
#function to check options to make sure all are correct and pieces of the
#same color can't move to other pieces of the same color.
#will return boolean value, and instead of removing the options
def checkOptions(obj,position):
    #where d is the dictionary created by createDict()
    #the obj is the object whose options we are editing
    bp=[p1,p2,p3,p4,p5,p6,p7,p8,r1,r2,b1,b2,k1,k2,K1,q1]
    wp=[p9,p10,p11,p12,p13,p14,p15,p16,r3,r4,b3,b4,k3,k4,K2,q2]
    #need to return a boolean value to see if there are any pieces of the same
    #color, in that position
    if(obj.color=='white'):
        pos=[element.position for element in wp]
    else:
        pos=[element.position for element in bp]
    return(any([element!=position for element in pos]))
    
###################################################################
#function to return a boolean value true or false to see if a piece
#given its option list if obj1 can capture obj2. 
def canCapture(d,obj):
    #where d is the dictionary created by createDict() and obj is the
    #object whose options we will explore to see if there are any other options
    #out there...
    #will return T/F value if obj can capture any piece of the opposite color.
    #should also return what piece can be captured and what position it can
    #be captured.
    a=[]
    if(obj.color=='white'):
        p=[(element,element.position) for element in bp]
    else:
        p=[(element,element.position) for element in wp]
    #p is a list of the obj's opposite color pieces and their positions
    #need to check if d[obj] any of those positions are in p.
    for element in d[obj.identify()+" "+str(obj.num)]:
        for item in p:
            if(element in item):
                a.append((True,item[0],item[1]))
    if(len(a)==0):
        return False
    else:
        return a
######################################################################
#function to display the board in a more seeable manner
def displayBoard(board):
    for element in board:
        print(element)
####################################################################
#function that returns a T/F value to determine if that piece has moved
def hasMoved(current,previous):
    #previous is the previous position that the piece has moved.
    return(current!=previous) 
#######################################################################
#Testing
board=createBoard()
setupBoard(board)
bp=[p1,p2,p3,p4,p5,p6,p7,p8,r1,r2,b1,b2,k1,k2,K1,q1] #list of black pieces 
wp=[p9,p10,p11,p12,p13,p14,p15,p16,r3,r4,b3,b4,k3,k4,K2,q2] #list of white pieces
#print(createOptionsGrid(board,p1))
pieces=bp+wp #list of all the pieces 

#############################################################################
#Main function, play(), 
#simulates a game of chess...
import random
def play():
    board=createBoard()
    setupBoard(board);
    turn=0 #counter indicating what turn it is;
    #if it is zero and an even number then its whites turn; other than that its
    #blacks turn
    keepGoing=True #variable to tell if the infinite loop should keep going
    options=createDict()
    #need to account for capturing!!!! 
    while(keepGoing):
        options=createDict() #need this inside the loop to keep being updated
    #white turn, pick a piece that can play, get the options grid, and choose a position and play... 
        print("White's Turn!")
        if(turn==0 or turn%2==0):
            piece=wp[random.randint(0,len(wp)-1)] #piece that we're going to move.
            previous=[piece.position[0],piece.position[1]] #previous position of piece
            position=options[piece.identify()+" "+str(piece.num)][random.randint(0,len(
                options[piece.identify()+" "+str(piece.num)]))]
            #check to see if the piece has moved --- need to loop through this.
            while(hasMoved(position,previous)==False or position==[]):
                position=options[piece.identify()+" "+str(piece.num)][
                    random.randint(0,len(options[piece.identify()+ " " + str(
                        piece.num)]))]
            #check, if position that the piece is going to move to has another piece
            #in which it can, capture...
            if(canCapture(options,piece)!=False):
                #now initilaiate capture sequence
                #canCapture when not false returns tuple (True,piece,position), which
                #is basically a list of these tuples...

                #checking to see if the position chosen is a capturable position by
                #the piece. 
                positions=[element[2] for element in canCapture(options,piece)]
                pieces=[element[1] for element in canCapture(options,piece)]
                if(position in positions):
                    #meaning if the position is going to capture the piece...
                    board[position[0]][position[1]]=piece.identify()+" "+piece.num
                    print("{} captured {}!".format(piece.identify() + " " +piece.num,
                                                   pieces[positions.index(position)]))
            piece.move(position)
            #now that the move() method has been invoked, you must adjust the board.
            board[piece.position[0]][piece.position[1]]=piece.identify()+" "+piece.num
            board[previous[0]][previous[1]]="X"
            displayBoard(board) 
    #black turn 
        else:
            print("Black's Turn")
            piece=bp[random.randint(0,len(bp)-1)]
            previous=[piece.position[0],piece.position[1]]
            position=options[piece.identify()+" "+piece.num][random.randint(0,
                                                len(options[piece.identify()+
                                                            " "+piece.num]))]
            while(hasMoved(position,previous)==False or position==[]):
                position=options[piece.identify()+" "+str(piece.num)][
                    random.randint(0,len(options[piece.identify()+ " " + str(
                        piece.num)]))]
            if(canCapture(options,piece)!= False):
                positions=[element[2] for element in canCapture(options,piece)]
                pieces=[element[1] for element in canCapture(options,piece)]
                if(position in positions):
                    board[position[0]][position[1]]=piece.identify() + " "+piece.num
                    print("{} captured {}!".format(piece.identify()+" "+piece.num,
                                                   pieces[positions.index(position)])
                          )
            piece.move(position)
            board[position[0]][position[1]]=piece.identify()+" " + piece.num
            board[previous[0]][previoius[1]]="X"
            displayBoard(board)

        turn=turn+1

        
    
        #keep going and have end conditions.
        #so for the end conditions, the King of both colors --- their options must
        #all be options of pieces of the opposite color!!!
        
        #I need to check to see if those positions are occupied by any other
        #piece of the OPPOSITE COLOR...
        #condition1 contains all the positions of the king  
        #K1 is black, so we search all the white pieces...
        
        c1=all([pos in options["King 1"] for p in wp for pos in options[
            p.identify()+" "+str(p.num)]])
        c2=all([pos in options["King 2"] for p in bp for pos in options[
            p.identify()+" "+str(p.num)]])
        if(c1==True and c2==True):
            keepGoing=False
    if(turn%2==0):
        print("White won game!")
    else:
        print("Black won game!")
    displayBoard(board) 
    
