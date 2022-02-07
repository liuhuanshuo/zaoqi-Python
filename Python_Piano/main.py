# 公众号：早起Python

import time
import threading
from tkinter import *
from playsound import playsound
from tkmacosx import Button
from pygame import mixer

def Cs1():
    mixer.Sound("mp3/Cs1.wav").play()

def Ds1():
    mixer.Sound("mp3/Ds1.wav").play()

def Fs1():
    mixer.Sound("mp3/Fs1.wav").play()

def Gs1():
    mixer.Sound("mp3/Gs1.wav").play()

def As1():
    mixer.Sound("mp3/As1.wav").play()
##########Cs2 ----- As2########
def Cs2():
    mixer.Sound("mp3/Cs2.wav").play()

def Ds2():
    mixer.Sound("mp3/Ds2.wav").play()

def Fs2():
    mixer.Sound("mp3/Fs2.wav").play()

def Gs2():
    mixer.Sound("mp3/Gs2.wav").play()

def As2():
    mixer.Sound("mp3/As2.wav").play()
##########Cs3 ----- As3########
def Cs3():
    mixer.Sound("mp3/Cs3.wav").play()

def Ds3():
    mixer.Sound("mp3/Ds3.wav").play()

def Fs3():
    mixer.Sound("mp3/Fs3.wav").play()

def Gs3():
    mixer.Sound("mp3/Gs3.wav").play()

def As3():
    mixer.Sound("mp3/As3.wav").play()


def Cs4():
    mixer.Sound("mp3/Cs4.wav").play()

def Ds4():
    mixer.Sound("mp3/Ds4.wav").play()

def Fs4():
    mixer.Sound("mp3/Fs4.wav").play()

def Gs4():
    mixer.Sound("mp3/Gs4.wav").play()

def As4():
    mixer.Sound("mp3/As4.wav").play()


def Cs5():
    mixer.Sound("mp3/Cs5.wav").play()

def Ds5():
    mixer.Sound("mp3/Ds5.wav").play()

def Fs5():
    mixer.Sound("mp3/Fs5.wav").play()

def Gs5():
    mixer.Sound("mp3/Gs5.wav").play()

def As5():
    mixer.Sound("mp3/As5.wav").play()

