import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk,ImageOps

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg




app_data = {
    'original_image': None,
    'processed_image': None
}

def rgb_to_yiq(image):
    mat = np.array([[0.299, 0.587, 0.114],
                    [0.596, -0.274, -0.322],    
                    [0.211, -0.523, 0.312]])
    return image @ mat.T

def yiq_to_rgb(image):
    mat = np.array([[1, 0.956, 0.621],
                    [1, -0.272, -0.647],
                    [1, -1.106, 1.703]])
    return image @ mat.T    

#Funcion que carga imagen

def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    if file_path:
       image = Image.open(file_path)
       display_image(image, original_canvas)
       app_data['original_image'] = image


#Funcion que procesa imagen
def process_image():
    if app_data['original_image']:
        gray_image = ImageOps.grayscale(app_data['original_image'])
        display_image(gray_image, processed_canvas)

def display_image(image, widget):
    resided = image.resize((300, 300))
    tk_image = ImageTk.PhotoImage(resided)
    widget.config(image=tk_image)
    widget.image = tk_image 

#Crear la ventana PRINCIPAL

root = tk.Tk()
root.title("PROCESAMIENTO DE IMAGENES")
root.geometry("800x400")

#frame principal que contiene los demas frames

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

#Parte superior que contien los frames izquierdo y derecho

top_frame = tk.Frame(main_frame)   
top_frame.pack(side="top", fill="both", expand=True)



botton_frame = tk.Frame(main_frame, height=40, bg="lightblue")
botton_frame.pack(side="bottom", fill="x", expand=True)

center_button_frame = tk.Frame(botton_frame, bg="lightblue")
center_button_frame.pack(side="left", fill="both", expand=True)

#Frame izquierdo y derecho
left_frame = tk.Frame(top_frame, width=400, height=400, bg="lightgray")
left_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(top_frame, width=400, height=400)
right_frame.pack(side="right", fill="both", expand=True)

load_button = tk.Button(center_button_frame, text="Cargar Imagen",command=load_image)
load_button.pack(side="left",pady=10)

process_button = tk.Button(center_button_frame, text="Procesar Imagen",command=process_image)
process_button.pack(side="left",pady=10)   

rgb_to_yiq_button = tk.Button(center_button_frame, text="RGB --> YIQ")
rgb_to_yiq_button.pack(side="left",pady=10) 


original_canvas = tk.Label(left_frame)
original_canvas.pack()

processed_canvas = tk.Label(right_frame)
processed_canvas.pack()

#Ejecutar la ventana
root.mainloop()
