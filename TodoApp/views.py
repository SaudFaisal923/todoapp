from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import ToDoList
from TodoApp.form import TodoForm
from datetime import datetime, timedelta
from django.utils import timezone
def Start(request):
	obj=ToDoList.objects.all()
	return render(request,"TodoApp/show.html",{"obj":obj})

def CreateTask(request):
	if request.method=="POST":
		form=TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("start"))
		else:
			return HttpResponse("hmmmm...")
	else:
		form=TodoForm()
		return render(request,"TodoApp/index.html",{"Userform":form})
		
def CompleteTask(request,id):
	#you have completed your task
	#point=0
	obj=ToDoList.objects.get(id=id)
	obj.status=True
	#x=
	#d=x.strftime("%m-%d-%Y %H:%M:%S")
	#y=datetime.strptime(d,"%m-%d-%Y %H:%M:%S")
#print(x.date(),x.time())

	if obj.enddate>=timezone.now():
		obj.points=5
	else:
		obj.points=-5
	obj.save()
	print("points",obj.points)
	return HttpResponseRedirect(reverse("start"))
	

def DeleteTask(request,id):
		obj=ToDoList.objects.get(id=id)
		obj.delete()
		return HttpResponseRedirect(reverse("start"))
		
def History(request):
		obj=ToDoList.objects.all().order_by("enddate")
		return render(request,"TodoApp/history.html",{"obj":obj})
		

def progress(request):
		labels=[]
		dates=[]
		d=timezone.now()
		for d_t in range(0,7):
			d=d-timedelta(days=1)
			labels.append(d)
			query=ToDoList.objects.filter(status=True,startdate__day=d.day)
			for c in query:
				c.points.count()
			print(c)
			#dates.append(query.points.count())
		print(labels,dates)
		return render(request, "TodoApp/progress.html",{"labels":labels,"dates":dates})
			
		
		
		