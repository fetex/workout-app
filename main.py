import tkinter   # modulo(es una biblioteca gráfica)
from PIL import Image, ImageTk


window = tkinter.Tk() #esto es para mostrar la ventana
window.geometry("630x630+5+5") #esto es para dimensionar la ventana
window.title("Bodybuilder App")


button1 = None


def show_new_window(): # permite vaciar la ventana para llevarnos al menu principal

    for widget in frame1.winfo_children(): #se usa el for porque winfo... da una lista de los elementos en la ventana
        widget.destroy()

    label1 = tkinter.Label(frame1, text = "Menú principal", font = ("verdana", 30), bg = "black", fg = "white" )
    label1.pack(pady = 20)
    
    button2 = tkinter.Button(frame1, text = "Rutinas preestablecidas", command = show_new_window2)
    button2.config(bg = "orange" , width=25, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button2.pack(pady = 20)
    button3 = tkinter.Button(frame1, text = "Regresar", command = go_back)
    button3.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button3.pack(pady = 10)


def show_new_window2(): #muestra el menú con las opciones de tren sup e inf.


    for widget in frame1.winfo_children():
        widget.destroy()

    button_tren_sup = tkinter.Button(frame1, text = "Tren superior", command = sup_routines_menu)
    button_tren_sup.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button_tren_sup.pack(pady = 100)

    button_tren_inf = tkinter.Button(frame1, text = "Tren inferior", command = inf_routines_menu  )
    button_tren_inf.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button_tren_inf.pack(pady = 20)

    back_button = tkinter.Button(frame1, text = "Regresar", command = show_new_window)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    back_button.pack(pady = 10)

is_paused = False
total_time = 0
activity = ""
rounds = 3 


def chest_timer():


    def countdown():
        """se globalizan las 3 variables (para modificarlas dentro de la función)
        se revisa que el tiempo no esté en pausa y sea mayor que cero (0)
        le va quitando de a 1 a 1
        hace lo mismo con los rounds o series
        si llega al final imprimer un mensaje de felicidades
        """
        global total_time, is_paused, activity, rounds


        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo


    def start_timer():
        """inicializa el temporizador 
        establece la actividad a trabajo
          reinicia el temporizador a 25
        """
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        """ pausa el temporizador
        """
        global is_paused
        is_paused = True


    def resume_timer():
        """
        reaunda el temporizador
        cambia el estado de pausa a False, haciendo que continue
        """
        global is_paused
        is_paused = False
        countdown()


    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)


    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = chest_menu,)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)


def bench_press():

    for widget in frame1.winfo_children():
        widget.destroy()
    
    chest_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("pressbanca.gif").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def inclined_press():

    for widget in frame1.winfo_children():
        widget.destroy()
    
    chest_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("image2.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def push_ups():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    chest_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("flexiones.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        

    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def openins():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    chest_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("aperturas.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        

    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def chest_menu(): #presionando el boton de pecho nos lleva a otro menú y muestra las opciones de ejercicios
    for widget in frame1.winfo_children():
        widget.destroy()


    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_chest = tkinter.Button(button_frame_a, text = "Press banca", command = bench_press     )
    button1_chest.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button1_chest.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_chest = tkinter.Button(button_frame_a, text = "Press Inclinado", command = inclined_press      )
    button2_chest.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button2_chest.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    


    button3_chest = tkinter.Button(button_frame_b, text = "Flexiones", font = 15, relief = "groove", command = push_ups    )
    button3_chest.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button3_chest.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_chest = tkinter.Button(button_frame_b, text = "Aperturas", font = 15, relief = "groove", command = openins    )
    button4_chest.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button4_chest.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = sup_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    back_button.pack(pady = 2)

    
def biceps_timer():

    
    def countdown():
        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo


    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()
        

    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)


    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = biceps_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)
    

