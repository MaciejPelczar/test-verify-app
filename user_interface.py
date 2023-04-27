import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from cv2 import cv2

import check_image
import database
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

        self.answer_indexes = []
        self.user_answers = []
        self.correct_answers = []
        self.test_id_indexes = tk.StringVar()
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

        self.l0 = tk.StringVar()
        self.l1 = tk.StringVar()
        self.l2 = tk.StringVar()
        self.l3 = tk.StringVar()
        self.l4 = tk.StringVar()
        self.l5 = tk.StringVar()
        self.l6 = tk.StringVar()
        self.l7 = tk.StringVar()
        self.l8 = tk.StringVar()
        self.l9 = tk.StringVar()
        self.l10 = tk.StringVar()
        self.l11 = tk.StringVar()

        self.student_id = tk.StringVar()
        self.test_id = tk.StringVar()
        self.percentage = tk.StringVar()
        self.filename = tk.StringVar(value="pyton.png")

        button_load = ttk.Button(self, text="LOAD IMAGE", command=self.load_file)
        button_check = ttk.Button(self, text="CHECK IMAGE", command=self.check_image)
        button_save = ttk.Button(self, text="SAVE GRADE", command=self.save_grade)
        button_close = ttk.Button(self, text="CLOSE", command=self.quit)

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

        button_load = ttk.Label(self, text="Test ID: ")
        button_load.grid(column=0, row=8, sticky="E")

        answers_id = ttk.Label(self, textvariable=self.test_id_indexes)
        answers_id.grid(column=1, row=8, sticky="W")

        ttk.Separator(
            master=self,
            orient="horizontal",
            style='blue.TSeparator',
            takefocus=1,
            cursor='plus'
        ).grid(row=9, column=0, ipadx=50, pady=10, columnspan=2)

        label_key = ttk.Label(self, text="KEY")
        label_key.grid(column=1, row=10)
        label_user = ttk.Label(self, text="USER")
        label_user.grid(column=0, row=10)

        label_1 = ttk.Label(self, textvariable=self.l0)
        label_1.grid(column=0, row=11)
        entry_1 = ttk.Label(self, textvariable=self.e0)
        entry_1.grid(column=1, row=11)

        label_2 = ttk.Label(self, textvariable=self.l1)
        label_2.grid(column=0, row=12)
        entry_2 = ttk.Label(self, textvariable=self.e1)
        entry_2.grid(column=1, row=12)

        label_3 = ttk.Label(self, textvariable=self.l2)
        label_3.grid(column=0, row=13)
        entry_3 = ttk.Label(self, textvariable=self.e2)
        entry_3.grid(column=1, row=13)

        label_4 = ttk.Label(self, textvariable=self.l3)
        label_4.grid(column=0, row=14)
        entry_4 = ttk.Label(self, textvariable=self.e3)
        entry_4.grid(column=1, row=14)

        label_5 = ttk.Label(self, textvariable=self.l4)
        label_5.grid(column=0, row=15)
        entry_5 = ttk.Label(self, textvariable=self.e4)
        entry_5.grid(column=1, row=15)

        label_6 = ttk.Label(self, textvariable=self.l5)
        label_6.grid(column=0, row=16)
        entry_6 = ttk.Label(self, textvariable=self.e5)
        entry_6.grid(column=1, row=16)

        label_7 = ttk.Label(self, textvariable=self.l6)
        label_7.grid(column=0, row=17)
        entry_7 = ttk.Label(self, textvariable=self.e6)
        entry_7.grid(column=1, row=17)

        label_8 = ttk.Label(self, textvariable=self.l7)
        label_8.grid(column=0, row=18)
        entry_8 = ttk.Label(self, textvariable=self.e7)
        entry_8.grid(column=1, row=18)

        label_9 = ttk.Label(self, textvariable=self.l8)
        label_9.grid(column=0, row=19)
        entry_9 = ttk.Label(self, textvariable=self.e8)
        entry_9.grid(column=1, row=19)

        label_10 = ttk.Label(self,  textvariable=self.l9)
        label_10.grid(column=0, row=20)
        entry_10 = ttk.Label(self, textvariable=self.e9)
        entry_10.grid(column=1, row=20)

        label_11 = ttk.Label(self,  textvariable=self.l10)
        label_11.grid(column=0, row=21)
        entry_11 = ttk.Label(self, textvariable=self.e10)
        entry_11.grid(column=1, row=21)

        label_12 = ttk.Label(self,  textvariable=self.l11)
        label_12.grid(column=0, row=22)
        entry_12 = ttk.Label(self, textvariable=self.e11)
        entry_12.grid(column=1, row=22)

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
        percentage, student_id, self.answer_indexes, test_id_indexes, img = check(self.filename.get())
        self.test_id_indexes.set(test_id_indexes)
        # print(self.test_id_indexes)
        self.load_correct_answers()

        self.percentage.set(round(percentage, 2))
        student_id_str = ""
        for i in range(5):
            student_id_str += str(student_id[i])

        self.student_id.set(student_id_str)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        photo = ImageTk.PhotoImage(img)
        image_label = ttk.Label(self, image=photo, textvariable=self.filename, padding=5, compound="top")
        image_label.photo = photo
        image_label.grid(column=2, row=2, columnspan=3, rowspan=21)

    def load_correct_answers(self):

        corr_ans = database.get_correct_answers(self.test_id_indexes.get())
        corr_ans = corr_ans.split(" ")

        dict_answer = {0: "A", 1: "B", 2: "C", 3: "D"}
        dict_reverse = {"A": 0, "B": 1, "C": 2, "D": 3}

        labels_cor = [self.e0, self.e1, self.e2, self.e3, self.e4, self.e5, self.e6, self.e7, self.e8, self.e9,
                      self.e10, self.e11]
        for i in range(12):
            self.correct_answers.append(dict_reverse[corr_ans[i]])
            labels_cor[i].set(corr_ans[i])

        labels_usr = [self.l0, self.l1, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7, self.l8, self.l9,
                      self.l10, self.l11]
        for i in range(12):
            self.user_answers.append(dict_answer[self.answer_indexes[i]])
            labels_usr[i].set(self.user_answers[i])

    def save_grade(self):
        answers = []
        ans = tuple(self.answer_indexes)
        dict_reverse = {0: "A", 1: "B", 2: "C", 3: "D"}
        for i in range(12):
            answers.append(dict_reverse[ans[i]])
        answers = " ".join(answers)

        database.save_to_database(self.student_id.get(), self.percentage.get(), answers, self.test_id_indexes.get())


def check(image_path):

    image = check_image.CheckImage(image_path)
    image.check_image()

    return image.percentage, image.student_indexes, image.answer_indexes, image.test_id_indexes_int, image.img


def start_user_interface():
    root = MainWindow()

    root.columnconfigure(0, weight=1)

    root.mainloop()
