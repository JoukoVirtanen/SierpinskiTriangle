from Tkinter import *
import math

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)

        width=800
        height=800
        self.canvas=Canvas(self, width=width, height=height)
        self.canvas.pack()

        x=100
        y=100
        size=600
        order=10
        self.drawSierpinskiTriangle(x, y, size, order)

    def drawTriangle(self, x, y, size):
        x1=x
        y1=y
        x2=x+size
        y2=y1
        x3=x+0.5*size
        y3=y+size*math.sqrt(3.0)/2.0

        self.canvas.create_line(x1, y1, x2, y2, fill="black")
        self.canvas.create_line(x2, y2, x3, y3, fill="black")
        self.canvas.create_line(x3, y3, x1, y1, fill="black")

    def drawSierpinskiTriangle(self, x, y, size, order):
        if order==1:
            self.drawTriangle(x, y, size)
        else:
            x1=x
            y1=y
            x2=x+size/2.0
            y2=y
            x3=x+size/4.0
            y3=y+size*math.sqrt(3.0)/4.0
            self.drawSierpinskiTriangle(x1, y1, size/2, order-1)
            self.drawSierpinskiTriangle(x2, y2, size/2, order-1)
            self.drawSierpinskiTriangle(x3, y3, size/2, order-1)
        
if __name__=="__main__":
    app=MainApp()
    app.geometry("800x800")
    app.mainloop()
