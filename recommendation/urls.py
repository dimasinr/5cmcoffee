from django.urls import path
from . import views

app_name = 'recommendation'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_confirm, name='logout'),
    path('recommend/', views.recommendation_form, name='form'),
    path('result/', views.recommendation_result, name='result'),
    path('coffee/<int:pk>/', views.coffee_detail, name='coffee_detail'),
    path('admin-menu/', views.admin_menu, name='admin_menu'),
    path('admin-menu/add/', views.admin_menu_add, name='admin_menu_add'),
    path('admin-menu/edit/<int:pk>/', views.admin_menu_edit, name='admin_menu_edit'),
    path('admin-menu/delete/<int:pk>/', views.admin_menu_delete, name='admin_menu_delete'),
    path('admin-users/', views.admin_users, name='admin_users'),
    path('admin-users/add/', views.admin_user_add, name='admin_user_add'),
    path('admin-users/edit/<int:pk>/', views.admin_user_edit, name='admin_user_edit'),
    path('admin-users/delete/<int:pk>/', views.admin_user_delete, name='admin_user_delete'),
    path('admin-preferensi/', views.admin_preferensi, name='admin_preferensi'),
]
