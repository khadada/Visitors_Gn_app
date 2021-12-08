from tkinter import *
# Variabes ------------------------
right_position = 780
center_position = 400
left_position=20
input_width = 3
font_title = ('Arial',24,'normal')
bg_color = "#fbfbfb"
# Window --------------------------
window=Tk()
window.configure(background = bg_color)
window.title('Visitors GN Temacine')
window.minsize(800,700)
window.maxsize(800,800)
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
visit_input_name = Entry(visitor_name_frame,borderwidth=5,relief=FLAT,justify=CENTER)
visit_input_name.pack()


visitor_family_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_family_frame.place(x=420,y=180)
visit_label_family_n = Label(visitor_family_frame,text=' :اللقب')
visit_label_family_n.pack()
visit_input_family_n = Entry(visitor_family_frame,borderwidth=5,relief=FLAT,justify=CENTER)
visit_input_family_n.pack()


visitor_birthday_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_birthday_frame.place(x=240,y=180)
visit_label_birthday = Label(visitor_birthday_frame,text=' :تاريخ الميلاد')
visit_label_birthday.pack()
visit_input_birthday = Entry(visitor_birthday_frame,borderwidth=5,relief=FLAT,justify=CENTER)
visit_input_birthday.pack()



visitor_birth_place_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_birth_place_frame.place(x=40,y=180)
visit_label_birth_place = Label(visitor_birth_place_frame,text=' :مكان الميلاد')
visit_label_birth_place.pack()
visit_input_birth_place = Entry(visitor_birth_place_frame,borderwidth=5,relief=FLAT,justify=CENTER)
visit_input_birth_place.pack()



visitor_parents_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_parents_frame.place(x=600,y=280)
visit_label_parents = Label(visitor_parents_frame,text=' :الأب والأم')
visit_label_parents.pack()
visit_input_parents = Entry(visitor_parents_frame,borderwidth=5,relief=FLAT,justify=CENTER)
visit_input_parents.pack()


visitor_job_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_job_frame.place(x=420,y=280)
visit_label_job = Label(visitor_job_frame,text=' :المهنة')
visit_label_job.pack()
visit_input_job = Entry(visitor_job_frame,borderwidth=5,relief=FLAT,justify=CENTER)
visit_input_job.pack()



visitor_address_frame = Frame(window,relief=SUNKEN,bd=2,width=80)
visitor_address_frame.place(x=240,y=280)
visit_label_adress = Label(visitor_address_frame,text=' :الساكن بـ')
visit_label_adress.pack()
visit_input_adress = Entry(visitor_address_frame,borderwidth=5,relief=FLAT,justify=CENTER)
visit_input_adress.pack()




visitor_phone_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_phone_frame.place(x=40,y=280)
visit_label_phone = Label(visitor_phone_frame,text=' :رقم الهاتف ')
visit_label_phone.pack()
visit_input_phone = Entry(visitor_phone_frame,borderwidth=5,relief=FLAT,justify=CENTER)
visit_input_phone.pack()



visitor_ident_card_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_ident_card_frame.place(x=600,y=380)
visit_label_ident_card = Label(visitor_ident_card_frame,text=' :بطاقة الهوية ')
visit_label_ident_card.pack()
visit_input_ident_card = Listbox(visitor_ident_card_frame,height=1,justify=CENTER)
visit_input_ident_card.insert(1,"بطاقة التعريف الوطنية")
visit_input_ident_card.insert(2,"رخصة السياقة")
visit_input_ident_card.insert(3,"جواز السفر ")
visit_input_ident_card.pack()



visitor_card_number_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_card_number_frame.place(x=420,y=380)
visit_label_card_number = Label(visitor_card_number_frame,text=' :الحاملة لرقم')
visit_label_card_number.pack()
visit_input_card_number = Entry(visitor_card_number_frame,borderwidth=5,relief=FLAT,justify=CENTER)
visit_input_card_number.pack()



visitor_date_card_frame = Frame(window,relief=SUNKEN,bd=2,width=80)
visitor_date_card_frame.place(x=240,y=380)
visit_label_date_card = Label(visitor_date_card_frame,text=' :الصادرة بتاريخ')
visit_label_date_card.pack()
visit_input_date_card = Entry(visitor_date_card_frame,borderwidth=5,relief=FLAT,justify=CENTER)
visit_input_date_card.pack()



visitor_card_source_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_card_source_frame.place(x=40,y=380)
visit_label_card_source = Label(visitor_card_source_frame,text=' : السلطة الصادرة ')
visit_label_card_source.pack()
visit_input_card_source = Entry(visitor_card_source_frame,borderwidth=5,relief=FLAT,justify=CENTER)
visit_input_card_source.pack()




visitor_case_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_case_frame.place(x=600,y=480)
visit_label_case = Label(visitor_case_frame,text=' :سبب الزيارة ')
visit_label_case.pack()
visit_input_case = Listbox(visitor_case_frame,height=1,justify=CENTER)
visit_input_case.insert(1,"تقديم شكوى")
visit_input_case.insert(2,"تبليغ ")
visit_input_case.insert(3,"إستفسار ")
visit_input_case.insert(4,"عمل ")
visit_input_case.insert(5,"زيارة ")
visit_input_case.pack()

visitor_detail_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
visitor_detail_frame.place(x=40,y=480)
visit_label_detail = Label(visitor_detail_frame,text=' : التحليل ')
visit_label_detail.pack()
text = Text(visitor_detail_frame,width=63, height= 6,spacing1=2,spacing2=2,spacing3=2,padx=10)
text.tag_configure("right",justify = 'r')
text.tag_add("r",1.0, 'end')
text.insert(INSERT, "أكتب التفاصيل هنا")
text.pack()



submit_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
submit_frame.place(x=600,y=530)
submit_button = Button(submit_frame,text='معاينة',borderwidth=5,justify=CENTER,padx=40,pady=5,bg='orange')
submit_button.pack()


view_frame = Frame(window,relief=SUNKEN,bd=2,width=2)
view_frame.place(x=600,y=580)
view_button = Button(view_frame,text='موافق',borderwidth=5,justify=CENTER,padx=40,pady=5,bg='green',fg="white")
view_button.pack()




# Footer -----------------------






window.mainloop()
