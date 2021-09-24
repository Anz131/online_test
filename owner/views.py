from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

from owner import forms
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from owner.decorators import signin_required
from owner.forms import QusCreationForm, QusUpdationForm
from owner.models import Test
from django.contrib import messages


class UserCreationView(TemplateView):
    model=User
    form_class=forms.RegistrationForm
    template_name ="registration.html"
    context={}

    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form

        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            self.context = {"form": form}
            return render(request,self.template_name,self.context)


class SignInView(TemplateView):
    template_name="login.html"
    form_class=forms.LoginForm
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form

        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if request.user.is_superuser:
                    return redirect("userhome")
                return redirect("userhome")
            else:
                self.context = {"form": form}
                return render(request,self.template_name,self.context)

class UserHome(ListView):
    template_name = "user_home.html"
    model = Test
    context_object_name = "tests"

class OwnerHome(ListView):
    template_name = "home.html"
    model=Test
    context_object_name="tests"


def add_qus(request):
    context={}
    form=QusCreationForm()
    context["form"]=form
    if request.method=="POST":
        form=QusCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Question Created")
            return redirect("addqus")
        else:
            messages.error(request,"Question not added")
            context["form"] = form
            return render(request, "add_qus.html", context)

    return render(request,"add_qus.html",context)

class SignOutView(TemplateView):
    def get(self,request, *args, **kwargs):
        logout(request)
        return redirect("signin")

def questions(request):
    tests=Test.objects.all()
    context={}
    context["tests"]=tests
    return render(request,"userhome.html",context)

def admin_questions(request):
    tests=Test.objects.all()
    context={}
    context["tests"]=tests
    return render(request,"home.html",context)

class TestFinish(TemplateView):
    template_name = "testfinish.html"
    context={}

# class QusDetailView(DetailView):
#     template_name = "qus_detail.html"
#     model = Test
#     context_object_name = "test"
#     pk_url_kwarg = 'id'

# def editqus(request,id):
#     test=Test.objects.get(id=id)
#     form=QusUpdationForm(instance=test)
#     context={}
#     context["form"]=form
#     if request.method=="POST":
#         form=QusUpdationForm(instance=test,data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#         else:
#             context["form"]=form
#             return render(request,"editqus.html",context)
#     return render(request,"editqus.html",context)





