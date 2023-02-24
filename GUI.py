from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np
import pickle
from Table import Table
from ForwardPass import ForwardPass
import LeakyReLU
from GradeDown import GradeDown
from Minus import Minus
from Each import Each

with open('net28by28.pickle', 'rb') as f:
    net = pickle.load(f)

def predict_digit(img):
    #resize image to 28x28 pixels
    img = img.resize((28,28), Image.NEAREST)
    #img.show()

    #convert rgb to grayscale
    img = img.convert('L')
    img = np.array(img)
    img[0] = [255]*28
    #reshaping to support our model input
    img = img.reshape(784)
    img = img.tolist()
    inp = Each(int, img)
    inp = Minus(255, inp)

    #predicting the class
    res = GradeDown(ForwardPass(LeakyReLU, net, Table(inp))[-1])[0]
    return res
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        # Creating elements
        self.canvas = tk.Canvas(self, width=300, height=300, bg = "white", cursor="cross")
        self.label = tk.Label(self, text="Thinking..", font=("Helvetica", 48))
        self.classify_btn = tk.Button(self, text = "Recognise", command = self.classify_handwriting) 
        self.button_clear = tk.Button(self, text = "Clear", command = self.clear_all)
        # Grid structure
        self.canvas.grid(row=0, column=0, pady=2, sticky=W, )
        self.label.grid(row=0, column=1,pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)
   
        self.canvas.bind("<B1-Motion>", self.draw_lines)
    def clear_all(self):
        self.canvas.delete("all")
    def classify_handwriting(self):
        HWND = self.canvas.winfo_id() # get the handle of the canvas
        rect = win32gui.GetWindowRect(HWND) # get the coordinate of the canvas
        im = ImageGrab.grab(rect)
        digit = predict_digit(im)
        self.label.configure(text= str(digit))
    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r=8
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='black')
app = App()
mainloop()