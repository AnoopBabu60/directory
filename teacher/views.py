from django.shortcuts import render
from .forms import TeacherRegistration
from .models import User

# Create your views here.
def list_teachers(request):
	err_data=None
	teachers=User.objects.all()
	if request.method=='POST':
		error_message = None
		fm=TeacherRegistration(request.POST,request.FILES)
		if fm.is_valid():
			error_message = validateUser(User)
			if not error_message:
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
				err_data = {
	                'err_data': error_message,
	            }
	           

	else:
		fm=TeacherRegistration()	
		teachers=User.objects.all()

	return render(request,'teacher/list.html',{'form':fm,'teach':teachers,'err_data':err_data})


def validateUser(user):	
	error_message = None;
	if user.isExists(user):
		error_message = 'Email Address Already Registered..'
		return error_message

def single(request,id,slug):
	single=User.objects.get(id=id)

	return render(request,'teacher/single.html',{'single':single})

