from Tkinter import *          
window = Tk()                    

lista = 'Rick Negan Michonne Daryl'.split()
listb = Listbox(window)           
for item in lista:
	listb.insert(0,item)                

listb.pack()                   
window.mainloop()                 