from django.http import HttpResponse
'''
from TestModel.models import Test


def add(request):
    name = request.Get.get("name")
    age = request.Get.get("age")
    test = Test(name=name, age=age)
    test.save()
    return HttpResponse("<p>數據庫以添加</p>")


def getAll(request):
    list = Test.objests.all()
    response = ""
    for var in list:
        response += var.name + " "
    return HttpResponse("<p>" + response + "</p>")


def update(request):
    id = request.Get.get("id")
    test = Test.objests.get(id=id)
    test.name = "swimchicken"
    test.save()
    return HttpResponse("<p>成功</p>")
    
'''
