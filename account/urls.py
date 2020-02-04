from django.urls import path
from . import views
from django.conf import settings
from .views import OTPView, Logout, GetUserAPI,SearchResultsView,HomePageView, register


app_name = 'account'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('', OTPView.as_view(), name='otplogin'),
    path('logout', Logout.as_view(), name='logout'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('home/', HomePageView.as_view(), name='home'),
  
    # API
    path('getuser', GetUserAPI.as_view(), name='getuser')
]
