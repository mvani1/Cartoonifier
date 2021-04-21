import tkinter as tk
from Cartoon import make_cartoon
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk
from PIL import Image

import cv2




def save_cartoon(file_path, cartoon_img):
    where = filedialog.asksaveasfilename(
        filetypes=(
            ("JPEG Files", "*.jpg"),
            ("PNG Files", "*.png"),
            ("All Files", "*.*"),
        ),
        defaultextension=file_path[-4:],
    )
    cartoon_img.save(where)


def show_save_button(file_path, cartoon_img):
    save_b = Button(
        top,
        text="Save to computer",
        command=lambda: save_cartoon(file_path, cartoon_img),
        padx=10,
        pady=5,
    )
    save_b.configure(
        highlightbackground="grey",
        background="grey",
        foreground="black",
        font=("arial", 10, "bold"),
    )

    save_b.place(relx=0.69, rely=0.86)


def convert(file_path):
    '''
    Approach : 1. Convert to GrayScale
           2. Blur it
           3. Extract Edges
           4. Blur Colored IMage
           5. Add mask with edges
    '''
    cartoon = make_cartoon(file_path)

    # Changing to Color again
    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
    cartoon_img = Image.fromarray(cartoon)
    cartoon_img.thumbnail(((top.winfo_width() / 1.8), (top.winfo_height() / 1.8)))
    im = ImageTk.PhotoImage(cartoon_img)
    label = Label(top, image=im)
    label.image = im
    # displaying it to right
    label.pack(side="right", expand="yes")
    show_save_button(file_path, cartoon_img)


def show_convert_button(file_path):
    # button for converting the uploaded image into cartoon
    convert_b = Button(
        top, text="Cartoonify me", command=lambda: convert(file_path), padx=10, pady=5
    )
    convert_b.configure(
        highlightbackground="grey",
        background="grey",
        foreground="black",
        font=("arial", 10, "bold"),
    )
    convert_b.place(relx=0.79, rely=0.46)


def upload_image():
    # path of image to process
    file_path = filedialog.askopenfilename()
    # open it
    uploaded = Image.open(file_path)
    uploaded.thumbnail(((top.winfo_width() / 1.25), (top.winfo_height() / 2.25)))
    im = ImageTk.PhotoImage(uploaded)
    label = Label(top, image=im)
    label.image = im
    label.pack(side="left", expand="yes")
    show_convert_button(file_path)

def main():

    global top
    # Initialising tkinter Object
    top  = Tk()
    top.geometry("1000x600")
    top.title("Cartoonifier")

    top.iconbitmap(
        "/Users/mehulvani/Python Cartoonifier/Lib/Pictures/df_icon.ico"
    )
    top.configure(background="grey")
    # Used Tkinter To create GUI button
    upload = Button(top, text="Upload an image", command=upload_image, padx=5, pady=5)
    upload.configure(
        highlightbackground="grey",
        background="grey",
        foreground="black",
        font=("arial", 10, "bold"),
    )
    upload.place(relx=0.44, rely=0.86)

    top.mainloop()

if __name__ == '__main__':
    main()

