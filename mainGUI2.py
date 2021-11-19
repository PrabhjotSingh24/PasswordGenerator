from main import *
from tkinter import *


def generate_pass():
    password = password_generator(
        0 if pass_length_var.get() == 'This box is important!' else int(pass_length_var.get()),
        custom_characters_var.get(),
        True if (special_characters_var.get()).lower() == "yes" else False
    )

    def save_password():
        with open('passwords.txt', 'a') as f:
            f.write(f"Username: {username_var.get()} Password: {password}\n")
    pass_window = Toplevel()
    pass_window.iconbitmap('pg.ico')
    pass_window.title("Password")
    pass_window.geometry('250x100')
    pass_entry = Entry(pass_window, font=(None, 14))
    pass_entry.insert(0, password)
    pass_entry.pack(pady=10)
    save = Button(pass_window, text="Save Password", font=(
        None, 14), command=save_password)
    save.pack()


try:
    root = Tk()
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.title("Password Generator")
    root.iconbitmap('pg.ico')
    root.geometry(
        f'417x220+{(screen_width-417)//2}+{(screen_height-220)//2}'
    )
    # Main frame holding all the children
    main_frame = Frame(root)
    main_frame.pack()

    # label frame for all the labels
    labels_frame = Frame(main_frame)
    labels_frame.grid(row=0, column=0)

    # entries frame for all the entry boxes
    entries_frame = Frame(main_frame)
    entries_frame.grid(row=0, column=1)

    # Buttons
    button_frame = Frame(root)
    button_frame.pack()

    get_password = Button(button_frame, text="Get Password",
                          font=(None, 14), command=generate_pass)
    get_password.grid(row=0, column=0, padx=5)

    # Labels
    pass_length = Label(labels_frame, text="Password Length: ",
                        font=(None, 14), justify=LEFT)
    pass_length.pack(anchor='w')

    custom_characters = Label(
        labels_frame, text="Custom Characters: ", font=(None, 14), justify=LEFT)
    custom_characters.pack(pady=10, anchor='w')

    special_characters = Label(
        labels_frame, text="Include Special\nCharacters? ", font=(None, 14), justify=LEFT)
    special_characters.pack(anchor='w')

    username = Label(labels_frame, text="Username: ",
                     font=(None, 14), justify=LEFT)
    username.pack(anchor='w')

    # Entries
    pass_length_var = StringVar()
    custom_characters_var = StringVar()
    special_characters_var = StringVar()
    username_var = StringVar()
    special_characters_var.set("No")
    special_characters_var_options = ["Yes", "No"]

    pass_length_entry = Entry(
        entries_frame, textvariable=pass_length_var, font=(None, 14))
    pass_length_entry.pack(anchor='e')

    custom_characters_entry = Entry(
        entries_frame, textvariable=custom_characters_var, font=(None, 14))
    custom_characters_entry.pack(anchor='e', pady=15)

    special_characters_options = OptionMenu(
        entries_frame, special_characters_var, *special_characters_var_options)
    special_characters_options.pack(anchor='w')

    username_entry = Entry(
        entries_frame, textvariable=username_var, font=(None, 14))
    username_entry.pack(anchor='e', pady=15)

    root.mainloop()
except:
    print("There is something wrong I can feel it...")