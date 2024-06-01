import json
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

def cargar_contraseñas():
    try:
        with open("contraseñas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_contraseñas(contraseñas):
    with open("contraseñas.json", "w") as archivo:
        json.dump(contraseñas, archivo)

def mostrar_contraseñas(contraseñas):
    if contraseñas:
        contraseñas_str = "\n".join(f"{sitio}: {contraseña}" for sitio, contraseña in contraseñas.items())
        messagebox.showinfo("Contraseñas", contraseñas_str)
    else:
        messagebox.showinfo("Contraseñas", "No tienes ninguna contraseña guardada.")

def añadir_contraseña(contraseñas):
    sitio = simpledialog.askstring("Sitio web", "Introduce el sitio web:")
    contraseña = simpledialog.askstring("Contraseña", "Introduce la contraseña:", show='*')
    if sitio and contraseña:
        contraseñas[sitio] = contraseña
        guardar_contraseñas(contraseñas)
        messagebox.showinfo("Éxito", "Contraseña añadida correctamente.")
    else:
        messagebox.showwarning("Advertencia", "Debes introducir tanto el sitio web como la contraseña.")

def eliminar_contraseña(contraseñas):
    sitio = simpledialog.askstring("Eliminar Contraseña", "Introduce el sitio web:")
    if sitio in contraseñas:
        del contraseñas[sitio]
        guardar_contraseñas(contraseñas)
        messagebox.showinfo("Éxito", "Contraseña eliminada correctamente.")
    else:
        messagebox.showwarning("Advertencia", "No se encontró ninguna contraseña para ese sitio.")

def main():
    contraseñas = cargar_contraseñas()

    root = tk.Tk()
    root.title("Gestor de Contraseñas")
    root.configure(bg='lightgray')

    # Cargar la imagen de fondo
    imagen_fondo = Image.open("images.png")
    imagen_fondo = imagen_fondo.resize((300, 400), Image.LANCZOS)
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

    # Crear un Label con la imagen de fondo
    fondo_label = tk.Label(root, image=imagen_fondo_tk)
    fondo_label.place(relwidth=1, relheight=1)

    frame = tk.Frame(root, bg='lightgray')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    btn_style = {
        'bg': 'cyan',
        'fg': 'black',
        'font': ('Helvetica', 12),
        'width': 20,
        'height': 2
    }

    mostrar_btn = tk.Button(frame, text="Mostrar Contraseñas", command=lambda: mostrar_contraseñas(contraseñas), **btn_style)
    mostrar_btn.pack(pady=10)

    añadir_btn = tk.Button(frame, text="Añadir Contraseña", command=lambda: añadir_contraseña(contraseñas), **btn_style)
    añadir_btn.pack(pady=10)

    eliminar_btn = tk.Button(frame, text="Eliminar Contraseña", command=lambda: eliminar_contraseña(contraseñas), **btn_style)
    eliminar_btn.pack(pady=10)

    salir_btn = tk.Button(frame, text="Salir", command=root.quit, **btn_style)
    salir_btn.pack(pady=10)

    # Añadir la etiqueta con el texto y la bandera en la esquina inferior derecha
    credito_label = tk.Label(root, text="Hecho por Saravia, Juan Manuel 🇦🇷", bg='lightgray', fg='black', font=('Helvetica', 10))
    credito_label.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    root.mainloop()

if __name__ == "__main__":
    main()