from django.shortcuts import render


def index(request):
    context = {"name": "swimchicken"}

    view_list = ["課程1", "課程2", "課程3"]
    context["view_list"] = view_list[1]

    view_dic = {"name": "swimchicken", "age": 28}
    context["view_dic"] = view_dic

    score = 89
    context["score"] = score

    enpty_list = []
    context["enpty_list"] = enpty_list

    return render(request, "index.html", context)
