from django.forms import ModelForm,Textarea,DateTimeInput
#from bootstrap_datepicker_plus import DateTimePickerInput                    
from .models import ToDoList

class TodoForm(ModelForm):
	class Meta:
		model=ToDoList
		fields=["title","tasks","task_type","startdate","enddate"]     
		widgets={
		'enddate': DateTimeInput(
		attrs={
                    "type":"datetime-local"
                },
        format='%Y-%m-%d %H:%i:%s'
		),
				'startdate': DateTimeInput(
		attrs={
                    "type":"datetime-local"
                },
        format='%Y-%m-%d %H:%i:%s'
		),
		}




