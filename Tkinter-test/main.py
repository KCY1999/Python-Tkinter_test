import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import importC

class aaa():

    def __init__(self):

        window = tk.Tk()
        window.title("CLASS")
        window.geometry('600x480')

        nb = ttk.Notebook(window)

        p1 = tk.Frame(nb, bg='gray')

        nb.add(p1, text="+-*/")
        nb.pack(fill="both", expand="yes")

        self.xf = tk.Frame(p1)
        self.xf.pack(side=tk.TOP)
        self.x_l = tk.Label(self.xf)
        self.x_l.pack(side=tk.LEFT)
        self.x_e = tk.Entry(self.xf)
        self.x_e.pack(side=tk.LEFT)

        self.yf = tk.Frame(p1)
        self.yf.pack(side=tk.TOP)
        self.y_l = tk.Label(self.yf)
        self.y_l.pack(side=tk.LEFT)
        self.y_e = tk.Entry(self.yf)
        self.y_e.pack(side=tk.LEFT)

        self.result_label = tk.Label(p1)
        self.result_label.pack()
        self.calculate = tk.Button(p1, text='+', command=self.btnclick1, fg='Red')
        self.calculate.pack()

        window.mainloop()

    def btnclick1(self):

        self.x1 = self.x_e.get()
        self.y1 = self.y_e.get()
        self.a1 = importC.num(self.x1, self.y1)
        self.result_label.configure(text=self.a1.sum())

main=aaa()

#################################################################################################
'''
t2 = tk.Label(p2, text='終極密碼', fg='BLUE',bg='pink')
t2.pack()
'''

