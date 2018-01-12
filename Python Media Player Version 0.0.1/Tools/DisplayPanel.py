#!/usr/bin/python

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This is an Example Of Tkinter Canvas Graphics
# This Script Is Created For http://bitforestinfo.blogspot.in
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################
'''
# ====================================================
# Usages:
#       Player(root, var1, var2, var3)
# root=Frame or widget for place display
# var1=String Variable For Song Path
# var2=String Variable For Song Playing Time
# var3=String Variable For Song Durations
#=====================================================

# Here Importing Module
try:
    import Tkinter, ttk
except:
    import tkinter as Tkinter
    import tkinter.ttk as ttk
import os.path
from Configuration_base import *

# Creating Class
class Player:
    def __init__(self, root, song, time, duration):
        self.root=Tkinter.Frame(root)
        self.root.pack(side='top')
        self.song=song
        self.time=time
        self.duration=duration
        self.create_console()
        self.auto_bind()
        
    def auto_bind(self):
        self.song.trace('w',self.update_song_title)
        self.time.trace('w',self.update_time)
        self.duration.trace('w', self.update_duration)
        return
    
    def create_console(self):
        self.back_time_label=Tkinter.PhotoImage(file="../Icons/background.gif")
        # consoleframe=Tkinter.LabelFrame(self.root, text='Display Panel', bg='aqua')
        # consoleframe.pack(side='top', expand='yes', fill='x')
        self.canvas=Tkinter.Canvas(self.root, width=400, height=100, bg='skyblue')
        self.canvas.pack()
        self.canvas.image=self.back_time_label
        self.canvas.create_image(0, 0, anchor="nw", image=self.back_time_label)
        self.time_display=self.canvas.create_text(10, 25, anchor="nw", fill='cornsilk', font=Digital_Clock_Font_Setting, text='0:00:00')
        self.song_display=self.canvas.create_text(220,40, anchor="nw", fill='cornsilk', font=Songs_playing_Font_Setting, text='Nothing For Playing')
        self.song_duration=self.canvas.create_text(220,65, anchor="nw", fill='cornsilk', font=duration_time_Font_Setting, text='[0:00:00]')        
        return
    
    def song_title_filter(self, text):
        if len(os.path.basename(text))>22:
            name=os.path.basename(text)[0:20]+'...'
            pass
        else:
            name=os.path.basename(text)
            pass
        return name
                    
    def update_duration(self, *args,**kwargs):
        raw_text=self.duration.get()
        text="[{}]".format(raw_text)
        self.canvas.itemconfig(self.song_duration, text=text)
        return
    
    def update_time(self, *args, **kwargs):
        text=self.time.get()
        self.canvas.itemconfig(self.time_display, text=text)
        return

    def update_song_title(self, *args, **kwargs):
        text=self.song.get()
        text=self.song_title_filter(text)
        self.canvas.itemconfig(self.song_display, text=text)
        return
    
        
if __name__=='__main__':
    root=Tkinter.Tk()
    Var=Tkinter.IntVar()
    root.title('Player Module')
    var1=Tkinter.StringVar()
    Tkinter.Entry(root, textvariable=var1).pack(side='top')
    var2=Tkinter.StringVar()
    Tkinter.Entry(root, textvariable=var2).pack(side='top')
    var3=Tkinter.StringVar()
    Tkinter.Entry(root, textvariable=var3).pack(side='top')
    Player(root, var1, var2, var3)
    while True:
        root.update()
        root.update_idletask()
