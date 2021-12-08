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
watchman_frame = Frame(window,relief=SUNKEN,bd=2)
watchman_frame.pack()
watchman_label = Label(watchman_frame,text=':الخفير')
watchman_label.pack()
watchman_input = Entry(watchman_frame,justify=RIGHT)
watchman_input.pack()
# alternative
alternative_frame = Frame(window,relief=SUNKEN,bd=2)
alternative_frame.pack()
alternative_label = Label(alternative_frame,text=':البديل')
alternative_label.pack()
alternative_input = Entry(alternative_frame,justify=RIGHT)
alternative_input.pack()
visitor_name_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_name_frame.place(x=20,y=180)

visit_label_name = Label(visitor_name_frame,text=' :الإسم')
visit_label_name.pack()
visit_input_name = Entry(visitor_name_frame,borderwidth=5,relief=FLAT,justify=RIGHT)
visit_input_name.pack()

# Footer -----------------------






window.mainloop()
