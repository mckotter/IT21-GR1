#############
# Kiirold Miirold KOrter
# 15.03.2022
# UL 6
#############
import tkinter as tk
from tkinter import *


#Aken
aken = tk.Tk()
aken.title('Joonistamine')
louend = Canvas(aken, width=500, height=500)
louend.pack()
#louend
louend.create_rectangle(15, 20, 200, 120, fill='red', )
louend.create_line(90, 20, 90, 120, fill='white', width=20)
louend.create_line(15, 70, 200, 70, fill='white', width=20)
#pildi lisamine 
minu_pilt = PhotoImage(file='denmark.PNG')
louend.create_image(15, 150, anchor=NW, image=minu_pilt)
aken.mainloop()