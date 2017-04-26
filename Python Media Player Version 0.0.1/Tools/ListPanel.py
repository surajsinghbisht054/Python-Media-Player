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
# ============================================
# Usages:
#       main(root, var1)
# root=Frame or widget for place display
# var1=String Variable For Song Path
#
# And If Want To Use Internal Functions Of ListPanel Then
#
# Usages:
#       storeobj=main(root, var1)
# hook=storeobj.hook
# hook.FuntionWantToUse 
#
# ============================================


# Here Importing Modules
# Importing Modules
try:
    import Tkinter, ttk,tkFileDialog
except:
    import tkinter as Tkinter
    import tkinter.ttk as ttk 
    import tkinter.filedialog as tkFileDialog

import os

from Configuration_base import *

# Creating Class
class ListPanel:
    def __init__(self, root, playing):
        self.playing=playing            # Playing Song Directory
        self.root=Tkinter.Frame(root, bg='skyblue')
        self.root.pack(side='top')
        self.var1=Tkinter.StringVar()       # For Search Songs
        self.directory=Tkinter.StringVar()  # For Directory
        self.directory.set('.')
        self.create_song_list_panel()

        
    def create_song_list_panel(self):
        # Creating Picture Canvas as Background
        background=Tkinter.PhotoImage(file="../Icons/background.gif")
        mainframe=Tkinter.Canvas(self.root)
        mainframe.pack(side='top', expand='yes', fill='both')
        mainframe.image=background
        mainframe.create_image(0, 0, anchor="nw", image=background)
        
        frame0=Tkinter.Frame(mainframe)
        frame0.pack(side='top')
        Tkinter.Label(frame0, text='Search : ', bg='skyblue').pack(side='left', expand='yes', fill='x')
        Tkinter.Entry(frame0, textvariable=self.var1).pack(side='left', expand='yes', fill='x')
        frame0.bind_all('<Any-KeyPress>',self.search_song_trigger)
        frame=Tkinter.Frame(mainframe, bg='skyblue')
        frame.pack(side='top')
        self.list_box=Tkinter.Listbox(frame, bg='powderblue', font=list_box_song_list_font, width=list_box_width, height=list_box_height)
        scrollbar=Tkinter.Scrollbar(frame, bg='skyblue')
        scrollbar.pack(side='right',expand='yes',fill='y')
        scrollbar.config(command=self.list_box.yview)
        self.list_box.config(yscrollcommand=scrollbar.set)
        self.list_box.pack(expand='yes',fill='both',side='right')
        frame1=Tkinter.Frame(mainframe, bg='blue')
        frame1.pack(side='top', expand='yes',fill='x')
        add_fileicon=Tkinter.PhotoImage(file="../Icons/add_file.gif")
        add_directoryicon=Tkinter.PhotoImage(file="../Icons/add_directory.gif")
        list_file=[
        (add_fileicon,'self.ask_for_play_song_direct'),
        (add_directoryicon,'self.ask_for_directory'),
        ]
        for i,j in list_file:
                storeobj=Tkinter.Button(frame1, image=i, command=eval(j), bg='blue')
                storeobj.pack(side='left')
                storeobj.image=i
        self.list_box.bind('<Double-Button-1>',self.play_on_click)
        return self.update_list_box_songs()
        

    def search_song_trigger(self, event=None):
            string=self.var1.get()
            list_dir=os.listdir(self.directory.get())
            self.list_box.delete('0','end')
            for i in list_dir:
                    if string in i:
                            if i[::-1][0]=='~':
                                pass
                            else:
                                    self.list_box.insert(0, i)
                    else:
                            pass
            return
    def play_on_click(self, event=None):
            store=self.list_box.selection_get()
            if self.directory.get()=='.':
                    path=os.path.join(os.getcwd(),store)
                    self.playing.set(path)
                    print ('[+] Song Variable Update Path : {}'.format(path))
                    return 
            else:
                    path=os.path.join(self.directory.get(),store)
                    self.playing.set(path)
                    print ('[+] Song Variable Update Path : {}'.format(path))
                    return 
        

    def update_list_box_songs(self, dirs='.'):
            files=os.listdir(dirs)
            files.reverse()
            self.list_box.delete('0','end')
            for i in files:
                    if i[::-1][0]=='~':
                            pass
                    else:
                            self.list_box.insert(0, i)
            return

        
    def ask_for_play_song_direct(self):
            path=tkFileDialog.askopenfilename(title='Play Selected Song')
            if path:
                    self.playing.set(path)
                    print ('[+] Song Variable Update Path : {}'.format(path))
                    return         

                    
    def ask_for_directory(self):
            path=tkFileDialog.askdirectory(title='Select Directory For Playlist')
            if path:
                    self.directory.set(path)
                    print (path)
                    return self.update_list_box_songs(dirs=path)
        
        
    
class main:
    def __init__(self, root, var1):
        self.playing=var1
        self.root=Tkinter.Frame(root)
        self.root.pack()
        self.anchorvar=Tkinter.IntVar()
        self.anchorvar.set(1)
        self.anchor_button=Tkinter.Button(self.root, text='[ Close ]', command=self.check_drawer, bg='skyblue', activebackground='powderblue')
        self.anchor_button.pack(side='top',expand='yes',fill='x')
        self.mainframe=Tkinter.Frame(self.root)
        self.mainframe.pack()
        obj=ListPanel(self.mainframe, self.playing)
        self.hook=obj
    def open_drawer(self):
        if self.anchorvar.get()==1:
            self.anchorvar.set(0)
            self.mainframe.pack_forget()
            self.anchor_button.config(text=' [ Open ]')
    def close_drawer(self):
        if self.anchorvar.get()==0:
            self.anchorvar.set(1)
            self.mainframe.pack(side='top',expand='yes',fill='both')
            self.anchor_button.config(text=' [ Close ]') 

    def check_drawer(self):
        if self.anchorvar.get()==1:
            self.anchorvar.set(0)
            self.mainframe.pack_forget()
            self.anchor_button.config(text=' [ Open ]')
        else:
            self.anchorvar.set(1)
            self.mainframe.pack(side='top',expand='yes',fill='both')
            self.anchor_button.config(text=' [ Close ]')        
    
               

        

if __name__=='__main__':
    root=Tkinter.Tk(className='Python Song List ')
    playing=Tkinter.StringVar()
    var1=Tkinter.StringVar() # For Playing Song
    Tkinter.Entry(root, textvariable=var1).pack(side='top')   
    main(root, var1)
    root.mainloop()
