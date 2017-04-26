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
# Importing Modules
try:
    import Tkinter, ttk
except:
    import tkinter as Tkinter
    import tkinter.ttk as ttk
import os
from Configuration_base import *
import Controls




class Main(Tkinter.Tk):
    def __init__(self, *args, **kwargs):
        Tkinter.Tk.__init__(self, *args, **kwargs)
        ct=Controls.Main(root=self)
        self.hook=ct.hook
        self.controls_=ct.hook2
        self.creating_menu_bar()
    def creating_menu_bar(self):
        try:
            add_fileicon=Tkinter.PhotoImage(file="../Icons/add_file.gif")
            add_directoryicon=Tkinter.PhotoImage(file="../Icons/add_directory.gif")
            exiticon=Tkinter.PhotoImage(file="../Icons/exit.gif")
            playicon=Tkinter.PhotoImage(file="../Icons/play.gif")
            pauseicon=Tkinter.PhotoImage(file="../Icons/pause.gif")
            stopicon=Tkinter.PhotoImage(file="../Icons/stop.gif")
            rewindicon=Tkinter.PhotoImage(file="../Icons/rewind.gif")
            fast_forwardicon=Tkinter.PhotoImage(file="../Icons/fast_forward.gif")
            previous_trackicon=Tkinter.PhotoImage(file="../Icons/previous_track.gif")
            next_trackicon=Tkinter.PhotoImage(file="../Icons/next_track.gif")
            muteicon=Tkinter.PhotoImage(file="../Icons/mute.gif")
            unmuteicon=Tkinter.PhotoImage(file="../Icons/unmute.gif")
            delete_selectedicon=Tkinter.PhotoImage(file="../Icons/delete_selected.gif")
    
        except Exception as e:
            print ("[ Script Detected Change or Missing Something ]\n")
            print (e)
            import sys
            sys.exit(0)

        menu_bar=Tkinter.Menu(self)    # MAIN BAR

        #   [ FILE ]  OPTIONS
        file_menu=Tkinter.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open_file",accelerator="Ctrl+O",compound="left", underline=0, image=add_fileicon, command=self.hook.ask_for_play_song_direct) 
        file_menu.add_command(label="Open_folder",accelerator="Ctrl+Shift+O",compound="left", underline=0, image=add_directoryicon, command=self.hook.ask_for_directory)
        file_menu.add_command(label="Open_Disk",accelerator="Ctrl+D",compound="left", underline=0, image=add_directoryicon, command=self.hook.ask_for_directory)
        file_menu.add_separator()
        file_menu.add_command(label="Quit",accelerator="Alt+F4",compound="left", underline=0, image=exiticon, command=self.destroy)

        #   [ EDIT ] OPTIONS
        edit_menu=Tkinter.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Play",accelerator="Space",compound="left", underline=0, image=playicon, command=self.controls_.play)
        edit_menu.add_command(label="Pause",accelerator="Space",compound="left", underline=0, image=pauseicon, command=self.controls_.pause)
        edit_menu.add_command(label="Stop",accelerator="Ctrl+T",compound="left", underline=0, image=stopicon, command=self.controls_.stop)
        edit_menu.add_separator()
        edit_menu.add_command(label="Rewind Track",accelerator="Ctrl+R",compound="left", underline=0, image=rewindicon, command=self.controls_.rewind)
        edit_menu.add_command(label="Fast_Forward",accelerator="Ctrl+F",compound="left", underline=0, image=fast_forwardicon, command=self.controls_.fast)
        edit_menu.add_separator()
        edit_menu.add_command(label="Previous Track",accelerator="Ctrl+P",compound="left", underline=0, image=previous_trackicon, command=self.controls_.previous)
        edit_menu.add_command(label="Next Track",accelerator="Ctrl+N",compound="left", underline=0, image=next_trackicon, command=self.controls_.Next)
        edit_menu.add_separator()
        edit_menu.add_command(label="Mute",accelerator="Ctrl+M",compound="left", underline=0, image=muteicon, command=self.controls_.mute)
        edit_menu.add_command(label="Un-mute",accelerator="Ctrl+N",compound="left", underline=0, image=unmuteicon, command=self.controls_.unmute)
        edit_menu.add_separator()
        edit_menu.add_command(label="Increase Volume",accelerator="Ctrl++",compound="left", underline=0, image=add_fileicon, command=self.controls_.increase_volume)
        edit_menu.add_command(label="Decrease Volume",accelerator="Ctrl+-",compound="left", underline=0, image=delete_selectedicon, command=self.controls_.decrease_volume)


        #   [ ABOUT ] OPTIONS
        about_menu=Tkinter.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label='Help', accelerator='F1', compound='left', underline=0)
        about_menu.add_separator()
        about_menu.add_command(label='About', accelerator='F2' ,compound='left', underline=0)

        #-------[ Joining menu sections with main menu ]----------------------
        menu_bar.add_cascade(label='File', menu=file_menu)
        menu_bar.add_cascade(label='Edit', menu=edit_menu)
        menu_bar.add_cascade(label='About', menu=about_menu)

        #------[ Joining with root ]------------------------------------------
        self.config(menu=menu_bar)


if __name__=='__main__':
    Main(className=PROGRAM_NAME).mainloop()
