from django.urls import path
from taskweb import views

urlpatterns=[
path("signup",views.SignUpView.as_view(),name="register"), 
path("",views.LoginView.as_view(),name="signin")  ,
path("home",views.IndexView.as_view(),name="home"),
path("tasks/add/",views.TaskcreateVIew.as_view(),name="task-add"),
path("tasks/all",views.TaskListView.as_view(),name="task-list"),
path("tasks/detail/<int:id>",views.TaskdetailView.as_view(),name="task-detail"),
path("tasks/delete/<int:id>",views.TaskDeleteView.as_view(),name="task-delete"),
path("tasks/edit/<int:id>",views.TaskEditView.as_view(),name="task-edit"),


]