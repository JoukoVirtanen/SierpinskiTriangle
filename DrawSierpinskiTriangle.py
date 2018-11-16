from Tkinter import *
import math

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.settings_frame=Frame(self)
        self.settings_frame.grid()

        width=600
        height=600
        self.canvas=Canvas(self, width=width, height=height)
        #self.canvas.pack()

        self.orderLabel=Label(self.settings_frame, text="Order: ")
        self.orderLabel.grid(column=0, row=0)

        self.orderEntryVar=StringVar()
        self.orderEntry=Entry(self.settings_frame, width=3, textvariable=self.orderEntryVar)
        self.orderEntry.grid(column=1, row=0)
        self.orderEntryVar.set("7")

        self.xLabel=Label(self.settings_frame, text="X: ")
        self.xLabel.grid(column=2, row=0)

        self.xEntryVar=StringVar()
        self.xEntry=Entry(self.settings_frame, width=4, textvariable=self.xEntryVar)
        self.xEntry.grid(column=3, row=0)
        self.xEntryVar.set("50")

        self.yLabel=Label(self.settings_frame, text="Y: ")
        self.yLabel.grid(column=4, row=0)

        self.yEntryVar=StringVar()
        self.yEntry=Entry(self.settings_frame, width=4, textvariable=self.yEntryVar)
        self.yEntry.grid(column=5, row=0)
        self.yEntryVar.set("50")

        self.sizeLabel=Label(self.settings_frame, text="Size: ")
        self.sizeLabel.grid(column=6, row=0)

        self.sizeEntryVar=StringVar()
        self.sizeEntry=Entry(self.settings_frame, width=4, textvariable=self.sizeEntryVar)
        self.sizeEntry.grid(column=7, row=0)
        self.sizeEntryVar.set("400")

        action=lambda: self.drawSierpinskiTriangleUserInput()
        self.clearButton=Button(self.settings_frame, text="Add", command=action)
        self.clearButton.grid(column=9, row=0)

        action=lambda: self.clearCanvas()
        self.clearButton=Button(self.settings_frame, text="Clear", command=action)
        self.clearButton.grid(column=10, row=0)

        self.canvas.grid(column=0, row=1)

        x=int(self.xEntryVar.get())
        y=int(self.yEntryVar.get())
        size=int(self.sizeEntryVar.get())
        order=int(self.orderEntryVar.get())
        self.drawSierpinskiTriangle(x, y, size, order)

    def clearCanvas(self):
        self.canvas.delete(ALL)

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

    def drawSierpinskiTriangleUserInput(self):
        x=int(self.xEntryVar.get())
        y=int(self.yEntryVar.get())
        size=int(self.sizeEntryVar.get())
        order=int(self.orderEntryVar.get())
        if order>0 and order<8:
            self.drawSierpinskiTriangle(x, y, size, order)
        else:
            print "Order must be between 1 and 7"
        
if __name__=="__main__":
    app=MainApp()
    app.geometry("800x800")
    app.mainloop()
