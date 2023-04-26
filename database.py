import sqlite3 as sql
from datetime import datetime


con = sql.connect('simple-db')


def save_to_database(student_id, percent, answers, test_id):
    date_and_time = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    # answers = '-'.join(answers)
    # corr_ans = corr_ans.split(" ")
    #
    # date_and_time = date_and_time.split(" ")

    # student = student_id.split(" ")
    # student = "".join(student)
    # {student_id}, {percent}, {answers}, {test_id}, {date_and_time}
    data = (student_id, percent, answers, test_id, date_and_time)
    sq = '''INSERT INTO STUDENTS_RESULT (STUDENT_ID, PERCENT, ANSWERS, TEST_ID, DATE_TIME) VALUES (?, ?, ?, ?, ?)'''

    print(data[0], data[1], data[2], data[3], data[4])
    with con:
        con.execute(sq, data)
    print("Zapis do bazy!")


def get_correct_answers(test_id):
    with con:
        corr_ans = con.execute(f"SELECT ANSWERS FROM CORRECT_ANSWERS WHERE TEST_ID = {test_id}")
        corr_ans = list(corr_ans)
    print("Odczyt z bazy!")
    return corr_ans[0][0]
