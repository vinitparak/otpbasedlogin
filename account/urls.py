from django.urls import path
from . import views
from django.conf import settings
from .views import OTPView, Logout, GetUserAPI,SearchResultsView,HomePageView, register, topic, topic_country, topic_language
from django.conf.urls import url


app_name = 'account'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('', OTPView.as_view(), name='otplogin'),
    path('logout', Logout.as_view(), name='logout'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('home/', HomePageView.as_view(), name='home'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('topics1/<str:topic_id>/', views.topic_country, name='topic1'),
    path('topics2/<int:topic_id>/', views.topic_language, name='topic2'),

    # API
    path('getuser', GetUserAPI.as_view(), name='getuser')
]
