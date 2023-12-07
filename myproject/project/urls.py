from django.urls import path
from project import views
from .views import index, BBLoginView,aplication_admin_render,aplication_admin_done, RegisterView, createapl, aplication_render, \
    apl_filter
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', index, name='index'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(next_page='index'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', aplication_render, name='profile'),
    path('create_aplication/', createapl, name='createapl'),
    path('aplication_admin/', aplication_admin_render, name='aplication_admin_render'),
    path('aplication_admin_done/', aplication_admin_done, name='aplication_admin_done'),
    path('profile/<int:id>', views.delete, name='delete'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('change/<int:id>', views.changeapl, name='change'),
    path('readyapl/<int:id>', views.readyapl, name='readyapl'),
    path('profile/<str:status>', apl_filter, name='filter'),
]


