from tkinter import *

bg_color = "#6E5C62"
disabled_bg_color = "#615458"
button_color = "#4C4347"

def create_label(label_frame, label_status):
    if label_status == False:
        return Label(label_frame, text=" ", width=2, 
                background=disabled_bg_color, 
                borderwidth=2, font=("Arial", 30, "bold"), relief="solid")
    else:
        return Label(label_frame, text=" ", width=2, 
                background=bg_color, 
                borderwidth=2, font=("Arial", 30, "bold"), relief="solid")

root = Tk(className="Wordle")

label_box_frame = Frame(root, padx=20, pady=20, bg=bg_color)
label_row = 0
label_box = [[] for i in range(5)]

while label_row < 5:
    label_column = 0
    while label_column < 5:
        label_status = True if label_row == 0 else False

        label_frame = Frame(label_box_frame, padx=2, pady=2, bg=bg_color)
        label_box[label_row].append(create_label(label_frame, label_status))
        label_box[label_row][label_column].pack()

        label_frame.grid(row=label_row, column=label_column)
        label_column += 1

    label_row += 1

label_box_frame.grid(row = 0)

keyboard_frame = Frame(root, background=bg_color, padx=20, pady=20)

Q_key = Button(keyboard_frame, text="Q", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
Q_key.grid(row=0, column=0)
W_key = Button(keyboard_frame, text="W", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
W_key.grid(row=0, column=1)
E_key = Button(keyboard_frame, text="E", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
E_key.grid(row=0, column=2)
R_key = Button(keyboard_frame, text="R", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
R_key.grid(row=0, column=3)
T_key = Button(keyboard_frame, text="T", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
T_key.grid(row=0, column=4)
Y_key = Button(keyboard_frame, text="Y", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
Y_key.grid(row=0, column=5)
U_key = Button(keyboard_frame, text="U", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
U_key.grid(row=0, column=6)
I_key = Button(keyboard_frame, text="I", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
I_key.grid(row=0, column=7)
O_key = Button(keyboard_frame, text="O", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
O_key.grid(row=0, column=8)
P_key = Button(keyboard_frame, text="P", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
P_key.grid(row=0, column=9)

A_key = Button(keyboard_frame, text="A", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
A_key.grid(row=1, column=0)
S_key = Button(keyboard_frame, text="S", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
S_key.grid(row=1, column=1)
D_key = Button(keyboard_frame, text="D", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
D_key.grid(row=1, column=2)
F_key = Button(keyboard_frame, text="F", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
F_key.grid(row=1, column=3)
G_key = Button(keyboard_frame, text="G", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
G_key.grid(row=1, column=4)
H_key = Button(keyboard_frame, text="H", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
H_key.grid(row=1, column=5)
J_key = Button(keyboard_frame, text="J", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
J_key.grid(row=1, column=6)
K_key = Button(keyboard_frame, text="K", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
K_key.grid(row=1, column=7)
L_key = Button(keyboard_frame, text="L", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
L_key.grid(row=1, column=8)

backspace_img = PhotoImage(file="img/backspace_button.png")
backspace_key = Button(keyboard_frame, image=backspace_img, background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color)
backspace_key.grid(row=1, column=9)

Z_key = Button(keyboard_frame, text="Z", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
Z_key.grid(row=2, column=0)
X_key = Button(keyboard_frame, text="X", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
X_key.grid(row=2, column=1)
C_key = Button(keyboard_frame, text="C", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
C_key.grid(row=2, column=2)
V_key = Button(keyboard_frame, text="V", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
V_key.grid(row=2, column=3)
B_key = Button(keyboard_frame, text="B", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
B_key.grid(row=2, column=4)
N_key = Button(keyboard_frame, text="N", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
N_key.grid(row=2, column=5)
M_key = Button(keyboard_frame, text="M", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1)
M_key.grid(row=2, column=6)

enter_img = PhotoImage(file="img/enter_button.png")
enter_key = Button(keyboard_frame, image=enter_img, background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color)
enter_key.grid(row=2, column=7)

keyboard_frame.grid(row=1)

root.configure(bg=bg_color)

root.mainloop()