from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.encoding import force_text
from django.views.generic import FormView, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView
from .models import OTPUser, city, country, countrylanguage, Profile
from .forms import OTPForm, SignUpForm
from itertools import chain
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from .filters import UserFilter
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.profile.gender = form.cleaned_data.get('gender')
        user.profile.phone_number = form.cleaned_data.get('phone_number')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('account:home')
    else:
        form = SignUpForm()
    return render(request, 'account/register.html', {'form': form})


class OTPView(FormView):
    """
    OTP Login Form View
    """
    form_class = OTPForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('account:home')


    def get(self, request, *args, **kwargs):
        """
        If user already logged In
        """
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)

        return super(self.__class__, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        authenticate user otp
        """

        username = form.cleaned_data.get('username')
        otp = form.cleaned_data.get('otp')


        user = authenticate(username=username, otp=otp)
        # user = authenticate(username=username, password=otp)

        if user and user.is_active:
            login(self.request, user)
            return super(self.__class__, self).form_valid(form)

        # messages.error(self.request, 'Invalid OTP')
        return self.render_to_response(self.get_context_data(form=form))



class Logout(RedirectView):

    pattern_name = 'account:otplogin'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(self.__class__, self).get(request, *args, **kwargs)



# DRF VIEW For API Call
# These import should be on top
# Just to separately identify them they are here

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class GetUserAPI(APIView):
    
    def post(self, request, *args, **kwargs):
        otp = None
        username = request.POST.get('username')
        user = get_user_model().objects.filter(username=username).first()
        if user:
            otp = user.otp.get_otp()
            print(user.email)
            send_mail('OTP', f'Your OTP is {otp}', "forinternpurposes@gmail.com", [user.email])
            return Response({},status=status.HTTP_200_OK)
        return Response({"otp": 'No user found'},status=status.HTTP_400_BAD_REQUEST)


class SearchResultsView(ListView):
    template_name = 'data.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = city.objects.filter(Q(Name=query))
        object_con = country.objects.filter(Q(Name=query))
        object_lan = countrylanguage.objects.filter(Q(Language=query))
        return chain(object_list , object_con, object_lan)

class HomePageView(TemplateView):
    template_name = 'account/success.html'

def topic(request, topic_id):
    topic  = city.objects.all().filter(id=topic_id)
    return render(request, 'topic.html', {'topic':topic} )

def topic_country(request, topic_id):
    topic  = country.objects.all().filter(Code=topic_id)
    return render(request, 'topic1.html', {'topic':topic} )

def topic_language(request, topic_id):
    topic  = countrylanguage.objects.all().filter(sl=topic_id)
    return render(request, 'topic2.html', {'topic':topic} )








