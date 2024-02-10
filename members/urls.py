from django.urls import path
from . import views
from pathlib import Path

#path = Path("C:/Users/PC/Desktop/my_world")
#print(len(str(path)))

urlpatterns =[
    path('', views.main, name= 'main'),
    path('members/', views.members,name='members'),
    path('members/details/<int:id>',views.details,name='details'),
    path('testing/', views.testing, name='testing'),
]