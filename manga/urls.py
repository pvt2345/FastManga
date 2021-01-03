from django.urls import path
from . import views

app_name = 'manga'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('all-manga/', views.all_manga, name='all_manga'),
    path('detail-manga/<str:manga_code>',views.detail_manga, name='detail_manga')
]