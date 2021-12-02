from pytube import YouTube
root = Tk()
root.geometry('1000x1000')
root.resizable(0,0)
root.title("Download any youtube vid")
Label(root,text = 'Yt Vid Downloader', font ='Roboto 20 ').pack()
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'Groteska 15 ').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 52, y = 90)
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'oliviar  15').place(x= 180 , y = 210)

Button(root,text = 'DOWNLOAD', font = 'futura 15 ' ,bg = 'teal', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()
