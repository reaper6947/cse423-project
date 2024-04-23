from line import draw_line
class Cell:
    def __init__(self, x1, x2, y1, y2):
        
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
    def render(self):
        
        #bottom 
        draw_line(self.x1,self.y1,self.x2,self.y1)
        #right
        draw_line(self.x2,self.y1,self.x2,self.y2)
        #top
        draw_line(self.x2,self.y2,self.x1,self.y2)
        #left
        draw_line(self.x1,self.y1,self.x1,self.y2)


    


