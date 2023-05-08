from django.shortcuts import render

import MySQLdb
from django.conf import settings
from django.shortcuts import render

import pymysql
from django.conf import settings


def index(request):
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

def reg(request):
    if request.method == 'POST':
        studentID=request.POST.get('studentID')
    print(studentID)
    return render(request, 'index.html')
