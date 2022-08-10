import json

from django.shortcuts import render,HttpResponse

from .models import Greeting


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def test(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "test.html")


def medicine(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "medicine.html")


def search(request):
    try:
        rollno = request.GET["rollno"]
        d = {"status": "ok", "rollno": rollno, "result": "pasword"}
        d= json.dumps(d)
        return HttpResponse(d)
    except:
        d={"status":"error"}
        d= json.dumps(d)
        return HttpResponse(d)
def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

