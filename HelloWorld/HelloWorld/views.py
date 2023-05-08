from django.shortcuts import render
import MySQLdb
from django.conf import settings
from django.shortcuts import render
import pymysql
from django.conf import settings


# from .models import Class, ClassTime


def reg(request):
    if request.method == 'POST':
        student_id = request.POST.get('studentID')
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
                       "Take.Class_ID = Class_time.Class_ID WHERE Student_ID = %s;", student_id)
        results = cursor.fetchall()


        cursor.close()
        conn.close()

        schedule = [[None] * 15 for _ in range(5)]
        weekdays = ['一', '二', '三', '四', '五']

        for i in results:
            student_id, class_name, week_day, start_time, end_time = i
            week_day = int(week_day)  # 将星期转换成从0开始的索引
            start_time = int(start_time)  # 将节次转换成从0开始的索引
            end_time = int(end_time)
            schedule[week_day][start_time:end_time + 1] = [class_name] * (end_time - start_time + 1)

        context = {'schedule': schedule, 'weekdays': weekdays}
        return render(request, 'index.html', context)
    else:
        schedule = None
        weekdays = ['一', '二', '三', '四', '五']
        context = {'schedule': schedule, 'weekdays': weekdays}
        return render(request, 'index.html', context)


def quary(request):

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


def index(request):
    if request.method == 'POST':
        studentID = request.POST.get('studentID')
    return render(request, 'index.html')
