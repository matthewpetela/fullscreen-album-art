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

def resize_image(img, root):
    min_size = min(root.winfo_screenheight(), root.winfo_screenwidth())
    return img.resize((min_size, min_size))

def center_image(img, root):
    width = (root.winfo_screenwidth() - img.width) // 2
    height = (root.winfo_screenheight() - img.height) // 2
    return width, height

def display_image(root):
    canvas = tk.Canvas(root)
    canvas.config(background="black") # change background to black
    canvas.pack(expand=True, fill='both') # make canvas entire tk
    img = Image.open("21.jpg") # get image
    img = resize_image(img, root) if img.height != root.winfo_screenheight() and img.width != root.winfo_screenwidth() else img
    width, height = center_image(img, root)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(width, height, image=img, anchor='nw')
    root.bind('<Escape>', close)
    root.mainloop()


def main():
    root = tkinter_init()
    #print(f"{root.winfo_screenheight()}x{root.winfo_screenwidth()}")
    display_image(root)
    

if __name__ == "__main__":
    main()