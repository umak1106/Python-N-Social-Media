from future.moves import tkinter
from tkinter import *
from tkinter import filedialog
from pygame import mixer

class Musical:
    def __init__(self, window ):
        window.geometry('800x300'); window.title('Music Player'); window.resizable(0,0)
        Load = Button(window,bg = 'green',fg='pink' , text = 'Load',  width = 10, font = ('arial', 10), command = self.load)
        Play = Button(window,bg = 'yellow' ,fg='pink' ,text = 'Play',  width = 10,font = ('arial', 10), command = self.play)
        Pause = Button(window,bg = 'blue',fg='pink' ,text = 'Pause',  width = 10, font = ('arial', 10), command = self.pause)
        Stop = Button(window ,bg = 'purple',fg='pink' ,text = 'Stop',  width = 10, font = ('arial', 10), command = self.stop)
        Load.place(x=0,y=10);Play.place(x=110,y=10);Pause.place(x=210,y=10);Stop.place(x=110,y=60)
        self.m_file = False
        self.state = False
    def load(self):
        self.m_file = filedialog.askopenfilename()
    def play(self):
        if self.m_file:
            mixer.init()
            mixer.music.load(self.m_file)
            mixer.music.play()
    def pause(self):
        if not self.state:
            mixer.music.pause()
            self.state=True
        else:
            mixer.music.unpause()
            self.state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
Music = Musical(root)
root.mainloop()
