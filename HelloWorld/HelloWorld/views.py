from django.shortcuts import render
import MySQLdb
from django.conf import settings
from django.shortcuts import render
import pymysql
from django.conf import settings


# from .models import Class, ClassTime


def index(request):
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='37070378',
        db='django',
        port=3306
    )
    cursor = conn.cursor()
    cursor.execute("SELECT Take.Student_ID, Class.Class_Name, Class_time.Week_Day, Class_time.Start_TIme, "
                   "Class_time.End_Time FROM Take JOIN Class ON Take.Class_ID = Class.Class_ID JOIN Class_time ON "
                   "Take.Class_ID = Class_time.Class_ID WHERE Student_ID = 'D2023003';")
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'index.html', {'results': results})


def result(request):
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='37070378',
        db='django',
        port=3306
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")

    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return render(request, 'index.html', {'results': results})



