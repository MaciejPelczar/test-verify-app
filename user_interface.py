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
        self.error_text = tk.StringVar()
        self.error_text1 = tk.StringVar()

        self.button_load = ttk.Button(self, text="LOAD IMAGE", command=self.load_file)
        self.button_check = ttk.Button(self, text="CHECK IMAGE", command=self.check_image)
        self.button_edit = ttk.Button(self, text="EDIT", state='disable', command=self.edit_results)
        self.button_save = ttk.Button(self, text="SAVE GRADE", command=self.save_grade)
        self.button_close = ttk.Button(self, text="CLOSE", command=self.quit)
        self.button_ok = ttk.Button(self, text="OK", state='disable', command=self.commit_edit_changes)

        self.button_load.grid(column=0, row=0, columnspan=2)
        self.button_check.grid(column=2, row=0)
        self.button_edit.grid(column=5, row=0)
        self.button_save.grid(column=3, row=0)
        self.button_close.grid(column=4, row=0)
        self.button_ok.grid(column=5, row=2)

        ttk.Separator(
            master=self,
            orient="horizontal",
            style='blue.TSeparator',
            takefocus=1,
            cursor='plus'
        ).grid(row=1, column=0, ipadx=300, pady=10, columnspan=6)

        label_percent = ttk.Label(self, text="Percentage grade")
        label_percent.grid(column=0, row=3, columnspan=2)
        label_percent_display = ttk.Label(self, textvariable=self.percentage)
        label_percent_display.grid(column=0, row=4, columnspan=2)

        label_student_id = ttk.Label(self, text="Student ID")
        label_student_id.grid(column=0, row=5, columnspan=2)
        self.label_student_id_display = ttk.Entry(self, state='disable', width=8, textvariable=self.student_id)
        self.label_student_id_display.grid(column=0, row=6, columnspan=2)

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

        self.label_1 = ttk.Entry(self, width=6, state='disable', textvariable=self.l0)
        self.label_1.grid(column=0, row=11)
        entry_1 = ttk.Label(self, textvariable=self.e0)
        entry_1.grid(column=1, row=11)

        self.label_2 = ttk.Entry(self, width=6, state='disable', textvariable=self.l1)
        self.label_2.grid(column=0, row=12)
        entry_2 = ttk.Label(self, textvariable=self.e1)
        entry_2.grid(column=1, row=12)

        self.label_3 = ttk.Entry(self, width=6, state='disable', textvariable=self.l2)
        self.label_3.grid(column=0, row=13)
        entry_3 = ttk.Label(self, textvariable=self.e2)
        entry_3.grid(column=1, row=13)

        self.label_4 = ttk.Entry(self, width=6, state='disable', textvariable=self.l3)
        self.label_4.grid(column=0, row=14)
        entry_4 = ttk.Label(self, textvariable=self.e3)
        entry_4.grid(column=1, row=14)

        self.label_5 = ttk.Entry(self, width=6, state='disable', textvariable=self.l4)
        self.label_5.grid(column=0, row=15)
        entry_5 = ttk.Label(self, textvariable=self.e4)
        entry_5.grid(column=1, row=15)

        self.label_6 = ttk.Entry(self, width=6, state='disable', textvariable=self.l5)
        self.label_6.grid(column=0, row=16)
        entry_6 = ttk.Label(self, textvariable=self.e5)
        entry_6.grid(column=1, row=16)

        self.label_7 = ttk.Entry(self, width=6, state='disable', textvariable=self.l6)
        self.label_7.grid(column=0, row=17)
        entry_7 = ttk.Label(self, textvariable=self.e6)
        entry_7.grid(column=1, row=17)

        self.label_8 = ttk.Entry(self, width=6, state='disable', textvariable=self.l7)
        self.label_8.grid(column=0, row=18)
        entry_8 = ttk.Label(self, textvariable=self.e7)
        entry_8.grid(column=1, row=18)

        self.label_9 = ttk.Entry(self, width=6, state='disable', textvariable=self.l8)
        self.label_9.grid(column=0, row=19)
        entry_9 = ttk.Label(self, textvariable=self.e8)
        entry_9.grid(column=1, row=19)

        self.label_10 = ttk.Entry(self, width=6, state='disable', textvariable=self.l9)
        self.label_10.grid(column=0, row=20)
        entry_10 = ttk.Label(self, textvariable=self.e9)
        entry_10.grid(column=1, row=20)

        self.label_11 = ttk.Entry(self, width=6, state='disable', textvariable=self.l10)
        self.label_11.grid(column=0, row=21)
        entry_11 = ttk.Label(self, textvariable=self.e10)
        entry_11.grid(column=1, row=21)

        self.label_12 = ttk.Entry(self, width=6, state='disable', textvariable=self.l11)
        self.label_12.grid(column=0, row=22)
        entry_12 = ttk.Label(self, textvariable=self.e11)
        entry_12.grid(column=1, row=22)

        self.error_label = ttk.Label(self, width=22, textvariable=self.error_text)
        self.error_label.grid(column=5, row=3, rowspan=2)
        self.error_label = ttk.Label(self, width=22, textvariable=self.error_text1)
        self.error_label.grid(column=5, row=5, rowspan=2)

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
        self.button_edit.configure(state="disable")

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
        self.button_edit.configure(state="normal")

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
        labels_usr = [self.l0, self.l1, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7, self.l8, self.l9,
                      self.l10, self.l11]
        for i in range(12):
            answers.append(labels_usr[i].get())
        answers = " ".join(answers)
        database.save_to_database(self.student_id.get(), self.percentage.get(), answers, self.test_id_indexes.get())
        self.button_edit.configure(state="disable")

    def edit_results(self):
        self.button_ok.configure(state="normal")
        labels = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                  self.label_8, self.label_9, self.label_10, self.label_11, self.label_12,
                  self.label_student_id_display]
        for i in labels:
            i.configure(state="normal")

        buttons = [self.button_load, self.button_check, self.button_edit, self.button_save, self.button_close]
        for i in buttons:
            i.configure(state="disable")

    def commit_edit_changes(self):

        id_checked_output = self.check_if_enter_correct_student_id()

        correct_inputs, percentage = self.check_if_enter_correct_user_answer()
        if correct_inputs & (id_checked_output == "Success!"):

            self.button_ok.configure(state="disable")
            labels = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7,
                      self.label_8, self.label_9, self.label_10, self.label_11, self.label_12,
                      self.label_student_id_display]
            for i in labels:
                i.configure(state="disable")

            buttons = [self.button_load, self.button_check, self.button_edit, self.button_save, self.button_close]
            for i in buttons:
                i.configure(state="normal")

            self.percentage.set(percentage)

            self.error_text.set("Success!\nEdit User Answers")
            self.error_text1.set("Success!\nEdit StudentID")

        else:
            if not correct_inputs:
                self.error_text.set("Error!\nEnter A, B, C, or D")
            else:
                self.error_text.set("Success!\nEdit User Answers")
            if id_checked_output != "Success!":
                self.error_text1.set(id_checked_output)
            else:
                self.error_text1.set("Success!\nEdit StudentID")

    def check_if_enter_correct_user_answer(self):
        sum_cor = 0
        user = [self.l0, self.l1, self.l2, self.l3, self.l4, self.l5,
                self.l6, self.l7, self.l8, self.l9, self.l10, self.l11]
        key = [self.e0, self.e1, self.e2, self.e3, self.e4, self.e5,
               self.e6, self.e7, self.e8, self.e9, self.e10, self.e11]

        correct_inputs = 0
        for i in range(12):
            user[i].set(user[i].get().capitalize())

            if user[i].get() in "ABCD":
                correct_inputs += 1
        if correct_inputs == 12:
            for i in range(12):
                if user[i].get() == key[i].get():
                    sum_cor += 1
            percentage = str(round(sum_cor / 12 * 100, 2))
            return 1, percentage
        else:
            return 0, self.percentage.get()

    def check_if_enter_correct_student_id(self):
        try:
            student = int(self.student_id.get())
        except:
            return "Error!\nStudentID not a number!"

        if len(str(student)) < 5:
            return "Error!\nStudent ID too short!"
        elif len(str(student)) > 5:
            return "Error!\nStudentID too long!"
        else:
            return "Success!"


