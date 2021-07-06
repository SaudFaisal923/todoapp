from django.db import models
from django.utils import timezone
from datetime import datetime
class ToDoList(models.Model):
	
	type=(("Important","Important"),("Very Important","Very important"))
	title=models.CharField(max_length=100,default="pay")
	tasks=models.TextField(verbose_name="description")
	task_type=models.CharField(choices=type,max_length=100)
	startdate=models.DateTimeField()
	enddate=models.DateTimeField()
	status=models.BooleanField(default=False)
	points=models.IntegerField(default=0)
	def __str__(self):
		return self.title
		
	@property
	def diff_date(self):
		return self.enddate-timezone.now()
	class Meta:
		ordering=["-id"]
		
		
	
	

	
	
	
	
	
	