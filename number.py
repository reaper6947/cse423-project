from line import draw_line

class Number:
    def __init__(self,number,size,x,y):
        self.num = number
        self.size = size
        self.x = x
        self.y = y
        self.draw()
        
    def draw(self):
        
        x = self.x
        y= self.y
        if self.num == "0":
            self.zero(x,y)
        elif self.num == "1":
            self.one(x,y)
        elif self.num == "2":
            self.two(x,y)
        elif self.num == "3":
            self.three(x,y)
        elif self.num == "4":
            self.four(x,y)
        elif self.num == "5":
            self.five(x,y)
        elif self.num == "6":
            self.six(x,y)
        elif self.num == "7":
            self.seven(x,y)
        elif self.num == "8":
            self.eight(x,y)



    def zero(self,x, y):
        size = self.size
        draw_line(x, y + size, x, y + size*2)
        draw_line(x + size, y + size*2, x, y + size*2)  
        draw_line(x + size, y + size, x + size, y + size*2)  
        draw_line(x + size, y, x + size, y + size)  
        draw_line(x, y, x + size, y) 
        draw_line(x, y, x, y + size)  

    def one(self,x, y):
        size = self.size
        draw_line(x + size, y + size, x + size, y + size*2)  
        draw_line(x + size, y, x + size, y + size)  
        


    def two(self,x, y):
        size = self.size
        draw_line(x + size, y + size*2, x, y + size*2)  
        draw_line(x + size, y + size, x + size, y + size*2)  
        draw_line(x, y, x + size, y)  
        draw_line(x, y, x, y + size)  
        draw_line(x, y + size, x + size, y + size)  
        


    def three(self,x, y):
        size = self.size
        draw_line(x + size, y + size*2, x, y + size*2)  
        draw_line(x + size, y + size, x + size, y + size*2)  
        draw_line(x + size, y, x + size, y + size)  
        draw_line(x, y, x + size, y)  # 5
        draw_line(x, y + size, x + size, y + size)  
        


    def four(self,x, y):
        size = self.size
        draw_line(x, y + size, x, y + size*2)  
        draw_line(x + size, y + size, x + size, y + size*2)  
        draw_line(x + size, y, x + size, y + size)  
        draw_line(x, y + size, x + size, y + size)  
        


    def five(self,x, y):
        size = self.size
        draw_line(x, y + size, x, y + size*2)  
        draw_line(x + size, y + size*2, x, y + size*2)  
        draw_line(x + size, y, x + size, y + size)  
        draw_line(x, y, x + size, y)  
        draw_line(x, y + size, x + size, y + size)  
        


    def six(self,x, y):
        size = self.size
        draw_line(x, y + size, x, y + size*2)  
        draw_line(x + size, y + size*2, x, y + size*2)  
        draw_line(x + size, y, x + size, y + size)  
        draw_line(x, y, x + size, y)  
        draw_line(x, y, x, y + size)  
        draw_line(x, y + size, x + size, y + size)  
        


    def seven(self,x, y):
        size = self.size
        draw_line(x + size, y + size*2, x, y + size*2)
        draw_line(x + size, y + size, x + size, y + size*2)
        draw_line(x + size, y, x + size, y + size)
        


    def eight(self,x, y):
        size = self.size
        draw_line(x, y + size, x, y + size*2) 
        draw_line(x + size, y + size*2, x, y + size*2) 
        draw_line(x + size, y + size, x + size, y + size*2) 
        draw_line(x + size, y, x + size, y + size) 
        draw_line(x, y, x + size, y) 
        draw_line(x, y, x, y + size)  
        draw_line(x, y + size, x + size, y + size)  
        
        