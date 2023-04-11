from tkinter import *

root = Tk()
root.title("Calculadora")


#Entrada
entrada = Entry(root, font=('Curier 20'))
entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#Botones

boton1 = Button(root, text='1', width=5, height=2)
boton2 = Button(root, text='2', width=5, height=2)
boton3 = Button(root, text='3', width=5, height=2)
boton4 = Button(root, text='4', width=5, height=2)
boton5 = Button(root, text='5', width=5, height=2)
boton6 = Button(root, text='6', width=5, height=2)
boton7 = Button(root, text='7', width=5, height=2)
boton8 = Button(root, text='8', width=5, height=2)
boton9 = Button(root, text='9', width=5, height=2)
boton0 = Button(root, text='0', width=15, height=2)

boton_borrar = Button(root, text='DEL', width=5, height=2)
boton_parentesis1 = Button(root, text='(', width=5, height=2)
boton_parentesis2 = Button(root, text=')', width=5, height=2)
boton_punto = Button(root, text='.', width=5, height=2)

boton_sumar = Button(root, text='+', width=5, height=2)
boton_restar = Button(root, text='-', width=5, height=2)
boton_multiplicar = Button(root, text='*', width=5, height=2)
boton_dividir = Button(root, text='/', width=5, height=2)
boton_igual = Button(root, text='=', width=5, height=2)

#poner los botones

boton_borrar.grid(row=1,column=0,padx=5,pady=5)
boton_parentesis1.grid(row=1,column=1,padx=5,pady=5)
boton_parentesis2.grid(row=1,column=2,padx=5,pady=5)
boton_dividir.grid(row=1,column=3,padx=5,pady=5)

boton7.grid(row=2,column=0,padx=5,pady=5)
boton8.grid(row=2,column=1,padx=5,pady=5)
boton9.grid(row=2,column=2,padx=5,pady=5)
boton_multiplicar.grid(row=2,column=3,padx=5,pady=5)

boton4.grid(row=3,column=0,padx=5,pady=5)
boton5.grid(row=3,column=1,padx=5,pady=5)
boton6.grid(row=3,column=2,padx=5,pady=5)
boton_restar.grid(row=3,column=3,padx=5,pady=5)

boton1.grid(row=4,column=0,padx=5,pady=5)
boton2.grid(row=4,column=1,padx=5,pady=5)
boton3.grid(row=4,column=2,padx=5,pady=5)
boton_sumar.grid(row=4,column=3,padx=5,pady=5)

boton0.grid(row=5,column=0,padx=5,pady=5, columnspan= 2)
boton_punto.grid(row=5,column=2,padx=5,pady=5)
boton_igual.grid(row=5,column=3,padx=5,pady=5)


root.mainloop()