from django.shortcuts import render
from .forms import TeacherRegistration
from .models import User

# Create your views here.
def list_teachers(request):
	if request.method=='POST':
		fm=TeacherRegistration(request.POST,request.FILES)
		if fm.is_valid():
			nm=fm.cleaned_data['firstname']
			nm=fm.cleaned_data['lastname']
			nm=fm.cleaned_data['email']
			nm=fm.cleaned_data['phone']
			nm=fm.cleaned_data['room']
			nm=fm.cleaned_data['subjects']
			reg=User(firstname=nm,lastname=nm,email=nm,phone=nm,room=nm,subjects=nm)
			fm.save()
			fm=TeacherRegistration()	
	else:
		fm=TeacherRegistration()	
		teachers=User.objects.all()

	return render(request,'teacher/list.html',{'form':fm,'teach':teachers})