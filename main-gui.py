import config
import cv2
import PIL.Image, PIL.ImageTk
import target
from tkinter import *
from tkinter import messagebox

# Create menu bar
def create_menu_bar(window):
    menu_bar = Menu(window)
    # File menu
    menu_file = Menu(menu_bar, tearoff=0)
    menu_file.add_command(label="Calibrate", underline=0, accelerator="CTRL+P", command=target.set_cornerpoints_gui)
    menu_file.add_separator()
    menu_file.add_command(label="Exit", underline=1, command=window.quit)
    menu_bar.add_cascade(label="File", underline=0, menu=menu_file)
    # Help menu
    menu_help = Menu(menu_bar, tearoff=0)
    menu_help.add_command(label="About...", command=show_about)
    menu_bar.add_cascade(label="Help", underline=0, menu=menu_help)
    # Binding controls
    window.bind_all("<Control-p>", lambda x: target.set_cornerpoints_gui())
    # Add menu bar to the window
    window.config(menu=menu_bar)

def read_frame():
    # Recuperation des points de reference
    corner_points = target.get_cornerpoints()

    # Capture the video frame by frame
    success, frame = config.source.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    if success:
        if not corner_points:
            # On récupère l'image originale
            target_frame = frame
            main_window.title("ACM10 - Webcam")
        else:
            # On récupère l'image traitée
            target_frame = target.processing(frame, corner_points)
            main_window.title("ACM10 - Cible temp réel")

        # Capture the latest frame and transform to image
        captured_image = PIL.Image.fromarray(target_frame)
        # Convert captured image to photoimage
        photo_image = PIL.ImageTk.PhotoImage(image=captured_image)
        # Displaying photoimage in the label
        video_label.photo_image = photo_image
        # Configure image in the label
        video_label.configure(image=photo_image)
        # Repeat the same process after every 10ms
        video_label.after(10, read_frame)
    else:
        # Placer un label avec le message d'erreur
        print("Erreur de lecture de la source...")

def show_about():
    messagebox.showinfo("About", "ACM10 - https://github.com/Narmos/AC10M")
    
# Create the main window
main_window = Tk()
main_window.minsize(config.target_width, config.target_height)
main_window.title("ACM10")
# Bind the window with Escape keyboard to quit app whenever pressed
main_window.bind('<Escape>', lambda e: main_window.quit())

# Create menu
create_menu_bar(main_window)

# Create a label and display it on window
video_label = Label(main_window)
video_label.pack()

# Read the video
read_frame()

# Create an infinite loop for displaying window on screen
main_window.mainloop()