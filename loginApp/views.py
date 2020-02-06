from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import *
from .models import *
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.views import LoginView 


# Create your views here.

def index(request):

    data_user = Person.objects.all()
    
    return render (request,'loginApp/index.html',context = {'datauser': data_user})
'''
class Registration(View):

    def get(self, request):
        form = Registration()
        return render (request,'loginApp/registrationuser.html',context={'form':form}) 
    def post(self,request):
        dataform = Registration(request.POST)
        if dataform.is_valid():
            new_data_form = dataform.save()
            return redirect('user_list')
        return render (request,'loginApp/registrationuser.html',context = {'form':dataform})  
'''
class Auth(View):

    def get(self, request):
        form = Registration()
        return render (request,'loginApp/registrationuser.html',context={'form':form}) 
    def post(self,request):
        dataform = Registration(request.POST)
        if dataform.is_valid():
            new_data_form = dataform.save()
            return redirect('user_list')
        return render (request,'loginApp/registrationuser.html',context = {'form':dataform})
   





def changepassword(requests):

    currentpassword= request.user.password #user's current password

    form = ChangePasswordform(request.POST or None)

    if form.is_valid():
        currentpasswordentered= form.cleaned_data.get("lastpassword")
        password1= form.cleaned_data.get("newpassword1")
        password2= form.cleaned_data.get("newpassword2")

        matchcheck= check_password(currentpasswordentered, currentpassword)
'''
	if matchcheck:

        return None 
	    #change password code
'''


def process_request(self, request):
        if request.path.startswith('/admin/'):
            if not request.user.is_superuser:
                return redirect_to_login(request.path)
        # Continue processing the request as usual:
        return None 


    
    
#from django.shortcuts import render_to_response, redirect
#from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout

#from Person.forms.login import LoginForm
#from Person.forms.register import RegisterForm

def login(request):
    """Login view."""
    if request.method != 'POST':
        form = LoginForm()

    form = LoginForm(data=request.POST)

    if form.is_valid():
       person = authenticate(login=request.POST.get('logim'),
                              password=request.POST.get('password1'))
    if person is not None:
            if person.is_active:
                django_login(request,  person)
                return redirect('/')
    else:
        form = LoginForm()

    return render_to_response('login.html', {
        'form': form
    }, context_instance=RequestContext(request))

