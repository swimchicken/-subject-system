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
            week_day = int(week_day)  # 將星期轉換成從0開始的索引
            start_time = int(start_time)  # 將節次轉換成從0開始的索引
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
        Class_Department = request.POST.get('Class_Department')
        Class_Grade = request.POST.get('Class_Grade')
        conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='37070378',
            db='django',
            port=3306
        )

        cursor = conn.cursor()
        cursor.execute("SELECT Class.Class_ID, Class.Class_Name, Class.Credit, Class.Required_Elective, Class.Class_Department, Class.Class_Grade, Class.Teacher, Class.Student_Maximum, Class_time.Week_Day, Class_time.Start_Time, Class_time.End_Time FROM Class JOIN Class_Time ON Class.Class_ID = Class_Time.Class_ID WHERE Class_Department = %s AND Class_Grade = %s;",Class_Department ,Class_Grade)
        results_ClassData = cursor.fetchall()

        cursor.execute("SELECT count(Take_ID) FROM Take WHERE Class_ID = %d;",Class_ID)
        results_SeletedNumber = cursor.fetchall()

        cursor.close()
        conn.close()

        Week_Day = ['一', '二', '三', '四', '五']

        for i in results_ClassData:
            Class_ID, Class_Name, Credit, Required_Elective,Class_Department,Class_Grade,Teacher,Student_Maximum,Week_Day,Start_Time,End_Time, End_Time = i

            Week_Day = int(Week_Day)  # 將星期轉換成從0開始的索引
            Start_Time = int(Start_Time)  # 將節次轉換成從0開始的索引
            End_Time = int(End_Time)
        
        for i in results_SeletedNumber:
            Seleted_Number = i


        context = {
            'Class_ID': Class_ID, 
            'Class_Name': Class_Name, 
            'Credit': Credit, 
            'Required_Elective': Required_Elective,
            'Class_Department': Class_Department,
            'Class_Grade': Class_Grade,
            'Teacher': Teacher,
            'Seleted/Maximum_Number': Seleted_Number+'/'+Student_Maximum
            }
        return render(request, 'index.html', context)
    return render(request, 'index.html')
