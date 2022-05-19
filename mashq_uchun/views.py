from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from .models import *

def salomlash(request):
    return HttpResponse('Salom dunyo')
def bosh(request):
    return render(request, 'salomlash.html')
def oquvchilar(request):
    s = ["Ahmadjon", 'Jamshidbek', 'Rahimjon']
    return render(request, 'oquvchilar.html', {'students': s})

def oquvchi(request, ism):
    s = ["Ahmadjon", 'Jamshidbek', 'Rahimjon']
    s.remove(ism)
    return render(request, 'oquvchi.html', {'students': s})

def all_students(request):
    talabalar = Student.objects.all()
    malumot = {
        "students": talabalar
    }
    return render(request, "students.html", malumot)