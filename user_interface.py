import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from cv2 import cv2

import main


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Test answer verify")

        main_frame = MainFrame(self)
        main_frame.grid(pady=10, padx=10)


class MainFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.e0 = tk.StringVar()
        self.e1 = tk.StringVar()
        self.e2 = tk.StringVar()
        self.e3 = tk.StringVar()
        self.e4 = tk.StringVar()
        self.e5 = tk.StringVar()
        self.e6 = tk.StringVar()
        self.e7 = tk.StringVar()
        self.e8 = tk.StringVar()
        self.e9 = tk.StringVar()
        self.e10 = tk.StringVar()
        self.e11 = tk.StringVar()

        self.student_id = tk.StringVar()
        self.percentage = tk.StringVar()
        self.filename = tk.StringVar(value="Python-Symbol.png")

        button_load = ttk.Button(self, text="LOAD IMAGE", command=self.load_file)
        button_check = ttk.Button(self, text="CHECK IMAGE", command=self.check_image)
        button_save = ttk.Button(self, text="SAVE GRADE")
        button_close = ttk.Button(self, text="CLOSE")

        button_load.grid(column=0, row=0, columnspan=2)
        button_check.grid(column=2, row=0)
        button_save.grid(column=3, row=0)
        button_close.grid(column=4, row=0)

        ttk.Separator(
            master=self,
            orient="horizontal",
            style='blue.TSeparator',
            takefocus=1,
            cursor='plus'
        ).grid(row=1, column=0, ipadx=250, pady=10, columnspan=5)

        label_percent = ttk.Label(self, text="Percentage grade")
        label_percent.grid(column=0, row=3, columnspan=2)
        label_percent_display = ttk.Label(self, textvariable=self.percentage)
        label_percent_display.grid(column=0, row=4, columnspan=2)

        label_student_id = ttk.Label(self, text="Student ID")
        label_student_id.grid(column=0, row=5, columnspan=2)
        label_student_id_display = ttk.Label(self, textvariable=self.student_id)
        label_student_id_display.grid(column=0, row=6, columnspan=2)

        ttk.Separator(
            master=self,
            orient="horizontal",
            style='blue.TSeparator',
            takefocus=1,
            cursor='plus'
        ).grid(row=7, column=0, ipadx=50, pady=10, columnspan=2)

        button_load = ttk.Button(self, text="LOAD ANSWERS", command=self.load_correct_answers)
        button_load.grid(column=0, row=8, columnspan=2)

        answers_id = ttk.Entry(self, width=10)
        answers_id.grid(column=0, row=9, columnspan=2)

        ttk.Separator(
            master=self,
            orient="horizontal",
            style='blue.TSeparator',
            takefocus=1,
            cursor='plus'
        ).grid(row=10, column=0, ipadx=50, pady=10, columnspan=2)

        label_1 = ttk.Label(self, text="1", width=2)
        label_1.grid(column=0, row=11, sticky="E")
        entry_1 = ttk.Label(self, width=7, textvariable=self.e0)
        entry_1.grid(column=1, row=11, sticky="W")

        label_2 = ttk.Label(self, text="2", width=2)
        label_2.grid(column=0, row=12, sticky="E")
        entry_2 = ttk.Label(self, width=7, textvariable=self.e1)
        entry_2.grid(column=1, row=12, sticky="W")

        label_3 = ttk.Label(self, text="3", width=2)
        label_3.grid(column=0, row=13, sticky="E")
        entry_3 = ttk.Label(self, width=7, textvariable=self.e2)
        entry_3.grid(column=1, row=13, sticky="W")

        label_4 = ttk.Label(self, text="4", width=2)
        label_4.grid(column=0, row=14, sticky="E")
        entry_4 = ttk.Label(self, width=7, textvariable=self.e3)
        entry_4.grid(column=1, row=14, sticky="W")

        label_5 = ttk.Label(self, text="5", width=2)
        label_5.grid(column=0, row=15, sticky="E")
        entry_5 = ttk.Label(self, width=7, textvariable=self.e4)
        entry_5.grid(column=1, row=15, sticky="W")

        label_6 = ttk.Label(self, text="6", width=2)
        label_6.grid(column=0, row=16, sticky="E")
        entry_6 = ttk.Label(self, width=7, textvariable=self.e5)
        entry_6.grid(column=1, row=16, sticky="W")

        label_7 = ttk.Label(self, text="7", width=2)
        label_7.grid(column=0, row=17, sticky="E")
        entry_7 = ttk.Label(self, width=7, textvariable=self.e6)
        entry_7.grid(column=1, row=17, sticky="W")

        label_8 = ttk.Label(self, text="8", width=2)
        label_8.grid(column=0, row=18, sticky="E")
        entry_8 = ttk.Label(self, width=7, textvariable=self.e7)
        entry_8.grid(column=1, row=18, sticky="W")

        label_9 = ttk.Label(self, text="9", width=2)
        label_9.grid(column=0, row=19, sticky="E")
        entry_9 = ttk.Label(self, width=7, textvariable=self.e8)
        entry_9.grid(column=1, row=19, sticky="W")

        label_10 = ttk.Label(self, text="10", width=2)
        label_10.grid(column=0, row=20, sticky="E")
        entry_10 = ttk.Label(self, width=7, textvariable=self.e9)
        entry_10.grid(column=1, row=20, sticky="W")

        label_11 = ttk.Label(self, text="11", width=2)
        label_11.grid(column=0, row=21, sticky="E")
        entry_11 = ttk.Label(self, width=7, textvariable=self.e10)
        entry_11.grid(column=1, row=21, sticky="W")

        label_12 = ttk.Label(self, text="12", width=2)
        label_12.grid(column=0, row=22, sticky="E")
        entry_12 = ttk.Label(self, width=7, textvariable=self.e11)
        entry_12.grid(column=1, row=22, sticky="W")

        file_name_string = self.filename.get()
        image = Image.open(file_name_string).resize((420, 600))
        photo = ImageTk.PhotoImage(image)
        image_label = ttk.Label(self, image=photo, textvariable=self.filename, padding=5, compound="top")
        image_label.photo = photo
        image_label.grid(column=2, row=2, columnspan=3, rowspan=21)

    def load_file(self, *args):

        self.filename.set(fd.askopenfilename())

        file_name_string = self.filename.get()
        image = Image.open(file_name_string).resize((420, 600))
        photo = ImageTk.PhotoImage(image)
        image_label = ttk.Label(self, image=photo, textvariable=self.filename, padding=5, compound="top")
        image_label.photo = photo
        image_label.grid(column=2, row=2, columnspan=3, rowspan=21)

    def check_image(self, *args):
        percentage, student_id, img= main.check(self.filename.get())
        self.percentage.set(round(percentage, 2))
        self.student_id.set(student_id)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        photo = ImageTk.PhotoImage(img)
        image_label = ttk.Label(self, image=photo, textvariable=self.filename, padding=5, compound="top")
        image_label.photo = photo
        image_label.grid(column=2, row=2, columnspan=3, rowspan=21)

    def load_correct_answers(self):
        cor_ans = []
        dic = {0: "A", 1: "B", 2: "C", 3: "D"}
        correct_answers = [1, 2, 0, 0, 3, 2, 3, 1, 3, 0, 3, 1]

        for i in range(12):
            cor_ans.append(dic[correct_answers[i]])

        labels = [self.e0, self.e1, self.e2, self.e3, self.e4, self.e5, self.e6, self.e7, self.e8, self.e9, self.e10,
                  self.e11]

        for i in range(12):
            labels[i].set(cor_ans[i])

    def save_grade(self):
        pass


root = MainWindow()

root.columnconfigure(0, weight=1)

root.mainloop()
