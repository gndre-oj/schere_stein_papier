# -*- coding: utf-8 -*-

try:
    import tkinter as tk
    from tkinter import *
    from tkinter import ttk
    import random as r
    from PIL import Image, ImageTk # pillow muss extern installiert werden wenn auto-download nicht funktioniert

except ImportError:
    from subprocess import call
    from tkinter import StringVar, ttk, Tk, IntVar

    def download():
        text_var.set("Der Download beginnt...")
        fenster.update()
        call("curl https://bootstrap.pypa.io/get-pip.py -o get -pip.py")
        call("python -m pip install -I pip")
        call("pip install pillow")
        text_var.set("Download abgeschlossen.")
        fenster.update()
        fenster.after(5000,fenster.destroy)

    fenster = Tk()
    fenster.config(bg="#3b3b3b")
    text_var = StringVar()
    text_var.set("Fehlende Daten downloaden?")
    ttk.Label(fenster,textvariable=text_var).grid(column=0,row=0,pady=4,padx=4)
    ttk.Button(fenster,text="Download",command=download).grid(column=0,row=1,pady=4,padx=4)

class game():
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Stein, Schere, Papier")
        self.root.geometry("750x750")
        self.root.config(bg="#d6e9f7")
        
        self.text_var = StringVar()
        self.highscore_var = IntVar()
        self.score_var = IntVar()
        self.temp_var = 0
        
        self.__build()
        self.__display()
        
    def score(self):
        self.temp_var += 1
        self.score_var.set(self.temp_var)
        print("Score: " + str(self.score_var.get()))
        
    def active_game(self, b_state):
        # Stein = 1
        # Papier = 2
        # Schere = 3
        
        fg_color_w = "#e13423"
        fg_color_l = "#e13423"
        
        
        com = r.randint(1,3)
        
        if b_state == 1:
            self.p_choice.config(image=self.img_1)
        elif b_state == 2:
            self.p_choice.config(image=self.img_2)
        elif b_state == 3:
            self.p_choice.config(image=self.img_3)
            
        if com == 1:
            self.com_choice.config(image=self.img_1)
        elif com == 2:
            self.com_choice.config(image=self.img_2)
        elif com == 3:
            self.com_choice.config(image=self.img_3)
            
        
        if b_state == com:
            self.text_var.set("Draw")
            self.result.config(fg="#eeb422")
        else:
            if b_state == 1:
                if com == 2:
                    self.text_var.set("Lose")
                    self.result.config(fg=fg_color_l)
                    self.temp_var = 0
                    print("Streak Ende")
                else:
                    self.text_var.set("Victory")
                    self.result.config(fg="#2e8b57")
                    self.score()
            elif b_state == 2:
                if com == 3:
                    self.text_var.set("Lose")
                    self.result.config(fg=fg_color_l)
                    self.temp_var = 0
                    print("Streak Ende")
                else:
                    self.text_var.set("Victory")
                    self.result.config(fg="#2e8b57")
                    self.score()
            elif b_state == 3:
                if com == 1:
                    self.text_var.set("Lose")
                    self.result.config(fg=fg_color_l)
                    self.temp_var = 0
                    print("Streak Ende")
                else:
                    self.text_var.set("Victory")
                    self.result.config(fg="#2e8b57")
                    self.score()
        
    
    def __build(self):
        
        bg_color = "#d6e9f7"
        
        img_stone = (Image.open(r"img\stein.png"))
        img_paper = (Image.open(r"img\papier.png"))
        img_scissor = (Image.open(r"img\schere.png"))
        img_vs = (Image.open(r"img\vs.png"))
        
        self.img_1 = ImageTk.PhotoImage(img_stone) # Bild Stein
        self.img_2 = ImageTk.PhotoImage(img_paper) # Bild Papier
        self.img_3 = ImageTk.PhotoImage(img_scissor) # Bild Schere
        self.img_vs = ImageTk.PhotoImage(img_vs)
        
        self.scoreboard_frame = Frame(self.root, bg=bg_color)
        self.scoreboard_frame.pack(anchor="ne")
        self.main_game_frame = Frame(self.root, bg=bg_color)
        self.main_game_frame.pack()
        self.frame_buttons = Frame(self.main_game_frame, bg=bg_color)
        self.frame_buttons.pack(side="top")
        self.frame_vs = Frame(self.main_game_frame, bg=bg_color)
        self.frame_vs.pack(side="top")
        self.frame_game = Frame(self.main_game_frame, bg=bg_color)
        self.frame_game.pack(side="top")
        self.frame_result = Frame(self.main_game_frame, bg=bg_color)
        self.frame_result.pack(side="top")
        
        Label(self.frame_vs, image=self.img_vs, bg=bg_color).pack(side="left",padx=5,pady=10) # vs Zeichen
        self.p_choice = Label(self.frame_game, bg=bg_color)
        self.p_choice.pack(side="left",padx=45,pady=2) # Player Wahl
        self.com_choice = Label(self.frame_game, bg=bg_color)
        self.com_choice.pack(side="left",padx=45,pady=2) # Computer Wahl        
        self.result = Label(self.frame_result, font=("Frank Ruehl CLM Bold", 30), textvariable=self.text_var, bg=bg_color)
        self.result.pack(padx=15, pady=8) # Result Label
        
        Button(self.frame_buttons, bg=bg_color, activebackground=bg_color, borderwidth=0, image=self.img_1,
               command=lambda : self.active_game(1)).pack(side="left",padx=5,pady=2)
        Button(self.frame_buttons, bg=bg_color, activebackground=bg_color, borderwidth=0, image=self.img_2,
               command=lambda : self.active_game(2)).pack(side="left",padx=5,pady=2)
        Button(self.frame_buttons, bg=bg_color, activebackground=bg_color, borderwidth=0, image=self.img_3,
               command=lambda : self.active_game(3)).pack(side="left",padx=5,pady=2)
        
    def __display(self):
        self.root.mainloop()
    
if __name__ == "__main__":
    app = game()