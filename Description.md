- import os: Этот модуль предоставляет функции для взаимодействия с операционной системой.
- from tkinter import *: Это импортирует все классы и функции из модуля tkinter, который используется для создания графического пользовательского интерфейса (GUI).
- from tkinter import filedialog: Это импортирует модуль filedialog, который предоставляет диалоговые окна для запроса у пользователя файлов или директорий.
- from pygame import mixer: Это импортирует модуль mixer из pygame, который используется для воспроизведения звука.
- from PIL import Image: Это импортирует модуль Image из PIL (Python Imaging Library), который используется для работы с изображениями.
- root = Tk(): Это создает главное окно приложения.
- root.geometry("516x700+340+10"): Это устанавливает размер и положение главного окна.
- root.title("Аудиоплеер - Витяз 2"): Это устанавливает заголовок главного окна.
- root.config(bg='#0f0f0f'): Это устанавливает цвет фона главного окна.
- root.resizable(False, False): Это делает главное окно нерастягиваемым.
- mixer.init(): Это инициализирует модуль mixer pygame.
- songs = []: Это создает пустой список для хранения песен.
- paused = False: Это создает переменную, которая отслеживает, приостановлено ли воспроизведение.
- current_song_index = None: Это создает переменную для отслеживания текущей песни.
- def resize_image(image_path): Это определяет функцию, которая изменяет размер изображения до 50x50 пикселей.
- def addMusic(): Это определяет функцию, которая позволяет пользователю выбрать папку с музыкой и добавляет все mp3-файлы из этой папки в список песен.
- def playMusic(): Это определяет функцию, которая воспроизводит выбранную песню.
- def update_time(): Это определяет функцию, которая обновляет отображаемое время воспроизведения каждую секунду.
- def pauseMusic(): Это определяет функцию, которая приостанавливает воспроизведение песни.
- def stopMusic(): Это определяет функцию, которая останавливает воспроизведение песни.
- def nextMusic(): Это определяет функцию, которая воспроизводит следующую песню в списке.
- def prevMusic(): Это определяет функцию, которая воспроизводит предыдущую песню в списке.
- def update_track_info(): Это определяет функцию, которая обновляет информацию о текущем, предыдущем и следующем треках.
- lower_frm = Frame(root, bg="#000000", width=516, height=400): Это создает фрейм, который будет использоваться для отображения анимации.
- frmcount = 32: Это устанавливает количество кадров в анимации.
- frms = [PhotoImage(file= os.path.join(os.path.dirname(__file__), 'animation.gif'), format='gif -index %i' % i) for i in range(frmcount)]: Это создает список изображений для каждого кадра анимации.
- def update(ind): Это определяет функцию, которая обновляет кадр анимации каждые 40 миллисекунд.
- lbl = Label(root): Это создает метку, которая будет использоваться для отображения анимации.
- root.after(0, update, 0): Это начинает анимацию сразу после запуска приложения.
- menu = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'menu.png')): Это загружает изображение для меню.
- lb_menu = Label(root, image=menu, width=516, height=120): Это создает метку с изображением меню.
- frm_music = Frame(root, bd=2, relief=RIDGE, width=516, height=120): Это создает фрейм для отображения списка песен и кнопок управления.
- resize_image(os.path.join(os.path.dirname(__file__), 'play.png')): Это изменяет размер изображения кнопки 'play'.
- btn_play = PhotoImage(file= os.path.join(os.path.dirname(__file__), 'play.png')): Это загружает измененное изображение кнопки 'play'.
- btn_p = Button(root, image=btn_play, bg='#0f0f0f', height=50, width=50, command=playMusic): Это создает кнопку 'play', которая воспроизводит выбранную песню при нажатии.
- btn_p.place(x=225, y=516): Это размещает кнопку 'play' на координатах (225, 516) в окне root.
37-42. Эти строки повторяют те же шаги для кнопки 'stop'.
43-48. Эти строки повторяют те же шаги для кнопки 'pause'.
49-54. Эти строки повторяют те же шаги для кнопки 'next'.
55-60. Эти строки повторяют те же шаги для кнопки 'prev'.
- btn_browse = Button(root, text="Выбрать папку с музыкой", font=('Arial,bold', 15), fg="Black", bg="#FFFFFF", width=48, command=addMusic): Это создает кнопку 'browse', которая позволяет пользователю выбрать папку с музыкой.
- btn_browse.place(x=0, y=572): Это размещает кнопку 'browse' на координатах (0, 572) в окне root.
- Scroll = Scrollbar(frm_music): Это создает полосу прокрутки для frm_music.
- Playlist = Listbox(frm_music, width=100, font=('Arial,bold', 15), bg='#0f0f0f', fg='#00ff00', selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set): Это создает Listbox с именем Playlist, который будет использоваться для отображения списка песен.
- Scroll.config(command=Playlist.yview): Эта строка связывает полосу прокрутки Scroll с Playlist, так что когда вы прокручиваете полосу прокрутки, Playlist прокручивается.
- Scroll.pack(side=RIGHT, fill=Y): Эта строка размещает полосу прокрутки Scroll справа от frm_music и заполняет ее по вертикали.
- Playlist.pack(side=RIGHT, fill=BOTH): Эта строка размещает Playlist справа от frm_music и заполняет его по обеим осям (горизонтальной и вертикальной).
- root.mainloop(): Эта строка запускает основной цикл обработки событий Tkinter, который ожидает действия пользователя, такие как нажатие кнопки.
