from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
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


def all_kitoblar(request):
    books = Kitob.objects.all()
    top = Kitob.objects.order_by("-sahifa")[:2]
    data = {
        'book': books,
        'sahifa': top
    }
    return render(request, 'Books.html', data)

def kitob_edit(request, pk):
    if request.method == 'POST':
        Kitob.objects.filter(id=pk).update(
            nom = request.POST.get('n'),
            sahifa = request.POST.get('s'),
            janr = request.POST.get('j'),
            sana = request.POST.get('d'),
            muallif = request.POST.get('m')
        )
        return redirect('/books/')
    kt = Kitob.objects.get(id=pk)
    data = {
        'kitob': kt,
        'muallif': Muallif.objects.all()
    }
    return render(request, 'kitob_edit.html', data)

def mualliflar(request):
    if request.method == 'POST':
        Muallif.objects.create(
            ism = request.POST.get('i'),
            yosh = request.POST.get('y'),
            jins = request.POST.get('j')
        )
        return redirect("/muallif/")
    mualliflar = Muallif.objects.all()
    flex = {
        'muallif': mualliflar
    }
    return render(request, 'muallif.html', flex)

def muallif_edit(request, pk):
    if request.method == 'POST':
        Muallif.objects.filter(id=pk).update(
            ism = request.POST.get('i'),
            yosh = request.POST.get('y'),
            tirik = request.POST['t'],
            jins = request.POST['j']
        )
        return redirect('/muallif/')
    ms = Muallif.objects.get(id=pk)
    data = {
        'mualliflar': ms
    }
    return render(request, 'muallif_edit.html', data)

def talaba(request, pk):
    Student.objects.filter(id=pk).delete()
    return redirect("/students/")

def muallif(request, pk):
    Muallif.objects.filter(id=pk).delete()
    return redirect('/muallif/')

def all_students(request):
    if request.method == 'POST':
        Student.objects.create(
            ism = request.POST.get('i'),
            guruh = request.POST.get('g'),
            kitob_soni = request.POST.get('k_s')
        )
        return redirect("/students/")
    talabalar = Student.objects.all()
    malumot = {
        "students": talabalar
    }
    return render(request, "index.html", malumot)
def bitta_student(request, pk):
    abc = {
        'talaba':Student.objects.get(id=pk)
    }
    return render(request, "student_first.html", abc)

def student_del(request, pk):
    Student.objects.filter(id=pk).delete()
    return redirect('/students')

def record(request):
    if request.method == 'POST':
        Record.objects.create(
            sana = request.POST.get('s'),
            student = Student.objects.get(id=request.POST.get('st')),
            kitob = Kitob.objects.get(id=request.POST.get('k')),
            qaytardi = request.POST.get('q'),
            qaytarish_sana = request.POST.get('q_s')
        )
        return redirect('/records')
    recordchilar = Record.objects.all()
    data = {
        'records': recordchilar,
        'kitob':Kitob.objects.all(),
        'student':Student.objects.all()
    }
    return render(request, "record.html", data)

def student_tahrirlash(request, pk):
    if request.method == 'POST':
        Student.objects.filter(id=pk).update(
            ism = request.POST.get('i'),
            guruh = request.POST.get('g'),
            kitob_soni = request.POST.get('k_s')
        )
        return redirect('/students/')
    st = Student.objects.get(id=pk)
    data = {
        'student': st
    }
    return render(request, 'students_edit.html', data)