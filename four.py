# snake game
import tkinter as tk
import random
from time import sleep, perf_counter
from threading import Thread

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.game = {}
        self.game["grid"] = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,2,3,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,"a",0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]
        self.game["dead"] = False
        self.game["snake"] = {
            "direction":0, # East
            "location":[4,4],
            "length":3
        }
        self.game["speed"] = 1

        self.title = tk.Label(text="Snekk")
        self.title.pack()
        self.tics = []

        self.start = tk.Button(text="start",command=self.stdart)
        self.start.pack()
        
        self.applePlaced = True


        self.boxes = []
        # while( not self.game["dead"] ):
    def stdart (self) :
        self.master.bind('a',lambda event:self.rotate(-1))
        self.master.bind('d',lambda event:self.rotate(1))
        for b in self.game["grid"]:
            t = ""
            for cell in b:
                if(cell == 0):
                    t+="__"
                if(cell == "a"):
                    t+="ap"
                else:
                    if(cell > 0):
                        t+="##"
                t+=" "
            box = tk.Label(text=t ,font="monospace")
            box.pack()
            self.boxes.append(box)
        print("start")
        self.start.pack_forget()
        tick_thread = Thread(target=self.gametick)
        tick_thread.daemon = True
        # 
        tick_thread.start()
    def placeApple (self):
        print("place Apple...")
        x = round(random.random()*len(self.game["grid"]))-1
        y = round(random.random()*len(self.game["grid"][x]))-1
        if(self.game["grid"][x][y] == 0):
            self.game["grid"][x][y] = "a"
            self.applePlaced = True
        else:
            print("apple place failed :(")
    def rotate (self, dir):
        print("rotato")
        # dir should be 1 or -1
        if(dir == 1):
            # clockwise
            if self.game["snake"]["direction"] == 3:
                self.game["snake"]["direction"] = 0
            else :
                self.game["snake"]["direction"] += 1
        else:
            # counter-clockwise
            if self.game["snake"]["direction"] == 0:
                self.game["snake"]["direction"] = 3
            else :
                self.game["snake"]["direction"] -= 1
        self.screen(False)
    def screen (self,deplete) :
        for bb in self.boxes:
            bb.pack_forget()
        self.boxes = []
        y=0
        for b in self.game["grid"]:
            # print(b)
            t = ""
            x = 0
            for cell in b:
                if(cell == 0):
                    t+="__"
                if(cell == "a"):
                    t+="ap"
                else:
                    if(cell > 0):
                        if cell == self.game["snake"]["length"]:
                            heads = ["->","\\/","<-","/\\"]
                            t+=heads[self.game["snake"]["direction"]]
                        else:
                            t+="##"
                        if(deplete):
                            self.game["grid"][y][x]-=1
                    
                t+=" "
                x+=1
            box = tk.Label(text=t )
            # if(t == self.boxes[y]) # Optimization?
            box.pack()
            self.boxes.append(box)
            y+=1
    def gametick (self) :
        while not (self.game["dead"]) :
            print("game tic")
            if(not self.applePlaced):
                self.placeApple()
            directions = [
                [1,0],
                [0,1],
                [-1,0],
                [0,-1]
            ]
            self.game["snake"]["location"][0]+=directions[self.game["snake"]["direction"]][0]
            self.game["snake"]["location"][1]+=directions[self.game["snake"]["direction"]][1]
            if(self.game["snake"]["location"][1]-directions[self.game["snake"]["direction"]][1]>9 or self.game["snake"]["location"][1]-directions[self.game["snake"]["direction"]][1]<0 or self.game["snake"]["location"][0]-directions[self.game["snake"]["direction"]][0]>14 or self.game["snake"]["location"][0]-directions[self.game["snake"]["direction"]][0]<0):
                self.game["dead"]=True
            self.screen(True)
            if not (self.game["dead"]):
                x = self.game['snake']["location"][0] 
                y = self.game['snake']["location"][1]
                if not (self.game["snake"]["location"][1]>9 or self.game["snake"]["location"][1]<0 or self.game["snake"]["location"][0]>14 or self.game["snake"]["location"][0]<0):
                    cell = self.game["grid"][y][x]
                    if(cell == "a"):
                        self.game['snake']["length"]+=1
                        self.applePlaced = False
                        if(self.game['snake']["length"]%5==0):
                            self.game['speed']
                    else:
                        if(cell > 0):
                            self.game["dead"]=True
                    self.game["grid"][y][x]=self.game['snake']["length"]    
                sleep(1/self.game["speed"])
        dead = tk.Label(text=f"you died. score: {self.game["snake"]["length"]-3}")
        dead.pack()
root = tk.Tk()
myapp = App(root)
myapp.mainloop()