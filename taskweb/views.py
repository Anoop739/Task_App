from django.shortcuts import render,redirect
from django.views.generic import View
from taskweb.forms import UserForm,LoginForm,TaskForm,TaskEditForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from api.models import Tasks
# Create your views here.

class SignUpView(View):
      def get(self,request,*args,**kwargs):
        form=UserForm()
        
        return render(request,"register.html",{"form":form})
      def post(self,request,*args,**kwargs):
        form=UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin") 
        else:
          return render(request,"register.html",{"form":form})    

class LoginView(View):
    def get(self,request,*args,**kwargs):
      form=LoginForm()
      return render(request,"login.html",{"form":form}) 
    def post(self,request,*args,**kwargs):
      form=LoginForm(request.POST)
      if form.is_valid():
        uname=form.cleaned_data.get("username")
        pwd=form.cleaned_data.get("password")
        usr=authenticate(request,username=uname,password=pwd) 
        if usr:
          login(request,usr)
          return redirect ("home")
        else:
          return render(request,"login.html",{"form":form})

class IndexView(View):
    def get(self,request,*args,**kwargs):

      return render(request,"index.html")


class TaskcreateVIew(View):
  def get(self,request,*args,**kwargs):
    form=TaskForm()
    return render(request,"task-add.html",{"form":form})
  def post(self,request,*args,**kwargs):
      form=TaskForm(request.POST)
      if form.is_valid():
        form.instance.user=request.user
        form.save()
        print("saved")
        return redirect("task-list")
      else: 
         
        return render(request,"task-add.html",{"form":form})
        
class TaskListView(View):
  def get(self,request,*args,**kwargs):
    qs=Tasks.objects.filter(user=request.user).order_by("-created_date")
    return render(request,"task-list.html",{"tasks":qs}) 

class TaskdetailView(View):
  def get(self,request,*args,**kwargs):
    id=kwargs.get("id")
    qs=Tasks.objects.get(id=id)
    return render(request,"task-detail.html",{"tasks":qs}) 

class TaskDeleteView(View):
  def get(self,request,*args,**kwargs):
     id=kwargs.get("id")
     qs=Tasks.objects.filter(id=id).delete()
     return redirect("task-list")
class TaskEditView(View):
  def get(self,request,*args,**kwargs):
     id=kwargs.get("id")
     obj=Tasks.objects.get(id=id)
     form=TaskEditForm(instance=obj)
     return render(request,"task-edit.html",{"form":form})

  def post(self,request,*args,**kwargs):
    id=kwargs.get("id")
    obj=Tasks.objects.get(id=id)
    form=TaskEditForm(request.POST,instance=obj)

    if form.is_valid():
        
        form.save()
        print("saved")
        return redirect("task-list")
    else: 
         
        return render(request,"task-edit.html",{"form":form})
        
     