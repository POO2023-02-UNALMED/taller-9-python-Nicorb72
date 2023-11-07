from tkinter import Tk, Button, Entry, StringVar

root = Tk()
root.title("Calculadora POO")
root.resizable(0, 0)
root.geometry("302x259")

numero = ""
valores = StringVar()
operacion = False  

pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"), textvariable=valores)
pantalla.grid(row=0, column=0, columnspan=200, padx=1, pady=0)

boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: num(1)).grid(row=1, column=0, padx=1, pady=1, sticky="w")
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: num(2)).grid(row=1, column=1, padx=1, pady=1, sticky="w")
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: num(3)).grid(row=1, column=2, padx=1, pady=1, sticky="w")
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: num(4)).grid(row=2, column=0, padx=1, pady=1, sticky="w")
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: num(5)).grid(row=2, column=1, padx=1, pady=1, sticky="w")
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: num(6)).grid(row=2, column=2, padx=1, pady=1, sticky="w")
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: num(7)).grid(row=3, column=0, padx=1, pady=1, sticky="w")
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: num(8)).grid(row=3, column=1, padx=1, pady=1, sticky="w")
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: num(9)).grid(row=3, column=2, padx=1, pady=1, sticky="w")

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2", command=lambda: resultado()).grid(row=4, column=0, columnspan=2, padx=1, pady=1, sticky="w")
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=lambda: num(".")).grid(row=4, column=2, padx=1, pady=1, sticky="w")
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: num("+")).grid(row=1, column=3, padx=1, pady=1, sticky="w")
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: num("-")).grid(row=2, column=3, padx=1, pady=1, sticky="w")
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: num("*")).grid(row=3, column=3, padx=1, pady=1, sticky="w")
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: num("/")).grid(row=4, column=3, padx=1, pady=1, sticky="w")

