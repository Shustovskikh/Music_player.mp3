import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from PIL import Image

root = Tk()
root.geometry("516x700+340+10")
root.title("Аудиоплеер - Витяз 2")
root.config(bg='#0f0f0f')
root.resizable(True, True)
mixer.init()

songs = []
paused = False
current_song_index = None

def resize_image(image_path):
    img = Image.open(image_path)
    img = img.resize((50, 50), Image.LANCZOS)
    img.save(image_path)

def addMusic():
    global songs
    files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
    if files:
        songs = files
        print(songs)
        for song in songs:
            Playlist.insert(END, os.path.basename(song))  # Добавить только имя файла в Listbox

def playMusic():
    global paused, current_song_index
    if paused:
        mixer.music.unpause()
        paused = False
    else:
        current_song_index = Playlist.curselection()[0]
        music_name = songs[current_song_index]  # Получить полный путь к файлу
        print(music_name)
        mixer.music.load(music_name)  # Загрузить полный путь к файлу
        mixer.music.play()
        update_track_info()
        update_time()

def update_time():
    if not paused and mixer.music.get_busy():
        current_time = mixer.music.get_pos() // 1000
        mins, secs = divmod(current_time, 60)
        time_string = f"{mins:02d}:{secs:02d}"
        Playlist.delete(0)  # Удалить предыдущее время
        Playlist.insert(0, "Time: " + time_string)  # Добавить новое время на первую позицию
        root.after(1000, update_time)

def pauseMusic():
    global paused
    mixer.music.pause()
    paused = True

def stopMusic():
    mixer.music.stop()

def nextMusic():
    global current_song_index
    mixer.music.stop()  # Остановить текущий трек
    current_song_index = current_song_index+1 if current_song_index+1 < len(songs) else 0
    Playlist.select_clear(current_song_index-1)
    Playlist.select_set(current_song_index)
    playMusic()

def prevMusic():
    global current_song_index
    mixer.music.stop()  # Остановить текущий трек
    current_song_index = current_song_index-1 if current_song_index-1 >= 0 else len(songs)-1
    Playlist.select_clear(current_song_index+1)
    Playlist.select_set(current_song_index)
    playMusic()

def update_track_info():
    current_track = Playlist.get(current_song_index)
    previous_track = Playlist.get(current_song_index-1) if current_song_index-1 >= 0 else "No previous track"
    next_track = Playlist.get(current_song_index+1) if current_song_index+1 < len(songs) else "No next track"
    Playlist.insert(END, f"Current: {current_track}")
    Playlist.insert(END, f"Previous: {previous_track}")
    Playlist.insert(END, f"Next: {next_track}")

lower_frm = Frame(root, bg="#000000", width=516, height=400)
lower_frm.place(x=0, y=00)

frmcount = 32
frms = [PhotoImage(file= os.path.join(os.path.dirname(__file__), 'animation.gif'), format='gif -index %i' % i) for i in range(frmcount)]

def update(ind):
    frame = frms[ind]
    ind += 1
    if ind == frmcount:
        ind = 0
    lbl.config(image=frame)
    root.after(40, update, ind)

lbl = Label(root)
lbl.place(x=0, y=0)
root.after(0, update, 0)

menu = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'menu.png'))
lb_menu = Label(root, image=menu, width=516, height=120)
lb_menu.place(x=0, y=580)

frm_music = Frame(root, bd=2, relief=RIDGE, width=516, height=120)
frm_music.place(x=0, y=580)

resize_image(os.path.join(os.path.dirname(__file__), 'play.png'))
btn_play = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'play.png'))
btn_p = Button(root, image=btn_play, bg='#0f0f0f', height=50, width=50, command=playMusic)
btn_p.place(x=225, y=516)

resize_image(os.path.join(os.path.dirname(__file__), 'stop.png'))
btn_stop = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'stop.png'))
btn_s = Button(root, image=btn_stop, bg='#0f0f0f', height=50, width=50, command=stopMusic)
btn_s.place(x=140, y=516)

resize_image(os.path.join(os.path.dirname(__file__), 'pause.png'))
btn_pause = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'pause.png'))
btn_ps = Button(root, image=btn_pause, bg='#0f0f0f', height=50, width=50, command=pauseMusic)
btn_ps.place(x=310, y=516)

resize_image(os.path.join(os.path.dirname(__file__), 'next.png'))
btn_next = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'next.png'))
btn_n = Button(root, image=btn_next, bg='#0f0f0f', height=50, width=50, command=nextMusic)
btn_n.place(x=395, y=516)

resize_image(os.path.join(os.path.dirname(__file__), 'prev.png'))
btn_prev = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'prev.png'))
btn_pr = Button(root, image=btn_prev, bg='#0f0f0f', height=50, width=50, command=prevMusic)
btn_pr.place(x=55, y=516)

btn_browse = Button(root, text="Выбрать папку с музыкой", font=('Arial,bold', 15), fg="Black", bg="#FFFFFF", width=48, command=addMusic)
btn_browse.place(x=0, y=572)

Scroll = Scrollbar(frm_music)
Playlist = Listbox(frm_music, width=100, font=('Arial,bold', 15), bg='#0f0f0f', fg='#00ff00', selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

root.mainloop()