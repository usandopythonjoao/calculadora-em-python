from tkinter import *
from tkinter import ttk

################# Colors ####################

white_color = "#feffff"
light_gray_color = "#ECEFF1"
light_black_color = "#3b3b3b"

blue_color = "#6f9fbd"
dark_blue_color = "#38576b"

orange_color = '#FFAB40'

red_color = '#ff333a'

green_color = '#6bd66f'

dark_yellow_color = "#ab8918"

################# Window Configuration ####################

window = Tk()
window.title('Calculadora')
window.geometry('235x318')
window.configure(bg=white_color)

################# Style Confguration ####################

style = ttk.Style(window)
style.theme_use("clam")

################# Frames Configuration ####################

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

number_display_frame = Frame(
    window, width=300,
    height=150,
    bg=light_black_color,
    pady=0,
    padx=0,
    relief="flat"
)

number_display_frame.grid(row=1, column=0, sticky=NW)

buttons_frame = Frame(
    window,
    width=300,
    height=340,
    bg=light_black_color,
    pady=0,
    padx=0,
    relief="flat"
)

buttons_frame.grid(row=2, column=0, sticky=NW)

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


# for storing all the expressions that will be evalueted
all_values = ""

# for single value entering
value_text = StringVar()

################# Label ####################

app_screen = Label(number_display_frame, width=16, height=2, textvariable=value_text, padx=7,
                   relief="flat", anchor="e", bd=0, justify=RIGHT, font=('Ivy 18'), bg=dark_blue_color, fg=white_color)
app_screen.place(x=0, y=0)

################# Buttons ####################

b_1 = Button(buttons_frame, text="C", width=11, height=2, bg=white_color, fg=light_black_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: scream_clear())
b_1.place(x=0, y=0)
b_2 = Button(buttons_frame, text="%", width=5, height=2, bg=white_color, fg=light_black_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entering_values('%'))
b_2.place(x=118, y=0)
b_3 = Button(buttons_frame, text="/", width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE, command=lambda: entering_values('/'))
b_3.place(x=177, y=0)

b_4 = Button(buttons_frame, text="7", width=5, height=2, bg=white_color, fg=light_black_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entering_values(7))
b_4.place(x=0, y=52)
b_5 = Button(buttons_frame, text="8", width=5, height=2, bg=white_color, fg=light_black_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entering_values(8))
b_5.place(x=59, y=52)
b_6 = Button(buttons_frame, text="9", width=5, height=2, bg=white_color, fg=light_black_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entering_values(9))
b_6.place(x=118, y=52)
b_7 = Button(buttons_frame, text="*", width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE, command=lambda: entering_values('*'))
b_7.place(x=177, y=52)

b_8 = Button(buttons_frame, text="4", width=5, height=2, bg=white_color, fg=light_black_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entering_values(4))
b_8.place(x=0, y=104)
b_9 = Button(buttons_frame, text="5", width=5, height=2, bg=white_color, fg=light_black_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entering_values(5))
b_9.place(x=59, y=104)
b_10 = Button(buttons_frame, text="6", width=5, height=2, bg=white_color, fg=light_black_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entering_values(6))
b_10.place(x=118, y=104)
b_11 = Button(buttons_frame, text="-", width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
              relief=RAISED, overrelief=RIDGE, command=lambda: entering_values('-'))
b_11.place(x=177, y=104)

b_12 = Button(buttons_frame, text="1", width=5, height=2, bg=white_color, fg=light_black_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entering_values(1))
b_12.place(x=0, y=156)
b_13 = Button(buttons_frame, text="2", width=5, height=2, bg=white_color, fg=light_black_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entering_values(2))
b_13.place(x=59, y=156)
b_14 = Button(buttons_frame, text="3", width=5, height=2, bg=white_color, fg=light_black_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entering_values(3))
b_14.place(x=118, y=156)
b_15 = Button(buttons_frame, text="+", width=5, height=2, bg=orange_color, fg=white_color, font=('Ivy 13 bold'),
              relief=RAISED, overrelief=RIDGE, command=lambda: entering_values('+'))
b_15.place(x=177, y=156)

b_16 = Button(buttons_frame, text="0", width=11, height=2, bg=white_color, fg=light_black_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entering_values(0))
b_16.place(x=0, y=208)
b_17 = Button(buttons_frame, text=".", width=5, height=2, bg=white_color, fg=light_black_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entering_values('.'))
b_17.place(x=118, y=208)
b_18 = Button(buttons_frame, text="=", width=5, height=2, bg=orange_color, fg=white_color, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate())
b_18.place(x=177, y=208)

window.mainloop()
