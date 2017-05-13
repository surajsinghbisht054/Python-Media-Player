# This Program Is Created Only For Practise and Educational Purpose Only
# This Program Is Created By S.S.B
# This Program Is Completely Free And Open Source
__author__='''

S.S.B
surajsinghbisht054@gmail.com
https://bitforestinfo.blogspot.com
'''
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
# Here Importing Modules
from Configuration_base import *

try:
    import Tkinter, ttk
except:
    import tkinter as Tkinter
    import tkinter.ttk as ttk
    
import player, ListPanel, DisplayPanel, os, threading, time

class Controls:
    def __init__(self, root, playing, player, volume):
        self.playervolume=volume
        self.root=Tkinter.Frame(root)
        self.root.pack()
        self.status=Tkinter.IntVar() # For Song Status
        self.playing=playing
        self.player=player
        self.var=Tkinter.IntVar() # For Volume Bar
        self.var.set(1.0)
        self.songtime=Tkinter.IntVar()
        self.create_control_panel()
        #self.time_thread()
        #print self.player.playing

    def time_thread(self):
        threading.Thread(target=self.update_time_).start()
        return
    
        
    def update_time_(self):
        while True:
            time.sleep(2)
            if self.player.player.playing:
                pass
            else:
                try:
                    print ('Playing Next Music')
                    self.Next()
                    pass
                except Exception as e:
                    print ('Playing Next Music- Error',e)
                    pass
                
                
    def create_control_panel(self):
        frame=Tkinter.LabelFrame(self.root)
        frame.pack(expand='yes',fill='x',side='top')
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
        self.muteicon=Tkinter.PhotoImage(file="../Icons/mute.gif")
        self.unmuteicon=Tkinter.PhotoImage(file="../Icons/unmute.gif")
        delete_selectedicon=Tkinter.PhotoImage(file="../Icons/delete_selected.gif")

        list_file=[
            (playicon,'self.play'),
            (pauseicon,'self.pause'),
            (stopicon,'self.stop'),
            (previous_trackicon,'self.previous'),
            (rewindicon,'self.rewind'),
            (fast_forwardicon,'self.fast'),
            (next_trackicon,'self.Next'),]
        for i,j in list_file:
            storeobj=ttk.Button(frame, image=i,command=eval(j))
            storeobj.pack(side='left')
            storeobj.image=i
        self.volume_label=Tkinter.Button(frame,image=self.unmuteicon)
        self.volume_label.image=self.unmuteicon
        
        volume=ttk.Scale(frame,from_=Volume_lowest_value, to=Volume_highest_value ,variable=self.var, command=self.update_volume)
        volume.pack(side='right', padx=10, )
        self.volume_label.pack(side='right')
        return

    
    def update_volume(self, event=None):
        if Volume_lowest_value==self.var.get():
            self.volume_label.config(state='active')
            self.volume_label.config(image=self.muteicon)
            self.playervolume.set(0.0)
            self.volume_label.config(state='disabled')
        else:
            self.volume_label.config(state='active')
            self.volume_label.config(image=self.unmuteicon)
            self.playervolume.set(self.volume_equalize())
            self.volume_label.config(state='disabled')
        return
    
    def volume_equalize(self):
        if len(str(self.var.get()))==1:
            val='0.{}'.format(str(self.var.get()))
        elif len(str(self.var.get()))==2:
            val='{}.{}'.format(str(self.var.get())[0],str(self.var.get())[1])
        else:
            val=self.var.get()
        return float(val)
    
    def mute(self):
        self.var.set(0)
        return self.update_volume()
    def unmute(self):
        self.var.set(11)
        return self.update_volume()
    def increase_volume(self):
        high=Volume_highest_value-5
        if self.var.get() < high:
            store=self.var.get()+5
            self.var.set(store)
            return self.update_volume()
    def decrease_volume(self):
        low=6
        if self.var.get() > low :
            store=self.var.get()-5
            self.var.set(store)
            return self.update_volume()
            
    def play(self):
        if self.status.get()==0:
            k=self.player.play_song()
            self.status.set(1)
            return k
        elif self.status.get()==1:
            k=self.player.play()
            self.status.set(0)
            return k
        else:
            print ('something wrong on controls.Controls.play')
            print ('or playing variable is empty')
            return 'Nothing'
    
    def pause(self):
        if self.status.get()==0 or self.status.get()==1:
            self.player.pause()
        return
        
    def stop(self):
        self.player.stop()
        return
    
    def previous(self):
        try:
            dirbase=os.path.dirname(self.playing.get())
            dirt=os.listdir(dirbase)
            base=os.path.basename(self.playing.get())
            k=dirt.index(base)-1
            path=os.path.join(dirbase, dirt[k])
            print (path)
            self.playing.set(path)
            pass
        except:
            pass
    def fast(self):
        return self.player.fast_forward()
    
    def Next(self):
        try:
            dirbase=os.path.dirname(self.playing.get())
            dirt=os.listdir(dirbase)
            base=os.path.basename(self.playing.get())
            k=dirt.index(base)-1
            path=os.path.join(dirbase, dirt[k])
            print (path)
            self.playing.set(path)
            pass
        except:
            pass
    def rewind(self):
        return self.player.rewind()
        
class Main:
    def __init__(self, root=None):
        self.root=Tkinter.Frame(root)
        self.root.pack(side='top')
        
        self.path=Tkinter.StringVar()           # For Song Path
        self.song_time=Tkinter.StringVar()      # For Song Playing Time
        self.song_duration=Tkinter.StringVar()  # For Song Duration
        self.volume=Tkinter.IntVar()            # For Song Volume

        # ============= Creating Media Player       ======================================================
        mediaplayer=player.mediaplayer(self.path, self.song_time, self.song_duration, self.volume)

        # ============= Creating Display Panel      ======================================================
        DisplayPanel.Player(self.root, self.path, self.song_time, self.song_duration)

        # ============= Creating Control Panel      ======================================================
        lit2=Controls(self.root, self.path, mediaplayer, self.volume)
        self.hook2=lit2
        # ============= Here Connecting List Panel  ======================================================
        lit=ListPanel.main(self.root, self.path)
        self.hook=lit.hook
        
        
if __name__=='__main__':
    root=Tkinter.Tk()
    Main(root)
    root.mainloop()
