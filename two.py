#  quiz gui app

import tkinter as tk
root = tk.Tk()

corrects = 0

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.title = tk.Label(text="Quiz App")
        self.title.pack()

        self.clear = tk.Button(text="Start Quiz",command=self.clearFunc)
        self.clear.pack()

        self.answerBar = tk.Label()

        self.entrythingy = tk.Label()
        self.entrythingy.pack()

        self.buttons = []

        # Create the application variable.
        self.contents = tk.StringVar()

        self.selans = tk.StringVar()
        # Set it to some value.
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        
    def clearFunc(self):
        # print("clearing...")
        self.contents.set("")
        self.clear.pack_forget()
        self.question()

    def nextQuestion(self):
        global questionN
        questionN+=1
        global questions
        if(questionN == len(questions)):
            global corrects
            self.contents.set(f"Quiz Over. Result: {corrects} out of {len(questions)}")
            self.clear.pack_forget()
            
        else:
            self.clearFunc()
    
    def answer (self):
        global questionN
        c = False
        q = questions[questionN]
        print(f"Answer: {self.selans.get()}")
        if(q["type"] == "multi"):
            if(self.selans.get() == q["answers"][q["answer"]]):
                c=True
        if(q["type"] == "textbox" or q["type"] == "numentry" or q["type"] == "truefalse"):
            if(self.selans.get() == q["answer"]):
                c=True
        global corrects
        if c :
            corrects+=1
            # print("c=Correct")
        # else :
            # print("c=Incorrect")
        self.answerBar.pack_forget()
        self.clear = tk.Button(text="Next",command=self.nextQuestion)
        self.clear.pack()

    def textAnswer (sdelf, text):
        # print(f"textAnswer: text:{text}")
        # sdelf.selans = text
        sdelf.answer()




    def answerButton (self,ancer):
        def functn ():
            # print(type(ancer))
            # if( type(ancer) )
            self.selans.set(str(ancer))
            self.answer()
        return functn
    
    def question (self) :
        # print("load question")
        global questionN
        global questions
        q = questions[questionN]
        self.contents.set( q["text"])
        for bS in self.buttons:
            bS.pack_forget()
        self.buttons = []
        # print(q)
        self.selans = tk.StringVar()
        if(q["type"] == "multi"):
            i = 0
            for aS in q["answers"]:
                # print(f"possible answer: {aS}")
                ansbtn = tk.Button(text=aS,command=self.answerButton(aS))
                # self.buttons[i].pack_forget()
                self.buttons.append(ansbtn)
                ansbtn.pack(in_=self.answerBar, expand=True)
                i+=1
        if(q["type"] == "textbox"):
            tboX = tk.Entry(textvariable=self.selans)
            ansbtn = tk.Button(text="Enter",command=self.answer)
            # self.buttons[i].pack_forget()
            self.buttons.append(ansbtn)
            self.buttons.append(tboX)
            
            tboX.bind('<KeyPress-Return>',self.textAnswer)
            tboX.pack(in_=self.answerBar, expand=True)
            ansbtn.pack(in_=self.answerBar, expand=True)
        if(q["type"] == "truefalse"):
            ansbtn = tk.Button(text="True",command=self.answerButton("True"))
            self.buttons.append(ansbtn)
            ansbtn.pack(in_=self.answerBar, expand=True)
            ansbtn = tk.Button(text="False",command=self.answerButton("False"))
            self.buttons.append(ansbtn)
            ansbtn.pack(in_=self.answerBar, expand=True)
        if(q["type"] == "numentry"):
            nuer = tk.Scale(variable=self.selans)
            self.buttons.append(nuer)
            nuer.pack(in_=self.answerBar,expand=True)
            ansbtn = tk.Button(text="Enter",command=self.answer)
            self.buttons.append(ansbtn)
            ansbtn.pack(in_=self.answerBar, expand=True)
        self.answerBar.pack()




questions = [
    {
        "text":"What is 2+2?",
        "type":"multi",
        "answers":[
            "1",
            "2",
            "3",
            "4"
        ],
        "answer":3
    },
    {
        "text":"What language is this coded in?",
        "type":"textbox",
        "answer":"python"
    },
    {
        "text":"Why are Hands?",
        "type":"truefalse",
        "answer":"True"
    },
    {
        "text":"How many fingers are on my left hand relative to the number of eyes on my face (Not including any superficial and subcutaneous eyes.)",
        "type":"numentry",
        "answer":"3"
    },
    {
        "text":"Choose the perfect number.",
        "type":"multi",
        "answers":range(10,45),
        "answer":3
    },
]

index = 2
questionN = 0
topText = "Quiz App!"
myapp = App(root)
myapp.mainloop()