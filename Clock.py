import pendulum
import tkinter

now = pendulum.now("Europe/Paris")
time=tkinter.Tk()
tie=now


label=tkinter.Label(time , text=tie)
label.pack()


time.mainloop()









