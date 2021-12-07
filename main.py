from tkinter import *
# Variabes ------------------------
right_position = 780
center_position = 400
left_position=20
input_width = 3
font_title = ('Arial',24,'normal')
# Window --------------------------
window=Tk()
window.title('Visitors GN Temacine')
window.minsize(800,600)
window.maxsize(800,780)
# Header --------------------------
title = Label(text="برنامج المواطنين الزائرين للفرقة",font=font_title)
title.pack()
# Container -----------------------
# date
day_label = Label(text=':اليوم')
day_label.place(x=(left_position +220), y=40)
day_input = Spinbox(window,from_=1,to=31,width=input_width)
day_input.place(x=(left_position +180), y=40)
month_label = Label(text=':الشهر')
month_label.place(x=(left_position +140), y=40)
month_input = Spinbox(window,from_=1,to=12,width=input_width)
month_input.place(x=(left_position +100), y=40)
year_label = Label(text=':السنة')
year_label.place(x=(left_position +60), y=40)
year_input = Spinbox(window,from_=1962,to=2090,width=(input_width * 2))
year_input.place(x=(left_position + 10) , y=40)
# watchman
watchman_label = Label(text=':الخفير')
watchman_label.pack()
watchman_input = Entry(window,justify=RIGHT)
watchman_input.pack()
# alternative
alternative_label = Label(text=':البديل')
alternative_label.pack()
alternative_input = Entry(window,justify=RIGHT)
alternative_input.pack()


# Footer -----------------------






window.mainloop()
