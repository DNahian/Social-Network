from django.urls import path
from home.views import HomeView
from . import views
app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('connect/<operation>/<int:pk>/', views.change_friend, name='change_friend'),
]
