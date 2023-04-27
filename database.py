import sqlite3 as sql
from datetime import datetime

con = sql.connect('simple-db')


def save_to_database(student_id, percent, answers, test_id):
    date_and_time = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    data = (student_id, percent, answers, test_id, date_and_time)
    sq = '''INSERT INTO STUDENTS_RESULT (STUDENT_ID, PERCENT, ANSWERS, TEST_ID, DATE_TIME) VALUES (?, ?, ?, ?, ?)'''

    with con:
        con.execute(sq, data)
    # print("Zapis do bazy!")


def get_correct_answers(test_id):
    with con:
        corr_ans = con.execute(f"SELECT ANSWERS FROM CORRECT_ANSWERS WHERE TEST_ID = {test_id}")
        corr_ans = list(corr_ans)
    # print("Odczyt z bazy!")
    return corr_ans[0][0]