class ZaoqiPiano:
    def __init__(self, master):
        self.master = master

        def play_music(event):
            ######################### C1 -- B1######################
            if event.char == "z":
                mixer.Sound("mp3/C1.wav").play()
                self.C1_button.configure(bg='yellow')
            if event.char == "x":
                mixer.Sound("mp3/D1.wav").play()
                self.D1_button.configure(bg='yellow')
            if event.char == "c":
                mixer.Sound("mp3/E1.wav").play()
                self.E1_button.configure(bg='yellow')
            if event.char == "v":
                mixer.Sound("mp3/F1.wav").play()
                self.F1_button.configure(bg='yellow')
            if event.char == "b":
                mixer.Sound("mp3/G1.wav").play()
                self.G1_button.configure(bg='yellow')
            if event.char == "n":
                mixer.Sound("mp3/A1.wav").play()
                self.A1_button.configure(bg='yellow')
            if event.char == "m":
                mixer.Sound("mp3/B1.wav").play()
                self.B1_button.configure(bg='yellow')
            ######################### C2 -- B2######################
            if event.char == "a"  or event.char == ",":
                mixer.Sound("mp3/C2.wav").play()
                self.C2_button.configure(bg='yellow')
            if event.char == "s" or event.char == ".":
                mixer.Sound("mp3/D2.wav").play()
                self.D2_button.configure(bg='yellow')
            if event.char == "d" or event.char == "/":
                mixer.Sound("mp3/E2.wav").play()
                self.E2_button.configure(bg='yellow')
            if event.char == "f":
                mixer.Sound("mp3/F2.wav").play()
                self.F2_button.configure(bg='yellow')
            if event.char == "g":
                mixer.Sound("mp3/G2.wav").play()
                self.G2_button.configure(bg='yellow')
            if event.char == "h":
                mixer.Sound("mp3/A2.wav").play()
                self.A2_button.configure(bg='yellow')
            if event.char == "j":
                mixer.Sound("mp3/B2.wav").play()
                self.B2_button.configure(bg='yellow')
            ######################### C3 -- B3######################
            if event.char == "q" or event.char == "k":
                mixer.Sound("mp3/C3.wav").play()
                self.C3_button.configure(bg='yellow')
            if event.char == "w" or event.char == "l":
                mixer.Sound("mp3/D3.wav").play()
                self.D3_button.configure(bg='yellow')
            if event.char == "e" or event.char == ";":
                mixer.Sound("mp3/E3.wav").play()
                self.E3_button.configure(bg='yellow')
            if event.char == "r" or event.char == "'":
                mixer.Sound("mp3/F3.wav").play()
                self.F3_button.configure(bg='yellow')
            if event.char == "t":
                mixer.Sound("mp3/G3.wav").play()
                self.G3_button.configure(bg='yellow')
            if event.char == "y":
                mixer.Sound("mp3/A3.wav").play()
                self.A3_button.configure(bg='yellow')
            if event.char == "u":
                mixer.Sound("mp3/B3.wav").play()
                self.B3_button.configure(bg='yellow')
            ######################### C4 -- B4######################
            if event.char == "1" or event.char == "i":
                mixer.Sound("mp3/C4.wav").play()
                self.C4_button.configure(bg='yellow')
            if event.char == "2" or event.char == "o":
                mixer.Sound("mp3/D4.wav").play()
                self.D4_button.configure(bg='yellow')
            if event.char == "3" or event.char == "p":
                mixer.Sound("mp3/E4.wav").play()
                self.E4_button.configure(bg='yellow')
            if event.char == "4" or event.char == "[":
                mixer.Sound("mp3/F4.wav").play()
                self.F4_button.configure(bg='yellow')
            if event.char == "5" or event.char == "]":
                mixer.Sound("mp3/G4.wav").play()
                self.G4_button.configure(bg='yellow')
            if event.char == "6" or event.char == "\\":
                mixer.Sound("mp3/A4.wav").play()
                self.A4_button.configure(bg='yellow')
            if event.char == "7":
                mixer.Sound("mp3/B4.wav").play()
                self.B4_button.configure(bg='yellow')

            ######################### C5-- B5######################
            if event.char == "8":
                mixer.Sound("mp3/C5.wav").play()
                self.C5_button.configure(bg='yellow')
            if event.char == "9":
                mixer.Sound("mp3/D5.wav").play()
                self.D5_button.configure(bg='yellow')
            if event.char == "0":
                mixer.Sound("mp3/E5.wav").play()
                self.E5_button.configure(bg='yellow')
            if event.char == "-":
                mixer.Sound("mp3/F5.wav").play()
                self.F5_button.configure(bg='yellow')
            if event.char == "=":
                mixer.Sound("mp3/G5.wav").play()
                self.G5_button.configure(bg='yellow')
            if event.char == " ":
                mixer.Sound("mp3/A5.wav").play()
                self.A5_button.configure(bg='yellow')

        def on_key_release(event):

            if event.keysym in keys:
                keys[event.keysym].config(bg=btn_bg)

        master.title("Python_Piano_GUI")
        master.geometry("1766x460")

        ######################### C1 -- B1######################
        self.C1_button = Button(master, bg="white", text="C1", height=200, width=50,activebackground='red')
        btn_bg = self.C1_button.cget("bg")
        self.C1_button.grid(row=5, column=0)
        self.Cs1_button = Button(master,bg="black", fg='white',text="C1#", command=Cs1, height=180, width=50)
        self.Cs1_button.grid(row=1, columnspan=2)
        self.D1_button = Button(master, bg="white", text="D1", height=200, width=50)
        self.D1_button.grid(row=5, column=1)
        self.Ds1_button = Button(master, bg="black", fg="white", text="D1#", command=Ds1, height=180, width=50)
        self.Ds1_button.grid(row=1, columnspan=4)
        self.E1_button = Button(master, bg="white", text="E1", height=200, width=50)
        self.E1_button.grid(row=5, column=2)
        self.F1_button = Button(master, bg="white", text="F1", height=200, width=50)
        self.F1_button.grid(row=5, column=3)
        self.Fs1_button = Button(master, bg="black", fg="white", text="F1#", command=Fs1, height=180, width=50)
        self.Fs1_button.grid(row=1, column=3, columnspan=2)
        self.G1_button = Button(master, bg="white", text="G1", height=200, width=50)
        self.G1_button.grid(row=5, column=4)
        self.Gs1_button = Button(master, bg="black", fg="white", text="G1#", command=Gs1, height=180, width=50)
        self.Gs1_button.grid(row=1, column=4, columnspan=2)
        self.A1_button = Button(master, bg="white", text="A1", height=200, width=50)
        self.A1_button.grid(row=5, column=5)
        self.As1_button = Button(master, bg="black", fg="white", text="A1#", command=As1, height=180, width=50)
        self.As1_button.grid(row=1, column=5, columnspan=2)
        self.B1_button = Button(master, bg="white", text="B1", height=200, width=50)
        self.B1_button.grid(row=5, column=6)
        ######################### C2 -- B2######################
        self.C2_button = Button(master, bg="white", text="C2", height=200, width=50)
        self.C2_button.grid(row=5, column=7)
        self.D2_button = Button(master, bg="white", text="D2", height=200, width=50)
        self.D2_button.grid(row=5, column=8)
        self.E2_button = Button(master, bg="white", text="E2", height=200, width=50)
        self.E2_button.grid(row=5, column=9)
        self.F2_button = Button(master, bg="white", text="F2", height=200, width=50)
        self.F2_button.grid(row=5, column=10)
        self.G2_button = Button(master, bg="white", text="G2", height=200, width=50)
        self.G2_button.grid(row=5, column=11)
        self.A2_button = Button(master, bg="white", text="A2", height=200, width=50)
        self.A2_button.grid(row=5, column=12)
        self.B2_button = Button(master, bg="white", text="B2", height=200, width=50)
        self.B2_button.grid(row=5, column=13)
        self.Cs2_button = Button(master, bg="black", fg="white", text="C2#", command=Cs2, height=180, width=50)
        self.Cs2_button.grid(row=1, column=7, columnspan=2)
        self.Ds2_button = Button(master, bg="black", fg="white", text="D2#", command=Ds2, height=180, width=50)
        self.Ds2_button.grid(row=1, column=8, columnspan=2)
        self.Fs2_button = Button(master, bg="black", fg="white", text="F2#", command=Fs2, height=180, width=50)
        self.Fs2_button.grid(row=1, column=10, columnspan=2)
        self.Gs2_button = Button(master, bg="black", fg="white", text="G2#", command=Gs2, height=180, width=50)
        self.Gs2_button.grid(row=1, column=11, columnspan=2)
        self.As2_button = Button(master, bg="black", fg="white", text="A2#", command=As2, height=180, width=50)
        self.As2_button.grid(row=1, column=12, columnspan=2)

        ######################### C3 -- B3######################
        self.C3_button = Button(master, bg="white", text="C3", height=200, width=50)
        self.C3_button.grid(row=5, column=14)
        self.D3_button = Button(master, bg="white", text="D3", height=200, width=50)
        self.D3_button.grid(row=5, column=15)
        self.E3_button = Button(master, bg="white", text="E3", height=200, width=50)
        self.E3_button.grid(row=5, column=16)
        self.F3_button = Button(master, bg="white", text="F3", height=200, width=50)
        self.F3_button.grid(row=5, column=17)
        self.G3_button = Button(master, bg="white", text="G3", height=200, width=50)
        self.G3_button.grid(row=5, column=18)
        self.A3_button = Button(master, bg="white", text="A3", height=200, width=50)
        self.A3_button.grid(row=5, column=19)
        self.B3_button = Button(master, bg="white", text="B3", height=200, width=50)
        self.B3_button.grid(row=5, column=20)

        self.Cs3_button = Button(master, bg="black", fg="white", text="C3#", command=Cs3, height=180, width=50)
        self.Cs3_button.grid(row=1, column=14, columnspan=2)
        self.Ds3_button = Button(master, bg="black", fg="white", text="D3#", command=Ds3, height=180, width=50)
        self.Ds3_button.grid(row=1, column=15, columnspan=2)
        self.Fs3_button = Button(master, bg="black", fg="white", text="F3#", command=Fs3, height=180, width=50)
        self.Fs3_button.grid(row=1, column=17, columnspan=2)
        self.Gs3_button = Button(master, bg="black", fg="white", text="G3#", command=Gs3, height=180, width=50)
        self.Gs3_button.grid(row=1, column=18, columnspan=2)
        self.As3_button = Button(master, bg="black", fg="white", text="A3#", command=As3, height=180, width=50)
        self.As3_button.grid(row=1, column=19, columnspan=2)
        ######################### C4 -- B4######################
        self.C4_button = Button(master, bg="white", text="C4", height=200, width=50)
        self.C4_button.grid(row=5, column=21)
        self.D4_button = Button(master, bg="white", text="D4", height=200, width=50)
        self.D4_button.grid(row=5, column=22)
        self.E4_button = Button(master, bg="white", text="E4", height=200, width=50)
        self.E4_button.grid(row=5, column=23)
        self.F4_button = Button(master, bg="white", text="F4", height=200, width=50)
        self.F4_button.grid(row=5, column=24)
        self.G4_button = Button(master, bg="white", text="G4", height=200, width=50)
        self.G4_button.grid(row=5, column=25)
        self.A4_button = Button(master, bg="white", text="A4", height=200, width=50)
        self.A4_button.grid(row=5, column=26)
        self.B4_button = Button(master, bg="white", text="B4", height=200, width=50)
        self.B4_button.grid(row=5, column=27)

        self.Cs4_button = Button(master, bg="black", fg="white", text="C4#", command=Cs4, height=180, width=50)
        self.Cs4_button.grid(row=1, column=21, columnspan=2)
        self.Ds4_button = Button(master, bg="black", fg="white", text="D4#", command=Ds4, height=180, width=50)
        self.Ds4_button.grid(row=1, column=22, columnspan=2)
        self.Fs4_button = Button(master, bg="black", fg="white", text="F4#", command=Fs4, height=180, width=50)
        self.Fs4_button.grid(row=1, column=24, columnspan=2)
        self.Gs4_button = Button(master, bg="black", fg="white", text="G4#", command=Gs4, height=180, width=50)
        self.Gs4_button.grid(row=1, column=25, columnspan=2)
        self.As4_button = Button(master, bg="black", fg="white", text="A4#", command=As4, height=180, width=50)
        self.As4_button.grid(row=1, column=26, columnspan=2)


        ######################### C5 -- B5######################
        self.C5_button = Button(master, bg="white", text="C5", height=200, width=50)
        self.C5_button.grid(row=5, column=28)
        self.D5_button = Button(master, bg="white", text="D5", height=200, width=50)
        self.D5_button.grid(row=5, column=29)
        self.E5_button = Button(master, bg="white", text="E5", height=200, width=50)
        self.E5_button.grid(row=5, column=30)
        self.F5_button = Button(master, bg="white", text="F5", height=200, width=50)
        self.F5_button.grid(row=5, column=31)
        self.G5_button = Button(master, bg="white", text="G5", height=200, width=50)
        self.G5_button.grid(row=5, column=32)
        self.A5_button = Button(master, bg="white", text="A5", height=200, width=50)
        self.A5_button.grid(row=5, column=33)
        self.B5_button = Button(master, bg="white", text="B5", height=200, width=50)
        self.B5_button.grid(row=5, column=34)

        self.Cs5_button = Button(master, bg="black", fg="white", text="C5#", command=Cs5, height=180, width=50)
        self.Cs5_button.grid(row=1, column=28, columnspan=2)
        self.Ds5_button = Button(master, bg="black", fg="white", text="D5#", command=Ds5, height=180, width=50)
        self.Ds5_button.grid(row=1, column=29, columnspan=2)
        self.Fs5_button = Button(master, bg="black", fg="white", text="F5#", command=Fs5, height=180, width=50)
        self.Fs5_button.grid(row=1, column=31, columnspan=2)
        self.Gs5_button = Button(master, bg="black", fg="white", text="G5#", command=Gs4, height=180, width=50)
        self.Gs5_button.grid(row=1, column=32, columnspan=2)
        self.As5_button = Button(master, bg="black", fg="white", text="A5#", command=As4, height=180, width=50)
        self.As5_button.grid(row=1, column=33, columnspan=2)


        keys = {"z": self.C1_button,"x": self.D1_button,"c": self.E1_button,"v": self.F1_button,"b": self.G1_button,"n": self.A1_button,"m": self.B1_button,
                "a": self.C2_button,"s": self.D2_button,"d": self.E2_button,"f": self.F2_button,"g": self.G2_button,"h": self.A2_button,"j": self.B2_button,"comma": self.C2_button,"period": self.D2_button,"slash": self.E2_button,
                "q": self.C3_button,"w": self.D3_button,"e": self.E3_button,"r": self.F3_button,"t": self.G3_button,"y": self.A3_button,"u": self.B3_button,"k": self.C3_button,"l": self.D3_button,"semicolon": self.E3_button,"apostrophe": self.F3_button,
                "1": self.C4_button,"2": self.D4_button,"3": self.E4_button,"4": self.F4_button,"5": self.G4_button,"6": self.A4_button,"7": self.B4_button,"i": self.C4_button,"o": self.D4_button,"p": self.E4_button,"bracketleft": self.F4_button,"bracketright": self.G4_button,"backslash": self.A4_button,
                "8": self.C5_button,"9": self.D5_button,"0": self.E5_button,"minus": self.F5_button,"equal": self.G5_button,"space": self.A5_button}
        master.bind('<KeyPress>', play_music)
        master.bind("<KeyRelease>", on_key_release)

mixer.init()
root = Tk()
my_gui = ZaoqiPiano(root)
root.mainloop()


