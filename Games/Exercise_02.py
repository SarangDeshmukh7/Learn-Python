'''
Time for some fake graphics! Let’s say we want to draw game boards
that look like this:
 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many
other sizes (8x8 for chess, 19x19 for Go, and many more).
Ask the user what size game board they want to draw, and draw it
for them to the screen using Python’s print statement.
'''

# Solution
def draw_board(size):
    """
    Draw game boards in size of 'size'.
    Arguments:
    size -- the size of the board.
    
    """
    h_element = ' ---'
    v_element = '|   '
    for i in range(size):
        print(h_element * (size))
        print(v_element * (size+1))
    print(h_element * (size))
    
        
def main():
    draw_board(int(input('Please input the size of board:')))
    
if __name__ == "__main__":
    main()

# Test Part
# >>> %Run test.py
# Please input the size of board:4
#  --- --- --- ---
# |   |   |   |   |   
#  --- --- --- ---
# |   |   |   |   |   
#  --- --- --- ---
# |   |   |   |   |   
#  --- --- --- ---
# |   |   |   |   |   
#  --- --- --- ---
