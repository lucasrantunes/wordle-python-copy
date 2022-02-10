import tkinter as tk

bg_color = "#6E5C62"
disabled_bg_color = "#615458"
button_color = "#4C4347"

class View(tk.Tk):
    def __init__(self, key_event_letter, key_event_backspace, key_event_enter):
        super().__init__()
        self.title("Wordle")
        self.label_box_frame = tk.Frame(self, padx=20, pady=20, bg=bg_color)
        label_row = 0
        self.label_box = [[] for i in range(6)]

        while label_row < 6:
            label_column = 0
            while label_column < 5:
                label_status = True if label_row == 0 else False

                label_frame = tk.Frame(self.label_box_frame, padx=2, pady=2, bg=bg_color)
                self.label_box[label_row].append(self.create_label(label_frame, label_status))
                self.label_box[label_row][label_column].pack()

                label_frame.grid(row=label_row, column=label_column)
                label_column += 1

            label_row += 1

        self.label_box_frame.grid(row = 0)

        self.keyboard_frame = tk.Frame(self, background=bg_color, padx=20, pady=20)

        self.Q_key = tk.Button(self.keyboard_frame, text="Q", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("Q"))
        self.Q_key.grid(row=0, column=0)
        self.W_key = tk.Button(self.keyboard_frame, text="W", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("W"))
        self.W_key.grid(row=0, column=1)
        self.E_key = tk.Button(self.keyboard_frame, text="E", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("E"))
        self.E_key.grid(row=0, column=2)
        self.R_key = tk.Button(self.keyboard_frame, text="R", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("R"))
        self.R_key.grid(row=0, column=3)
        self.T_key = tk.Button(self.keyboard_frame, text="T", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("T"))
        self.T_key.grid(row=0, column=4)
        self.Y_key = tk.Button(self.keyboard_frame, text="Y", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("Y"))
        self.Y_key.grid(row=0, column=5)
        self.U_key = tk.Button(self.keyboard_frame, text="U", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("U"))
        self.U_key.grid(row=0, column=6)
        self.I_key = tk.Button(self.keyboard_frame, text="I", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("I"))
        self.I_key.grid(row=0, column=7)
        self.O_key = tk.Button(self.keyboard_frame, text="O", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("O"))
        self.O_key.grid(row=0, column=8)
        self.P_key = tk.Button(self.keyboard_frame, text="P", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("P"))
        self.P_key.grid(row=0, column=9)

        self.A_key = tk.Button(self.keyboard_frame, text="A", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("A"))
        self.A_key.grid(row=1, column=0)
        self.S_key = tk.Button(self.keyboard_frame, text="S", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("S"))
        self.S_key.grid(row=1, column=1)
        self.D_key = tk.Button(self.keyboard_frame, text="D", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("D"))
        self.D_key.grid(row=1, column=2)
        self.F_key = tk.Button(self.keyboard_frame, text="F", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("F"))
        self.F_key.grid(row=1, column=3)
        self.G_key = tk.Button(self.keyboard_frame, text="G", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("G"))
        self.G_key.grid(row=1, column=4)
        self.H_key = tk.Button(self.keyboard_frame, text="H", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("H"))
        self.H_key.grid(row=1, column=5)
        self.J_key = tk.Button(self.keyboard_frame, text="J", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("J"))
        self.J_key.grid(row=1, column=6)
        self.K_key = tk.Button(self.keyboard_frame, text="K", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("K"))
        self.K_key.grid(row=1, column=7)
        self.L_key = tk.Button(self.keyboard_frame, text="L", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("L"))
        self.L_key.grid(row=1, column=8)

        self.backspace_img = tk.PhotoImage(file="img/backspace_button.png")
        self.backspace_key = tk.Button(self.keyboard_frame, image=self.backspace_img, background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, command=key_event_backspace)
        self.backspace_key.grid(row=1, column=9)

        self.Z_key = tk.Button(self.keyboard_frame, text="Z", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("Z"))
        self.Z_key.grid(row=2, column=0)
        self.X_key = tk.Button(self.keyboard_frame, text="X", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("X"))
        self.X_key.grid(row=2, column=1)
        self.C_key = tk.Button(self.keyboard_frame, text="C", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("C"))
        self.C_key.grid(row=2, column=2)
        self.V_key = tk.Button(self.keyboard_frame, text="V", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("V"))
        self.V_key.grid(row=2, column=3)
        self.B_key = tk.Button(self.keyboard_frame, text="B", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("B"))
        self.B_key.grid(row=2, column=4)
        self.N_key = tk.Button(self.keyboard_frame, text="N", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("N"))
        self.N_key.grid(row=2, column=5)
        self.M_key = tk.Button(self.keyboard_frame, text="M", background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, width=1, command=lambda: key_event_letter("M"))
        self.M_key.grid(row=2, column=6)

        self.enter_img = tk.PhotoImage(file="img/enter_button.png")
        self.enter_key = tk.Button(self.keyboard_frame, image=self.enter_img, background=button_color, activebackground=button_color, font=("Arial", 24, "bold"), foreground="white", activeforeground="white", borderwidth=0, highlightbackground=bg_color, command=key_event_enter)
        self.enter_key.grid(row=2, column=7)

        self.keyboard_frame.grid(row=1)
        self.configure(bg=bg_color)

        self.resizable(False, False)


    def create_label(self, label_frame, label_status):
        if label_status == False:
            return tk.Label(label_frame, text=" ", width=2, 
                    background=disabled_bg_color, foreground="white",
                    borderwidth=2, font=("Arial", 30, "bold"), relief="solid")
        else:
            return tk.Label(label_frame, text=" ", width=2, 
                    background=bg_color, foreground="white",
                    borderwidth=2, font=("Arial", 30, "bold"), relief="solid")

    def get_label_text(self, label_row, label_column):
        return self.label_box[label_row][label_column].cget("text")

    def update_label_box(self, label_row, label_column, letter):
        self.label_box[label_row][label_column]['text'] = letter
    
    def active_label_row(self, label_row):
        for column in range(0, 5):
            self.label_box[label_row][column]['background'] = bg_color
            print(column)
            print(label_row)

# def key_event(key):
#     print(f"Internal key event: {key}")

# if __name__ == "__main__":
#     view = View(key_event)
#     view.mainloop()