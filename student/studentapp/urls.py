from django.urls import path
from studentapp import views

urlpatterns = [
    path('test/', views.test),
    path('create/', views.create),
    path('', views.student),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]
