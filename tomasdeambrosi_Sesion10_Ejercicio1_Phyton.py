'''En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio 
para que deje todo como al principio. Al principio no tiene que haber una opción seleccionada.'''

import tkinter
from tkinter import ttk
from tkinter import IntVar

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=6)

seleccionado = IntVar()

def marcado():
    print(f'Opción {seleccionado.get()} seleccionada')

def reiniciar(event):
    seleccionado.set(None)
    print('Estado: reiniciado')


r1 = ttk.Radiobutton(text='Opción 1', value='1', variable=seleccionado, command=marcado)
r2 = ttk.Radiobutton(text='Opción 2', value='2', variable=seleccionado, command=marcado)
r3 = ttk.Radiobutton(text='Opción 3', value='3', variable=seleccionado, command=marcado)
r4 = ttk.Radiobutton(text='Opción 4', value='4', variable=seleccionado, command=marcado)
r5 = ttk.Radiobutton(text='Opción 5', value='5', variable=seleccionado, command=marcado)


b1 = ttk.Button(window, text='Reiniciar')
b1.bind('<Button-1>', reiniciar)

r1.grid(column=0, row=1, pady=1, padx=1)
r2.grid(column=0, row=2, pady=1, padx=1)
r3.grid(column=0, row=3, pady=1, padx=1)
r4.grid(column=0, row=4, pady=1, padx=1)
r5.grid(column=0, row=5, pady=1, padx=1)

b1.grid(column=1, row=6, pady=1, padx=1)

window.mainloop()


