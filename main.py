from tkinter import *
from tkinter import ttk

################# cores ###############
co1 = "#feffff"  # white/branca
co2 = "#6f9fbd"  # blue/azul
co3 = "#38576b"  # valor

fundo = "#3b3b3b"
co10 ="#ECEFF1"

cor1='#FFAB40'
cor2='#ff333a'
cor3='#6bd66f'
cor4="#ab8918"

janela = Tk()
janela.title('')
janela.geometry('235x318')
janela.configure(bg=co1)


style = ttk.Style(janela)
style.theme_use("clam")

################# Frames ####################

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame_score = Frame(janela, width=300, height=56,bg=co3, pady=0, padx=0, relief="flat",)
frame_score.grid(row=1, column=0, sticky=NW)

frame_quadros = Frame(janela, width=300, height=340,bg=fundo, pady=0, padx=0, relief="flat",)
frame_quadros.grid(row=2, column=0, sticky=NW)


################# Funções ####################

def entering_values(event):
	global all_values
	all_values = all_values + str(event)
	value_text.set(all_values)

def calculate():
	global all_values
	result = str(eval(all_values))
	value_text.set(result)
	all_values = ""

def scream_clear(): 
    global all_values
    all_values = "" 
    value_text.set("")

#for storing all the expressions that will be evalueted
all_values = "" 
# for single value entering
value_text = StringVar()

################# Label ####################

app_scream = Label(frame_score,width=16,height=2,textvariable = value_text , padx=7, relief="flat", anchor="e",bd=0, justify=RIGHT, font=('Ivy 18 '), bg='#37474F', fg=co1)
app_scream.place(x=0, y=0)

################# Buttons ####################

b_1 = Button(frame_quadros, text="C", width=11, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: scream_clear())
b_1.place(x=0, y=0)
b_2 = Button(frame_quadros, text="%", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('%'))
b_2.place(x=118, y=0)
b_3 = Button(frame_quadros, text="/", width=5, height=2, bg=cor1, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('/'))
b_3.place(x=177, y=0)

b_4 = Button(frame_quadros, text="7", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(7))
b_4.place(x=0, y=52)
b_5 = Button(frame_quadros, text="8", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(8))
b_5.place(x=59, y=52)
b_6 = Button(frame_quadros, text="9", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(9))
b_6.place(x=118, y=52)
b_7 = Button(frame_quadros, text="*", width=5, height=2, bg=cor1, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('*'))
b_7.place(x=177, y=52)

b_8 = Button(frame_quadros, text="4", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(4))
b_8.place(x=0, y=104)
b_9 = Button(frame_quadros, text="5", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(5))
b_9.place(x=59, y=104)
b_10 = Button(frame_quadros, text="6", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(6))
b_10.place(x=118, y=104)
b_11 = Button(frame_quadros, text="-", width=5, height=2, bg=cor1, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('-'))
b_11.place(x=177, y=104)

b_12 = Button(frame_quadros, text="1", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(1))
b_12.place(x=0, y=156)
b_13 = Button(frame_quadros, text="2", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(2))
b_13.place(x=59, y=156)
b_14 = Button(frame_quadros, text="3", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(3))
b_14.place(x=118, y=156)
b_15 = Button(frame_quadros, text="+", width=5, height=2, bg=cor1, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('+'))
b_15.place(x=177, y=156)

b_16 = Button(frame_quadros, text="0", width=11, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values(0))
b_16.place(x=0, y=208)
b_17 = Button(frame_quadros, text=".", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entering_values('.'))
b_17.place(x=118, y=208)
b_18 = Button(frame_quadros, text="=", width=5, height=2, bg=cor1, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: calculate())
b_18.place(x=177, y=208)

janela.mainloop()
