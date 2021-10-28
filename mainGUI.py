from tkinter import *
from main import password_generator

try:
    root=Tk()
    screen_width,screen_height=root.winfo_screenwidth(),root.winfo_screenheight()
    root.title("Password Generator")
    root.iconbitmap('pg.ico')
    root.geometry(
        f'417x200+{(screen_width-417)//2}+{(screen_height-200)//2}'
    )

    label_frame=Frame(root)
    label_frame.grid(row=0,column=0,padx=3)

    entries_frame=Frame(root)
    entries_frame.grid(row=0,column=1)

    #Labels
    pass_length_label=Label(label_frame,text="Password Length: ",font=(None,14),    justify=LEFT)
    pass_length_label.pack(anchor='w')

    custom_characters_label=Label(label_frame,text="Custom Characters: ",font=  (None,14),justify=LEFT)
    custom_characters_label.pack(anchor='w',pady=3)

    special_c_label=Label(label_frame,text="""Include Special
    Characters?""",font=(None,14),justify=LEFT)
    special_c_label.pack(anchor='w')

    #Entries
    pass_length_var=StringVar()
    custom_characters_var=StringVar()
    special_c_var=StringVar()
    special_c_var.set('yes')
    options=['yes','no']

    pass_length_entry=Entry(entries_frame,font=(None,14),   textvariable=pass_length_var)
    pass_length_entry.insert(0, 'This box is important!')
    pass_length_entry.pack(anchor="e")

    custom_characters_entry=Entry(entries_frame,font=(None,14), textvariable=custom_characters_var)
    custom_characters_entry.pack(anchor="e",pady=14)

    special_c_menu=OptionMenu(entries_frame,special_c_var,*options)
    special_c_menu.pack()

    #Password Generation
    def generate():
        password=password_generator(
        0 if pass_length_var.get()=='This box is important!' else int(pass_length_var.get()),
        custom_characters_var.get(),
        True if special_c_var.get()=="yes" else False
        )

        pass_window=Toplevel()
        pass_window.iconbitmap('pg.ico')
        pass_window.title("Password")
        pass_window.geometry('250x50')
        pass_entry=Entry(pass_window,font=(None,14))
        pass_entry.insert(0, password)
        pass_entry.pack()

    #Buttons
    get_pass=Button(root,text="Get Password",font=(None,14),command=generate)
    get_pass.place(x=137,y=300//2)



    root.mainloop()
except:
    print("Something Went Wrong!","""Please run the program again if you didn't changed anything""",sep='\n')

