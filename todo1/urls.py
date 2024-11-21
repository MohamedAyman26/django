# urls.py في تطبيقك
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),  # الصفحة الرئيسية
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('delete-task/<str:name>/', views.DeleteTask, name='delete'),  # نمط الحذف
    path('update-task/<str:name>/', views.Update, name='update'),  # نمط التحديث
]