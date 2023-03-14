from tkinter import *

file_name = "reference_values"


def hole_diameter():
    if not entry_01.get() == '':
        try:
            diameter = float(entry_01.get())
        except:
            diameter = 1
    else:
        diameter = 1
    return diameter


def hole_perimeter():
    perimeter = hole_diameter() * 3.141593
    return perimeter


def shear_stress():
    if not entry_02.get() == '':
        try:
            ss = float(entry_02.get())
        except:
            ss = 0
    else:
        ss = 0
    return ss


def plate_thickness():
    if not entry_03.get() == '':
        try:
            pt = float(entry_03.get())
        except:
            pt = 0
    else:
        pt = 0
    return pt


# FOLGA
def die_clearance():
    ss = shear_stress()
    pt = plate_thickness()
    if ss < 16:
        factor = 0.15
    elif ss < 33:
        factor = 0.2
    elif ss < 57:
        factor = 0.25
    clearance = factor * pt
    return clearance


# FORÇA DE CORTE
def cutting_force():
    if not entry_01.get() == '':
        return shear_stress() * hole_perimeter() * plate_thickness()
    else:
        return 0


def punch_base():
    hd = hole_diameter()
    if hd <= 28:
        pb = 30
    elif hd <= 38:
        pb = 40
    elif hd <= 48:
        pb = 50
    elif hd <= 61:
        pb = 63
    elif hd <= 73:
        pb = 76
    return pb


def die_base():
    hd = hole_diameter()
    if hd <= 22:
        db = 60
    else:
        db = 100
    return db


def apply():
    with open(f'{file_name}.txt', 'w') as file:
        file.writelines(f'"hole_diameter" = {hole_diameter()}\n')
        file.writelines(f'"die_clearance" = {die_clearance()}\n')
        file.writelines(f'"punch_base" = {punch_base()}\n')
        file.writelines(f'"die_base" = {die_base()}\n')
    label_04b['text'] = f'{cutting_force():.2f} kgf'


root = Tk()

root.geometry('280x240')
root.resizable(width=False, height=False)
root.title('MERINO - TRUMPF MODE')
root.config(bg='#F2B33D')

label_X0 = Label(root, background='#F2B33D', text=f'By Merino', foreground='#B8860B')
label_X0.grid(column=2, row=0, padx=5, pady=5)

label_01 = Label(root, text="Hole Diameter:", background='#F2B33D')
label_01.grid(column=1, row=1, padx=5, pady=5)
entry_01 = Entry(root, width=25, foreground='#008080')
entry_01.grid(column=2, row=1, padx=0, pady=5)

label_02 = Label(root, text="Shear Stress:", background='#F2B33D')
label_02.grid(column=1, row=2, padx=5, pady=5)
entry_02 = Entry(root, width=25, foreground='#008080')
entry_02.grid(column=2, row=2, padx=0, pady=5)

label_03 = Label(root, text="Plate Thickness:", background='#F2B33D')
label_03.grid(column=1, row=3, padx=5, pady=5)
entry_03 = Entry(root, width=25, foreground='#008080')
entry_03.grid(column=2, row=3, padx=0, pady=5)

label_04 = Label(root, text="Cutting Force:", background='#F2B33D')
label_04.grid(column=1, row=4, padx=5, pady=5)
label_04b = Label(root, width=22, text=f'{cutting_force():.2f} kgf', background='#B8860B')
label_04b.grid(column=2, row=4, padx=5, pady=5)

button_10 = Button(root, text="Aplicar", command=apply, width=12, background="#008080", foreground='#F2B33D', font='ComicSans 10 bold')
button_10.grid(column=2, row=10, padx=20, pady=22)

root.mainloop()