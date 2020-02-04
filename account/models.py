from django.db import models
import random
from django.utils import timezone
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

User = get_user_model()

class OTPUser(models.Model):
    """
    otp model to authenticate
    """

    user = models.OneToOneField(User,
                            verbose_name=_("User"),
                            on_delete=models.CASCADE,
                            related_name='otp')
    
    otp = models.CharField(_("OTP"),
                        max_length=6,
                        blank=True,
                        null=True)

    otp_last_generated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username


    def generate_otp(self):
        return User.objects.make_random_password(length=6, allowed_chars='0123456789')

    def get_otp(self):
        if (not self.otp or
            timezone.now() > self.otp_last_generated + timezone.timedelta(minutes=settings.OTP_VALIDITY)):
            self.otp = self.generate_otp()
            self.save()
        return self.otp

    def validate_otp(self, otp):
        if (otp == self.otp and
            timezone.now() < self.otp_last_generated + timezone.timedelta(minutes=settings.OTP_VALIDITY)):
            self.otp = None
            self.save()
            return True
        return False


@receiver(post_save, sender=User)
def _post_otp_save(sender, instance, created, **kwargs):
    if created:
        OTPUser.objects.create(user=instance)



class city(models.Model):
    Name = models.CharField(max_length=35)
    CountryCode = models.CharField(max_length=3)
    District = models.CharField(max_length=20)
    Population = models.IntegerField()

    def __Str__(self):
        return self.Name

    
class country(models.Model):
    Code = models.CharField(max_length=3,primary_key = True,default="")
    Name = models.CharField(max_length=52,default="")
    Continent = models.CharField(max_length=20,default="Asia")
    Region = models.CharField(max_length=26,default="")
    SurfaceArea = models.FloatField(default='0.00', unique = False) 
    IndepYear = models.IntegerField(null = True)
    Population = models.IntegerField(null=True,default='0')
    LifeExpectancy = models.FloatField(null = True, unique=False) 
    GNP = models.FloatField(null = True,unique=False) 
    GNPOld = models.FloatField(null = True,unique=False) 
    LocalName = models.CharField(max_length=45,null=True)
    GovermentForm = models.CharField(max_length=45)
    HeadOfState = models.CharField(max_length=60,null = True)
    Capital = models.IntegerField(null = True)
    Code2 = models.CharField(max_length=2,null=True)

    def __str__(self):
        return self.Code
def random_string():
    return str(random.randint(1, 99999))

class countrylanguage(models.Model):
    CATEGORY_CHOICES = (
    ('T', 'True'),
    ('F', 'False'),
    )
    sl = models.AutoField(primary_key=True,auto_created = True)
    CountryCode = models.CharField(max_length=3)
    Language = models.CharField(max_length=30)
    IsOfficial = models.CharField(choices=CATEGORY_CHOICES, max_length=1,default="F")
    Percentage = models.FloatField(default=0.0)

    def __str__(self):
        return self.sl
class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.IntegerField(null = True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
        

