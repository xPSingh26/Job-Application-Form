import sqlite3


def get_data():
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    res = cursor.execute("SELECT email FROM job_application_formdatabase")
    emails = res.fetchall()
    connection.close()
    emailList = []
    for email in emails:
        emailList.append(email[0])

    return emailList


if __name__ == '__main__':
    emailList = get_data()
    print(emailList)
