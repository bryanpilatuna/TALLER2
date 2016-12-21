##import turtle
##t= turtle.Pen()
##
##t.forward(50)
##t.left(90)
##t.forward(50)
##t.left(90)
##t.forward(50)
##t.left(90)
##t.forward(50)
##
##
##t.reset()
##for x in range (1,9):
##    t.forward(100)
##    t.left(225)

##
##t.reset()
##for x in range (1,38):
##    t.forward(100)
##    t.left(175)
##
##
##import turtle
##t= turtle.Pen()
##def micuadrado(size):
##    for x in range (1,5):
##        t.forward(size)
##        t.left(90)
##micuadrado(100)
##turtle.getscreen()._root.mainloop()
##
##a=int(input("Ingrese el numero de lados del Triangulo"))
##if(a%2==0):
##    print("Solo funciona para pares")
##    
##else:
##    b=180/a
##    c=180-b
##    import turtle
##    t= turtle.Pen()
##    t.reset()
##    for x in range (a):
##        t.forward(100)
##        t.left(c)
##   
##a=int(input("Ingrese le valor del cuadrado"))
##
##import turtle
##t= turtle.Pen()
##
##def micuadrado(a):
##    for x in range (1,5):
##        t.forward(a)
##        t.left(90)
##micuadrado(a)
##turtle.getscreen()._root.mainloop()


from tkinter import *
tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()

my_image=PhotoImage(file="ball.gif")
canvas.create_image(0,0, anchor=NW,image=my_image)
tk.mainloop()
