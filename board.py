
import random


from circle import draw_circle
from pixel import draw_pixel
from cell import Cell
from number import Number

class Board:
    def __init__(self, dim_size, num_bombs,width):
        # let's keep track of these parameters. they'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.width = width
        # let's create the board
        # helper function!
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()
        self.isSafe = True
        
        # initialize a set to keep track of which locations we've uncovered
        # we'll save (row,col) tuples into this set 
        self.dug = set() # if we dig at 0, 0, then self.dug = {(0,0)}
        self.visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        self.cell_size = self.width//self.dim_size
        self.isWon = False
    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here (or whatever representation you prefer,
        # but since we have a 2-D board, list of lists is most natural)

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None, ..., None],
        #  [None, None, ..., None],
        #  [...                  ],
        #  [None, None, ..., None]]
        # we can see how this represents a board!

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) # return a random integer N such that a <= N <= b
            row = loc // self.dim_size  # we want the number of times dim_size goes into loc to tell us what row to look at
            col = loc % self.dim_size  # we want the remainder to tell us what index in that row to look at

            if board[row][col] == '*':
                # this means we've actually planted a bomb there already so keep going
                continue

            board[row][col] = '*' # plant the bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # now that we have the bombs planted, let's assign a number 0-8 for all the empty spaces, which
        # represents how many neighboring bombs there are. we can precompute these and it'll save us some
        # effort checking what's around the board later on :)
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        # make sure to not go out of bounds!

        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at that location!
        # return True if successful dig, False if bomb dug

        # a few scenarios:
        # hit a bomb -> game over
        # dig at location with neighboring bombs -> finish dig
        # dig at location with no neighboring bombs -> recursively dig neighbors!

        self.dug.add((row, col)) # keep track that we dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue # don't dig where you've already dug
                self.dig(r, c)

        # if our initial dig didn't hit a bomb, we *shouldn't* hit a bomb here
        return True

    def renderBoard(self):
        cell_size = self.cell_size
        if(self.isSafe is not True):
            print("game over, revealing board")
            self.dug = set([(r,c) for r in range(self.dim_size) for c in range(self.dim_size)])
        elif ((len(self.dug) == self.dim_size ** 2 - self.num_bombs) and self.isSafe):
            print("You Won")
            self.isWon = True
            



        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    self.visible_board[row][col] = str(self.board[row][col])
                else:
                    self.visible_board[row][col] = 'hidden'

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                self.draw_cell(row*cell_size,col*cell_size,cell_size,val=self.visible_board[row][col])

    def draw_cell(self,x,y,cell_size,val):
            if val == "hidden":
                draw_pixel(x+cell_size//2,y+cell_size//2,size=cell_size-5,lineColor=[0.5,0.5,0.5])
            elif val == "*":
                draw_circle(cell_size//2, x+cell_size//2, y+cell_size//2, color=[1.0,0.0,0.0])
            else:
                Number(val,size=10,x=x+20,y=y+20)
            cell = Cell(x1=x,x2=x+cell_size,y1=y,y2=y+cell_size)
            cell.render()

    def click(self,click_x,click_y):
        cell_size = self.width//self.dim_size
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if self.check_click_inside_box(click_x,click_y,row*cell_size,col*cell_size,row*cell_size+cell_size,col*cell_size+cell_size):
                    self.isSafe = self.dig(row,col)

    def check_click_inside_box(self,click_x,click_y,x1,y1,x2,y2):
        
        if x1 <= click_x <= x2 and y1 <= click_y <= y2:
            return True
        return False
    