def curl_bar():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    biceps_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("curlbarra.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def curl_manc():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    biceps_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("curlmancuerna.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()
        

    image_window()


def focused_curl():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    biceps_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("focusedcurl.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        

    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def hammer_curl():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    biceps_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("hammercurl.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)        

    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()

    image_window()


def biceps_menu():
    for widget in frame1.winfo_children():
        widget.destroy()

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_biceps = tkinter.Button(button_frame_a, text = "Curl con barra", command = curl_bar      )
    button1_biceps.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button1_biceps.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_biceps = tkinter.Button(button_frame_a, text = "Curl mancuernas", command = curl_manc      )
    button2_biceps.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button2_biceps.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_biceps = tkinter.Button(button_frame_b, text = "Curl concentrado", font = 15, relief = "groove", command = focused_curl     )
    button3_biceps.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button3_biceps.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_biceps = tkinter.Button(button_frame_b, text = "Curl de martillo", font = 15, relief = "groove", command = hammer_curl    )
    button4_biceps.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button4_biceps.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = sup_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    back_button.pack(pady = 2)


def back_timer():


    def countdown():
        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo

    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()
        

    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = back_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)


def bar_rem():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    back_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("remobarra.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)        

    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def pulldown():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    back_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("pulldown.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        

    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def deadlift():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    back_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("deadlift.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()

    image_window()


def rem_manc():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    back_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("remomancuerna.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def back_menu():
    for widget in frame1.winfo_children():
        widget.destroy()

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_back = tkinter.Button(button_frame_a, text = "Remo con barra", command = bar_rem     )
    button1_back.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button1_back.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_back = tkinter.Button(button_frame_a, text = "Pulldown", command = pulldown      )
    button2_back.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button2_back.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_back = tkinter.Button(button_frame_b, text = "Peso muerto", font = 15, relief = "groove", command = deadlift     )
    button3_back.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button3_back.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_back = tkinter.Button(button_frame_b, text = "remo con mancuerna", font = 15, relief = "groove", command = rem_manc    )
    button4_back.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button4_back.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = sup_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    back_button.pack(pady = 2)

def triceps_timer():


    def countdown():

        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo


    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()
        

    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = triceps_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)


def manc_extensions():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    triceps_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("image3.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def french_press():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    back_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("french.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def tricep_kick():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    back_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("tricep_kick.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def paralels():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    back_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("paralels.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def triceps_menu():

    for widget in frame1.winfo_children():
        widget.destroy()

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_tricep = tkinter.Button(button_frame_a, text = "Extensiones con mancuerna", command = manc_extensions     )
    button1_tricep.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button1_tricep.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_tricep = tkinter.Button(button_frame_a, text = "Press frances", command = french_press      )
    button2_tricep.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button2_tricep.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_tricep = tkinter.Button(button_frame_b, text = "Patada de triceps", font = 15, relief = "groove", command = tricep_kick    )
    button3_tricep.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button3_tricep.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_tricep = tkinter.Button(button_frame_b, text = "Fondos en paralelas", font = 15, relief = "groove", command = paralels    )
    button4_tricep.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button4_tricep.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = sup_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    back_button.pack(pady = 2)
    

def shoulder_timer():


    def countdown():

        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo


    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()
        

    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = shoulder_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)


def militar_press():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    shoulder_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("pressmil.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def lateral_elevations():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    shoulder_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("image4.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def frontal_elev():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    shoulder_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("frontales.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def shrughs():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    shoulder_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("shrugs.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def shoulder_menu():
    
    for widget in frame1.winfo_children():
        widget.destroy()
        

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_shoulder = tkinter.Button(button_frame_a, text = "Press militar", command = militar_press     )
    button1_shoulder.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button1_shoulder.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_shoulder = tkinter.Button(button_frame_a, text = "Elevaciones laterales", command = lateral_elevations      )
    button2_shoulder.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button2_shoulder.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_shoulder = tkinter.Button(button_frame_b, text = "Elevaciones frontales", font = 15, relief = "groove", command = frontal_elev    )
    button3_shoulder.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button3_shoulder.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_shoulder = tkinter.Button(button_frame_b, text = "Shrugs", font = 15, relief = "groove", command = shrughs    )
    button4_shoulder.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button4_shoulder.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = sup_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    back_button.pack(pady = 2)


def abs_timer():


    def countdown():
        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo


    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()
        

    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = abs_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)


def crunches():

    for widget in frame1.winfo_children():
        widget.destroy()
    
    abs_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("crunches.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def leg_raisin():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    abs_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("image5.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def plank():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    abs_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("plank.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def russian_twist():
    for widget in frame1.winfo_children():
        widget.destroy()
    
    abs_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("russian.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def abs_menu():

    for widget in frame1.winfo_children():
        widget.destroy()

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_abs = tkinter.Button(button_frame_a, text = "Crunches", command = crunches     )
    button1_abs.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button1_abs.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_abs = tkinter.Button(button_frame_a, text = "Elevaciones de piernas", command = leg_raisin       )
    button2_abs.config(bg = "orange", width = 17, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button2_abs.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_abs = tkinter.Button(button_frame_b, text = "Plancha", font = 15, relief = "groove", command = plank    )
    button3_abs.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button3_abs.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_abs = tkinter.Button(button_frame_b, text = "Russian twists", font = 15, relief = "groove", command = russian_twist    )
    button4_abs.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button4_abs.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = sup_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    back_button.pack(pady = 2)


def sup_routines_menu(): #va a mostrar el nuevo menú, luego de presionar el boton de rutinas preestablecidas

    for widget in frame1.winfo_children():
        widget.destroy()


    label2 = tkinter.Label(frame1, text = "Tren superior", font = 15,relief = "groove")
    label2.config(padx = 10)
    label2.pack(anchor = "nw", padx = 220, pady = 20) #anchor es para ubicarlo con puntos cardinales

    button_frame = tkinter.Frame(frame1, bg = "black")
    button_frame.pack(anchor = "nw", padx = 20, pady = 10)

    button4 = tkinter.Button(button_frame, text = "Pecho", command = chest_menu   )
    button4.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button4.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button7 = tkinter.Button(button_frame, text = "Biceps", command = biceps_menu   )
    button7.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button7.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame2 = tkinter.Frame(frame1, bg = "black")
    button_frame2.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button5 = tkinter.Button(button_frame2, text = "Espalda", font = 15, relief = "groove", command = back_menu)
    button5.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button5.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button8 = tkinter.Button(button_frame2, text = "Triceps", font = 15, relief = "groove", command = triceps_menu)
    button8.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button8.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button_frame3 = tkinter.Frame(frame1, bg = "black")
    button_frame3.pack(anchor = "sw", padx = 20, pady = (10,0))

    button6 = tkinter.Button(button_frame3, text = "Hombros", command = shoulder_menu    )
    button6.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button6.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button9 = tkinter.Button(button_frame3, text = "Abdominales", command = abs_menu    )
    button9.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button9.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = show_new_window2)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    back_button.pack(pady = 2)


def timer_legs():


    def countdown():
        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo


    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()

        
    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar/reaunudar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = leg_menu,)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)


def deadlift_ruman():
    for widget in frame1.winfo_children():
        widget.destroy()
    timer_legs()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("image1.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)

    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def squats():
    for widget in frame1.winfo_children():
        widget.destroy()

    timer_legs()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("sentadillas.jpg").resize((500,500))  # se pone la imagen y se camvia el tamaño
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def Press():
    for widget in frame1.winfo_children():
        widget.destroy()

    timer_legs()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("presspierna.jpg").resize((500,500))  # se pone la imagen y se camvia el tamaño
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def strides():
    for widget in frame1.winfo_children():
        widget.destroy()

    timer_legs()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("zancadas.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)

    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()
    

def leg_menu():
    for widget in frame1.winfo_children():
        widget.destroy()


    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_legs = tkinter.Button(button_frame_a, text = "Sentadillas", command = squats     )
    button1_legs.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button1_legs.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_legs = tkinter.Button(button_frame_a, text = "Prensa", command = Press      )
    button2_legs.config(bg = "orange", width = 17, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button2_legs.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_legs = tkinter.Button(button_frame_b, text = "Peso muerto rumano", font = 15, relief = "groove", command = deadlift_ruman    )
    button3_legs.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button3_legs.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_legs = tkinter.Button(button_frame_b, text = "Zancadas", font = 15, relief = "groove", command = strides    )
    button4_legs.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button4_legs.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = inf_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    back_button.pack(pady = 2)
 

def calves_timer():
 

    def countdown():

        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  


    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()


    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = calves_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)
    

def calves_raising():

    for widget in frame1.winfo_children():
        widget.destroy()

    calves_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("elevacionesdepie.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def sit_raising():

    for widget in frame1.winfo_children():
        widget.destroy()


    calves_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("pantorrillassentado.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def calves_press():

    for widget in frame1.winfo_children():
        widget.destroy()


    calves_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("calvespress.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        

    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def calves_jumpin():
    for widget in frame1.winfo_children():
        widget.destroy()


    calves_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("calvesjumpin.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)

    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()
    

def calves_menu():

    for widget in frame1.winfo_children():
        widget.destroy()

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_calves = tkinter.Button(button_frame_a, text = "E. de talones de pie",  command= calves_raising    )
    button1_calves.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button1_calves.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_calves = tkinter.Button(button_frame_a, text = "E. de talones sentado", command = sit_raising      )
    button2_calves.config(bg = "orange", width = 17, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button2_calves.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_calves = tkinter.Button(button_frame_b, text = "Elevación en prensa", font = 15, relief = "groove", command= calves_press     )
    button3_calves.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button3_calves.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_calves = tkinter.Button(button_frame_b, text = "Saltos de pantorrilla", font = 15, relief = "groove", command = calves_jumpin    )
    button4_calves.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button4_calves.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = inf_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    back_button.pack(pady = 2)


def gluteus_timer():


    def countdown():

        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  

    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()


    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = gluteus_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)
    

def bridges():

    for widget in frame1.winfo_children():
        widget.destroy()

    gluteus_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("bridges.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def sumo():
    for widget in frame1.winfo_children():
        widget.destroy()


    gluteus_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("sumo.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)

    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def waist_raisin():
    for widget in frame1.winfo_children():
        widget.destroy()


    gluteus_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("waistraisin.jpg").resize((400,600))  
        img_tk = ImageTk.PhotoImage(img)
        
    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def lateral():
    for widget in frame1.winfo_children():
        widget.destroy()


    gluteus_timer()


    def image_window():

        window_image = tkinter.Toplevel() # es para abrir una nueva ventana
        window_image.title("Ejemplos")
        window_image.geometry("500x500+700+100")

        frame_image = tkinter.Frame(window_image, bg="black")
        frame_image.pack(expand=True, fill=tkinter.BOTH)
    
        img = Image.open("lateral.jpg").resize((500,500))  
        img_tk = ImageTk.PhotoImage(img)
        

    # Crear una etiqueta para mostrar la imagen
        label = tkinter.Label(frame_image, image=img_tk)
        label.image = img_tk
        label.pack()


    image_window()


def gluteus_menu():

    for widget in frame1.winfo_children():
        widget.destroy()
    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_calves = tkinter.Button(button_frame_a, text = "Puente", command = bridges     )
    button1_calves.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button1_calves.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_calves = tkinter.Button(button_frame_a, text = "Sentadillas sumo", command = sumo      )
    button2_calves.config(bg = "orange", width = 17, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button2_calves.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_calves = tkinter.Button(button_frame_b, text = "Elevaciones de cadera", font = 15, relief = "groove", command = waist_raisin    )
    button3_calves.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button3_calves.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_calves = tkinter.Button(button_frame_b, text = "Zancadas laterales", font = 15, relief = "groove", command = lateral    )
    button4_calves.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button4_calves.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = inf_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    back_button.pack(pady = 2)

    
def inf_routines_menu():

    for widget in frame1.winfo_children():
        widget.destroy()
    
    label3 = tkinter.Label(frame1, text = "tren inferior", font = 15,relief = "groove",     )
    label3.config(padx = 10)
    label3.pack(anchor = "nw", padx = 220, pady = 20)

    button_frame4 = tkinter.Frame(frame1, bg = "black")
    button_frame4.pack(anchor = "nw", padx = 20, pady = (10,0))

    button10 = tkinter.Button(button_frame4, text = "Pierna", command = leg_menu     )
    button10.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button10.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button11 = tkinter.Button(button_frame4, text = "Pantorrilla", command = calves_menu     )
    button11.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button11.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button_frame5 = tkinter.Frame(frame1, bg = "black")
    button_frame5.pack(anchor = "nw", padx = 20, pady = (10,0))

    button12 = tkinter.Button(button_frame5, text = "Glúteo",  command = gluteus_menu    )
    button12.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    button12.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = show_new_window2)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = ("verdana", 15))
    back_button.pack(side = tkinter.BOTTOM )


def go_back(): #permite regresar al boton de ingresar
    for widget in frame1.winfo_children():
        widget.destroy()
    button1.pack(pady = 200)


frame1 = tkinter.Frame(window, bg = "black")
frame1.config(width = 1000, height = 1000)
frame1.pack(expand = True, fill = tkinter.BOTH)

#etiquette = tkinter.Label(window, text = "Bienvenido a Workout app") #es una etiqueta
#etiquette.pack()  # mostrar en pantalla

button1 = tkinter.Button(frame1, text = "ingresar", font = "Verdana", command = show_new_window)
button1.config(bg = "gold" , width=10, height=2, relief = "groove", bd = 15, cursor = "pirate")
button1.pack(pady = 200)

window.mainloop() #lleva el registro de todo lo que pasa en la ventana
