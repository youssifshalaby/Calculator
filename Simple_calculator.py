from tkinter import *

class Calculator:
    def __init__(self,window):
        self.window = window
        self.window.title("Simple Calculator")
        self.window.geometry("400x500")
        self.window.resizable(False, False)
        self.window.configure(bg="#1e1e1e")
        self.expression = ""
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        self.entry = Entry(window,font=("Arial", 18), bd=12, relief=RIDGE, justify="left")
        self.entry.pack(expand=True,fill="both")

        for row in buttons:
            frame = Frame(window)
            frame.pack(expand=True,fill="both")
            for char in row:
                btn = Button(frame,font=("Arial", 18),text = char,command= lambda c=char : self.on_button_click(c))
                btn.pack(side="left",expand=True,fill="both")
        
    def on_button_click(self,char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += char
            
        self.entry.delete(0, END)
        self.entry.insert(0, self.expression)
            


window = Tk()
calculator = Calculator(window)
window.mainloop()






