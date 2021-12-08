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
watchman_input = Entry(watchman_frame,justify=CENTER,borderwidth=5,relief=FLAT)
watchman_input.pack()
# alternative
alternative_frame = Frame(window,relief=SUNKEN,bd=2)
alternative_frame.pack()
alternative_label = Label(alternative_frame,text=':البديل')
alternative_label.pack()
alternative_input = Entry(alternative_frame,justify=CENTER,borderwidth=5,relief=FLAT)
alternative_input.pack()


visitor_name_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_name_frame.place(x=600,y=180)
visit_label_name = Label(visitor_name_frame,text=' :الإسم')
visit_label_name.pack()
visit_input_name = Entry(visitor_name_frame,borderwidth=5,relief=FLAT,justify=RIGHT)
visit_input_name.pack()


visitor_family_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_family_frame.place(x=420,y=180)
visit_label_family_n = Label(visitor_family_frame,text=' :اللقب')
visit_label_family_n.pack()
visit_input_family_n = Entry(visitor_family_frame,borderwidth=5,relief=FLAT,justify=RIGHT)
visit_input_family_n.pack()


visitor_birthday_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_birthday_frame.place(x=240,y=180)
visit_label_birthday = Label(visitor_birthday_frame,text=' :تاريخ الميلاد')
visit_label_birthday.pack()
visit_input_birthday = Entry(visitor_birthday_frame,borderwidth=5,relief=FLAT,justify=RIGHT)
visit_input_birthday.pack()



visitor_birth_place_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_birth_place_frame.place(x=40,y=180)
visit_label_birth_place = Label(visitor_birth_place_frame,text=' :مكان الميلاد')
visit_label_birth_place.pack()
visit_input_birth_place = Entry(visitor_birth_place_frame,borderwidth=5,relief=FLAT,justify=RIGHT)
visit_input_birth_place.pack()



visitor_parents_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_parents_frame.place(x=600,y=280)
visit_label_parents = Label(visitor_parents_frame,text=' :الأب والأم')
visit_label_parents.pack()
visit_input_parents = Entry(visitor_parents_frame,borderwidth=5,relief=FLAT,justify=RIGHT)
visit_input_parents.pack()


visitor_job_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_job_frame.place(x=420,y=280)
visit_label_job = Label(visitor_job_frame,text=' :المهنة')
visit_label_job.pack()
visit_input_job = Entry(visitor_job_frame,borderwidth=5,relief=FLAT,justify=RIGHT)
visit_input_job.pack()

visitor_adress_frame = Frame(window,relief=SUNKEN,bd=2,width=80)
visitor_adress_frame.place(x=240,y=280)
visit_label_adress = Label(visitor_adress_frame,text=' :الساكن بـ')
visit_label_adress.pack()
visit_input_adress = Entry(visitor_adress_frame,borderwidth=5,relief=FLAT,justify=RIGHT)
visit_input_adress.pack()




visitor_phone_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_phone_frame.place(x=40,y=280)
visit_label_phone = Label(visitor_phone_frame,text=' :رقم الهاتف ')
visit_label_phone.pack()
visit_input_phone = Entry(visitor_phone_frame,borderwidth=5,relief=FLAT,justify=RIGHT)
visit_input_phone.pack()
# Footer -----------------------






window.mainloop()
