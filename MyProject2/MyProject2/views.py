from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Student1

def MyPage(request):
    txt="Hiii Pratik...!!"
    return HttpResponse(txt)


def MyShow(request):
    dict2={
        'roll':101,
        'name':'Pratik',
        'city':'Jalgaon'
    }
    return render(request,'index.html',dict2)

def MyAdd(request):
    dict1={
        'n1':0,
        'n2':0,
        'r1':0
        
    }
    if request.method == 'POST':
        no1=request.POST['no1']
        no2=request.POST['no2']
        res=request.POST['res']
        res=int(no1)+int(no2)
        dict1={
        'n1':no1,
        'n2':no2,
        'r1':res
        }
    return render(request,'add.html',dict1)


def ShowImg(request):
    return render(request, 'demo.html')


def MyStudent(request):
    if (request.method == 'POST'):
        r1=request.POST['roll']
        n1=request.POST['sname']
        c1=request.POST['city']
        co1=request.POST['country']
        s1=Student1(roll=r1,name=n1,city=c1,country=co1)
        s1.save()

    s1=Student1.objects.all()
    dict1={
        'data':s1
    }
    return render(request, 'stud.html',dict1)