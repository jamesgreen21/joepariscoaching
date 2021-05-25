from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User

# from sorl import thumbnail


class Profile(models.Model):
    """
    A Profile model that extends the User model in django auth
    """
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', "Don't specify"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICE,
        default='U'
    )
    address1 = models.CharField("Address line 1", max_length=1024, null=True, blank=True)
    address2 = models.CharField("Address line 2", max_length=1024, null=True, blank=True)
    city = models.CharField(max_length=1024, null=True, blank=True)
    postcode = models.CharField(max_length=12, null=True, blank=True)
    mobile = PhoneField(blank=True, help_text='Contact phone number')
    dob = models.DateField(null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, help_text='Height in CM', blank=True, null=True)
    # image = thumbnail.ImageField('Profile Pic', upload_to='accounts_img', default='accounts_img/logo.PNG')

    def __str__(self):
        return f'{self.user.username} Profile'

    # @property
    # def thumbnail(self):
    #     if self.image:
    #         return thumbnail.get_thumbnail(self.image, '50x50', quality=90)
    #     return None
