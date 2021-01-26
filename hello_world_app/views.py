from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .form import StudentRegistration
from .models import User,data
# Create your views here.
# def index(request):
#     return HttpResponse("<em>My Second App </em>")

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = data.objects.all()
    return render(request,'test_App/add_show.html',{'form':fm, 'stu':stud})

#Delete Function:
def delete_data(request,id):
    if request.method=='POST':
        pi = data.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')
#Update Function
def update_edit(request,id):
    if request.method=='POST':
        pi =data.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi =data.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
    return render(request , 'test_App/update.html',{'form':fm})