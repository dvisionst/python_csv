from tkinter import *
from tkinter import messagebox

choice = ""
procedure = ""
test_runs = ""
test_type = ""

def test_procedures():
    global procedure, test_type
    val = group_1.get()
    if val == 1:
        procedure = "WLTP"
        test_type = 'w'
    elif val == 2:
        procedure = "NEDC"
        test_type = 'n'
    return procedure


def run_type():
    global choice, test_runs
    val = group_2.get()
    if val == 1:
        choice = "Splits"
        test_runs = 'y'
    elif val == 2:
        choice = "Singles"
        test_runs = 'n'
    return choice


def message():
    result = messagebox.askyesno("Confirmation", f"You selected {test_procedures()} and {run_type()}")
    if result:
        window.destroy()


window = Tk()
window.title("APG Coastdown Processor")
window.config(bg='#47B5FF')
window.geometry('500x450')

canvas = Canvas(width=350, height=300, highlightthickness=0, bg='#47B5FF')
logo = PhotoImage(file="Capture.PNG")
canvas.create_image(200, 100, image=logo)
canvas.place(x=50, y=0)
canvas.create_text(200, 275, text="Please Select Test Parameters:", font=("Ariel", 15, "italic"))

frame1 = LabelFrame(window, text='Test Procedure', font=("Rockwell", 10, "bold"))
frame1.place(x=140, y=325)

frame2 = LabelFrame(window, text='Run Type', font=("Rockwell", 10, "bold"))
frame2.place(x=265, y=325)

confirm_button = Button(text="Confirm", width=20, command=message)
confirm_button.place(x=170, y=400)

group_1 = IntVar()
group_2 = IntVar()
Radiobutton(frame1, text='WLTP', variable=group_1, value=1).pack()
Radiobutton(frame1, text='NEDC', variable=group_1, value=2).pack()
Radiobutton(frame2, text='Split Runs', variable=group_2, value=1).pack()
Radiobutton(frame2, text='Single Runs', variable=group_2, value=2).pack()

window.mainloop()