def check(image_path):
    image = check_image.CheckImage(image_path)
    image.check_image()

    return image.percentage, image.student_indexes, image.answer_indexes, image.test_id_indexes_int, image.img


def show_last_results():
    win = root
    new = tk.Toplevel(win)
    new.geometry("520x600")
    new.title("Results")
    frame = ttk.Frame(new)
    frame.pack()

    # scrollbar
    scrollX = ttk.Scrollbar(frame, orient='horizontal')
    scrollX.pack(side=tk.BOTTOM, fill=tk.X)

    scrollY = ttk.Scrollbar(frame, orient='vertical')
    scrollY.pack(side=tk.RIGHT, fill=tk.Y)

    results = ttk.Treeview(frame, yscrollcommand=scrollY.set, xscrollcommand=scrollX.set, height=550)

    results.pack()

    scrollY.config(command=results.yview)
    scrollX.config(command=results.xview)

    # define our column

    results['columns'] = ('student_id', 'percent', 'answers', 'test_id', 'date_time')

    # format our column
    results.column("#0", width=0, stretch=tk.NO)
    results.column("student_id", anchor=tk.CENTER, width=70)
    results.column("percent", anchor=tk.CENTER, width=50)
    results.column("answers", anchor=tk.CENTER, width=160)
    results.column("test_id", anchor=tk.CENTER, width=50)
    results.column("date_time", anchor=tk.CENTER, width=120)

    # Create Headings
    results.heading("#0", text="", anchor=tk.CENTER)
    results.heading("student_id", text="Student Id", anchor=tk.CENTER)
    results.heading("percent", text="Score %", anchor=tk.CENTER)
    results.heading("answers", text="Answers", anchor=tk.CENTER)
    results.heading("test_id", text="Test Id", anchor=tk.CENTER)
    results.heading("date_time", text="Date & Time", anchor=tk.CENTER)

    all_info = (database.get_all())

    for i in reversed(list(all_info)):
        results.insert(parent="", index='end', iid=i, text='', values=(i[1], i[2], i[3], i[4], i[5]))

    win.mainloop()
    win.quit()


def show_credentials():
    win = root
    new = tk.Toplevel(win)
    new.geometry("550x120")
    new.title("About application")
    frame = ttk.Frame(new)
    frame.pack()

    label = ttk.Label(new, text="Answer card checker app.", font=("Segoe UI", 12))
    label_text = ttk.Label(new, text="The application allows you to load a photo of the answer card, "
                                     "using the openCV library, \nthe fields Answers, Student ID and Test ID are read. "
                                     "Answers are verified on the basis of \na key in the database with the "
                                     "appropriate Test ID. The application also allows you to \nsave the obtained "
                                     "results to the database. The GUI was created using the tkinter library.")
    label.pack()
    label_text.pack()
    win.mainloop()
    win.quit()


root = MainWindow()

root.columnconfigure(0, weight=1)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Check results", command=show_last_results)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=show_credentials)

menubar.add_cascade(label="Menu", menu=filemenu)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.mainloop()

