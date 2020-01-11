from django.shortcuts import render
from .models import Todo
from django.http import HttpResponse,JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def addtask(request):
    try:
        obj = Todo()
        obj.todotitle = request.GET['todotitle']
        obj.tododescription = request.GET['tododescription']
        obj.save()
        mydict= {
            "taskadded" : True,
            "alltask" : Todo.objects.all()
        }
        return render(request,'list.html',context=mydict)
    except:
        return render(request,'404.html')


def listalltask(request):
    try:
        mydict = {
        "alltask": Todo.objects.all()
        }
        return render(request,'list.html',context=mydict)
    except:
        return render(request,'404.html')


def edittask(request,id):
    try:
        obj = Todo.objects.get(id=id)
        mydict = {
        "objid" : obj.id,
        "objtitle" : obj.todotitle,
        "objdescription" : obj.tododescription
        }
        return render(request,'edit.html',context=mydict)
    except:
        return render(request,'404.html')

def updatetask(request,id):
    try:
        obj = Todo.objects.get(id=id)
        obj.todotitle = request.GET['todotitle']
        obj.tododescription = request.GET['tododescription']
        obj.save()
        mydict = {
        "taskupdated" : True,
        "alltask" : Todo.objects.all()
        }
        return render(request,'list.html',context=mydict)
    except:
        return render(request,'404.html')

def deletetask(request,id):
    try:
        obj = Todo.objects.get(id=id)
        obj.delete()
        mydict = {
            "taskdeleted" : True,
            "alltask" : Todo.objects.all()
        }
        return render(request,'list.html',context=mydict)
    except:
        return render(request,'404.html')

