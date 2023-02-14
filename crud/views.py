from django.shortcuts import render,redirect

# Create your views here.
from crud.models import Vehicle,User
from django.views.generic import ListView,UpdateView,View,CreateView
from django.contrib.auth.mixins import UserPassesTestMixin

from django.shortcuts import render
from crud.forms import VehicleUpdateForm,LoginForm,RegistrationForm,vehiclecreateform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator




def signin_reqired(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


@method_decorator(signin_reqired,name='dispatch')
class VehicleListView(ListView):
    model=Vehicle
    template_name="vehicle_list.html"
    context_object_name="vehicles"


@method_decorator(signin_reqired,name='dispatch')
class VehicleCreateView(UserPassesTestMixin, CreateView):
    model = Vehicle
    template_name = 'vehicles_create.html'
    form_class=vehiclecreateform
    success_url=reverse_lazy("list")
    
    def test_func(self):
        return self.request.user.can_create()


@method_decorator(signin_reqired,name='dispatch')
class VehicleUpdateView(UserPassesTestMixin, UpdateView):
    model = Vehicle
    template_name = 'vehicles_update.html'
    form_class=VehicleUpdateForm
    pk_url_kwarg="id"
    success_url=reverse_lazy("list")

    def test_func(self):
        return self.request.user.can_update()


@method_decorator(signin_reqired,name='dispatch')
class VehicleDeleteView(UserPassesTestMixin,View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Vehicle.objects.filter(id=id).delete()
        messages.success(request,'task deleted')
        return redirect("list")

    def test_func(self):
        return self.request.user.can_delete()


class RegistrationView(View,UserPassesTestMixin):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,'register.html',{'form':form})


    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,'account created')
            return redirect('signin')
        else:
            messages.error(request,'registration failed')
            return render(request,'register.html',{'form':form})


class LoginView(View,UserPassesTestMixin):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{'form':form})


    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,'login successfully')
                return redirect('list')
            else:
                messages.error(request,'invalid username or password')
                return render(request,'login.html',{'form':form})


@signin_reqired
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")