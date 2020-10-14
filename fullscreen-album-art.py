import tkinter as tk #Tkinter import for GUI
from PIL import ImageTk,Image #PIL import for image manipulation
from time import sleep

#Setups Tkinter GUI
def tkinter_init():
    root = tk.Tk() # root is tkinter obj
    root.geometry(f"{root.winfo_screenheight()}x{root.winfo_screenwidth()}") # sets window size to max screen size
    #root.geometry("500x500")
    root.attributes('-fullscreen', True) # sets to fullscreen mode
    return root # return tk obj

def close(event):
    quit()

def spotify_setup():
    return None

def display_image(root):
    canvas = tk.Canvas(root)
    canvas.pack(expand=True, fill='both')
    img = ImageTk.PhotoImage(Image.open("21.jpg")) #get image
    canvas.create_image(root.winfo_screenheight() // 2,root.winfo_screenwidth() // 2,anchor='center', image=img)
    root.bind('<Escape>', close)
    root.mainloop()


def main():
    root = tkinter_init()
    print(f"{root.winfo_screenheight()}x{root.winfo_screenwidth()}")
    display_image(root)
    

if __name__ == "__main__":
    main()